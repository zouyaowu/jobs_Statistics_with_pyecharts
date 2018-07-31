# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        对excel 操作的封装
# Purpose:     支持 2007及以后的 xecel 版本
#
# Author:      zou.yw
#
# Created:     2018/4/27
# Modifiy:
# Copyright:   (c) zou.yw 2018
# Licence:     GPL
#-------------------------------------------------------------------------------


# from openpyxl import Workbook, load_workbook
from public import *
import operator
import os
import re
from xml.etree.ElementTree import ElementTree,Element
import sqlite3


class To_be_verified(public_methods):

    def __data_format(self,data):
        """
        功能：对数据做格式化处理
        """
        try:
            if isinstance(data, list):
                for i in range(len(data)):
                    tmp_data = str(data)
                    tmp_data = tmp_data.strip()
                    tmp_data = data[i].lower()
                    tmp_data = tmp_data.replace("\\","/")
                    data[i] = tmp_data
            else:
                tmp_data = str(data)
                tmp_data = tmp_data.lower()
                tmp_data = tmp_data.strip()
                tmp_data = tmp_data.replace("\\","/")
                data = tmp_data
            return data
        except Exception as err:
            # print(err)
            return None


    def __get_file_list(self,file_path=None):
        """获取文件夹列表"""
        if not file_path:
            return None
        # file_set = set()
        file_list = []
        try:
            for fpath, dirs, fs in os.walk(file_path):
                # file_set = file_set | set(fs)
                file_list.extend(fs)
        except:
            pass
            # return (file_set)
        return (file_list)


    def __clean_verified_excel(self,excelfile=None):
        """清空待验证补丁文档"""
        pass


    def __creat_sqlite(self):
        """创建sqlite数据库存放数据"""
        # con = sqlite3.connect(":memory:")
        con = sqlite3.connect('test.db3')
        cur = con.cursor()
        tb_name = "check_in_datas"
        # 对应DLL文件, 是否与人力相关, 问题/需求编号, 功能/问题修改说明, SQL脚本/报表/其它配置文件(含路径), 修改人, 修改日期,
        # 验证状态, 验证人, 验证日期, 打包日期, 是否接口（EDI接口、电商服务、端点）配合升级，模块名称, ERP版本
        cur.executescript("""drop table if exists check_in_datas""")
        cur.executescript("""
            create table if not exists check_in_datas(
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            dll char(255),
            hr_related interger,
            demand_number char(255),
            change_describe char(1024),
            sql_script char(1024),
            author char(255),
            date_commit char(255),
            status char(255),
            tester char(255),
            date_test char(255),
            date_pack char(255),
            other_api char(255),
            sheet_name char(255),
            erp_version char(255))""")
        # cur.close()
        return (con, cur, tb_name)


    def excel_date_to_db(self,excel_file=None):
        """把excel内容存入数据库
        """
        con, cur, table_name = self.__creat_sqlite()
        excel_data = self.read_excel(excel_file,pack="dict")
        tmp = excel_file.split('\\')[-1]
        version = tmp.split('服装')[0]
        if not excel_data:
            return None
        # excel表中的标题栏，与数据库的字段名称进行对应，记录在excel标题栏中的位置
        # 此列表的顺序非常重要，要与后面的sql语句的插入字段的顺序对应
        sql_table_fileds = ["对应DLL文件", "是否与人力相关", "问题/需求编号", "功能/问题修改说明", "SQL脚本/报表/其它配置文件(含路径)", "修改人", "修改日期", "验证状态", "验证人", "验证日期", "打包日期", "是否接口（EDI接口、电商服务、端点）配合升级"]
        fls_v = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        for sheet_name in excel_data:
            sheet_date = excel_data[sheet_name]
            # print(sheet_name, len(excel_data[sheet_name]))
            # 遍历 excel 标题栏字段与 数据库字段 对应关系的字典
            if not "对应DLL文件" in sheet_date[0]:
                continue
            for x in range(len(sql_table_fileds)):
                try:
                    if sql_table_fileds[x] in sheet_date[0]:
                        # 定位到 要写入数据库的字段内容在哪一列
                        fls_v[x] = sheet_date[0].index(sql_table_fileds[x])
                except Exception as bug:
                    print(bug)

            for rows in sheet_date[1:-1]:
                if fls_v[1] == -1:
                    rows[fls_v[1]] = ""
                cur.execute(
                    'insert into '+ table_name + '(dll, hr_related, demand_number, change_describe, sql_script, author, ' \
                    'date_commit, status, tester, date_test, date_pack, other_api, sheet_name, erp_version) ' \
                    'values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (rows[fls_v[0]],"",rows[fls_v[2]],rows[fls_v[3]],rows[fls_v[4]],rows[fls_v[5]],rows[fls_v[6]],rows[fls_v[7]],
                     rows[fls_v[8]],rows[fls_v[9]],rows[fls_v[10]],rows[fls_v[11]],sheet_name,version))
            # cur.execute("select sheet_name, erp_version, count(dll) from " + table_name + " where not status = '' and sheet_name = '电商'")
        # cur.execute("select * from "+ table_name)
        # print(cur.fetchall())
        # cur.close()
        con.commit()
        return (cur, table_name)


    def get_updateFiles_from_excel(self,excel_file=None):
        """
        功能：待验证补丁表格文档读取
        入参：表格文件路径
        返回：提取出文件中包含的所有文件（报表、dll、sql 等）（3个返回结果）
        """
        dll_set = list()
        script_set = list()
        sql_set_tmp = set()
        # 非脚本、ERP的DLL、EXE文件（比如：订单推送、端点同步、宝胜官网接口）
        except_file = set()
        excel_data = self.read_excel(data=excel_file, read_type='row')
        if not excel_data:
            print("read excel %s err" % excel_file)
            return 0
        # print(excel_data)
        # 根据表格的排列，确定dll文件放到第几列，脚本文件放在第几列
        dll_index = 0
        sql_index = 3
        # 表头特征
        # tabel_head = (r'修改日期', r'对应DLL文件', r'SQL脚本/报表/其它配置文件(含路径')
        # 遍历表格，替换字符串，方便去重
        # 遍历每个工作簿
        for key in excel_data:
            # 遍历字典中的每个值（嵌套的列表），等同于excel的一张工作表
            sheet_data = excel_data[key]
            # print(sheet_data)
            # 遍历每个列表（等同于excel的每一行/每一列）
            for cells in sheet_data:
                if '修改日期' in cells:
                    try:
                        dll_index = cells.index(r'对应DLL文件')
                        sql_index = cells.index(r'SQL脚本/报表/其它配置文件(含路径)')
                    except:
                        dll_index = 0
                        sql_index = 3
                else:
                    # 把一个单元格内的多行拆分出来
                    # 用data_format格式化数据，方便后面的去重
                    dll_tmp = self.__data_format(cells[dll_index]).split('\n')
                    if dll_tmp != ['']:
                        dll_set.extend(dll_tmp)
                    script_tmp = self.__data_format(cells[sql_index]).split('\n')
                    if script_tmp != ['']:
                        script_set.extend(script_tmp)
        # 去重，把相同路径下同名文件合并
        script_tmp = list(set(script_set))
        script_set_tmp = set()
        for i in script_tmp:
            try:
                tmp = i.index('hkdatabase')
                t = i.split('hkdatabase')[-1]
                script_set_tmp.add(self.__data_format(t))
            except:
                except_file.add(i)
        # 把脚本、报表的服务器路径剔除
        script_set = []
        for i in script_set_tmp:
            t = i.split('/')[-1]
            if t != ['']:
                script_set.append(self.__data_format(t))
        """
        except_file = list(except_file)
        for i in range(len(except_file)):
            t = except_file[i].split('/')[-1]
            if t != ['']:
                except_file[i] = self.__data_format(t)
        """
        # dll_set.remove('')
        # script_set.remove('')
        return (dll_set, script_set, except_file)


    def patch_check(self,path='./', excel_file=None):
        """
        功能：待验证补丁检查，通过待验证补丁文档内的内容与本地实际文件做对比
        参数：
            入参：path=补丁目录（如果没有则默认当前目录）;
                      execel_file=表格文件路径（可选）如果没有表格路径，则读取目录中的第一个 .xlsx 文件
        """
        # 如果不传 excel 文件名，则在检查目录总查找
        if not excel_file:
            for i in os.listdir(path):
                if os.path.splitext(i)[1].lower() == '.xlsx':
                    if path[-1] != '/' or path[-1] != '\\':
                        path += '/'
                    excel_file = path + i
                    break
        if not os.path.exists(excel_file):
            if os.path.exists(path + '/' + excel_file):
                excel_file = path + '/' + excel_file
            else:
                print('%s not exist' % excel_file)
                return None
        dll = sql = list()
        dll_check = sql_check = None
        print(excel_file)
        dll, sql, exc_file = self.get_updateFiles_from_excel(excel_file)
        programe_file = ('.dll', '.exe', '.lib')
        script_file = ('.sql', '.rps')
        # 不检查的文件，如：版本号更新文件，视图刷新脚本
        no_check = ('版本脚本.sql', '视图刷新脚本.sql')
        for t in range(len(dll)):
            # 有部分人员签入不喜欢带上后缀，exe、lib 等
            dll[t] = self.__data_format(dll[t])
            if dll[t][-4:] in programe_file:
                dll[t] = dll[t][0:-4]
        # 去重
        dll_tmp = set(dll)
        dll = list(dll_tmp)
        dll.sort()
        dll_for_check = dll.copy()

        sql.sort()
        for i in range(sql.count('')):
            sql.remove('')
        sql_for_check = sql.copy()
        for t in range(len(sql_for_check)):
            sql_for_check[t] = self.__data_format(sql_for_check[t])
            # 调试步骤
            # print(sql_for_check[t])
            if sql_for_check[t][-4:] not in script_file:
                sql_for_check[t] += '.sql'

        # 本地文件遍历
        local_file = list()
        local_dll_list = list()
        local_sql_list = list()
        local_except_file = list()
        for k in ('程序', '报表', '脚本', '人力web'):
            local_file.extend(self.__data_format(self.__get_file_list(path + k)))
        for t in local_file:
            first_name, last_name = os.path.splitext(t)
            if last_name.lower() in programe_file:
                # 程序文件取不带后缀的文件名进行比较
                local_dll_list.append(self.__data_format(first_name))
            elif last_name.lower() in script_file:
                local_sql_list.append(self.__data_format(t))
            else:
                local_except_file.append(self.__data_format(t))
        local_dll_list.sort()
        local_sql_list.sort()
        for k in no_check:
            # 有可能有多个位置存放了不需要检查的脚本（如：脚本更新.sql）
            # 只保留其中一条，避免检查出错
            for t in range(local_sql_list.count(k)):
                local_sql_list.remove(k)

        dll_miss_in_excel = list()
        if operator.eq(dll_for_check, local_dll_list):
            print('dll 文件检查正常\n')
            dll = None
            dll_check = True
        else:
            for t in local_dll_list:
                # excel 中的元素去掉本地找到的列表元素
                # print("lcd:", local_dll_list)
                # print("ecd:", dll_for_check)
                try:
                    index_t = dll_for_check.index(t)
                    dll.pop(index_t)
                    dll_for_check.pop(index_t)
                except ValueError:
                    dll_miss_in_excel.append(t)
                except Exception as bug:
                    print("we have a bug", bug)

            # if dll:
                # print("excel文件中存在，在本地没有找到的dll：")
                # print(dll)
                # print()
            # if dll_miss_in_excel:
                # print("本地找到，excel中没有 或 此dll不在excel表格的“dll”列中：")
                # print(dll_miss_in_excel)


        sql_miss_in_excel = list()
        if operator.eq(sql_for_check, local_sql_list):
            print('sql 文件检查正常\n')
            sql_check = True
            sql = None
        else:
            sql_tmp = list()
            for k in local_sql_list:
                # excel 中的元素去掉本地找到的列表元素
                try:
                    index_t = sql_for_check.index(k)
                    sql_tmp.append(sql.pop(index_t))
                    sql_for_check.pop(index_t)
                except ValueError:
                    sql_miss_in_excel.append(k)
                except Exception as bug:
                    print("wo have a bug:", bug)

            # if sql:
                # print("excel文件中存在，在本地没有找到的脚本：")
                # print(sql)
                # print()
            # if sql_miss_in_excel:
                # print("本地找到，excel中没有或脚本贴的单元格错误的脚本：")
                # print(sql_miss_in_excel)

        # 不是脚本、不是程序的内容
        # f exc_file:
            # print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # print("此部分不属于 ERP脚本或程序，请人工检查:")
            # print(exc_file)
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        if dll_check and sql_check:
            # dll、sql 都没有问题，校验通过
            # print(dll,sql)
            return {"result":True, 'exc_file':exc_file}
        else:
            # 返回的内容包括：本地缺失的dll、excel缺失的dll、本地确实的sql、excel缺失的sql
            # print({"result":False, "dll_local_miss":dll, "dll_excel_miss":dll_miss_in_excel, "sql_local_miss":sql, "sql_excel_miss":sql_miss_in_excel, '请手动检查':exc_file})
            return {"result":False, "本地缺失的dll":dll, "excel缺失的dll":dll_miss_in_excel, "本地缺失的sql":sql, "excel缺失的sql":sql_miss_in_excel, '请手动检查':exc_file}
        # 返回的内容包括：本地缺失的dll、excel缺失的dll、本地确实的sql、excel缺失的sql
        # return (dll, dll_miss_in_excel, sql, sql_miss_in_excel, exc_file)


    def generation_update_instructions(self,excel_file=None, output='new.xlsx'):
        """
        根据待验证补丁文档，整理出一份新功能列表
        """
        # 新建一个文件，用来存放输出结果
        wb_new = Workbook()
        # 新建一张表
        ws_new = wb_new.active
        # 新增一行表头
        ws_new.append(['版本新功能列表'])
        ws_new.append(["序号", "类型", "系统模块", "恒康需求编号", "客户需求编号", "涉及的客户", "功能名称/修改说明", "对现有业务的影响", "备注"])

        try:
            # 打开文件
            workbook = load_workbook(excel_file)
            # 获取所有sheet，返回列表，格式：[u'sheet1', u'sheet2']
            workbook_sheets_list = workbook.sheetnames
            # print(workbook_sheets_list)
            # 根据特定字段来查找需要的内容
            bugid_trait = '问题/需求编号'
            modification_trait = '功能/问题修改说明'
            bugid_index = 1
            modification_index = 2
            for i in workbook_sheets_list:
                sheet = workbook[i]
                # 遍历工作簿所有单元格
                row_flag = 1
                for j in sheet.rows:
                    # 第一行是标题栏
                    if row_flag == 1:
                        for k in range(len(j)):
                            if j[k].value == bugid_trait:
                                bugid_index = k
                            elif j[k].value == modification_trait:
                                modification_index = k
                    else:
                        # 剔除空白行
                        if j[bugid_index].value or j[modification_index].value:
                            bug_id = ''
                            demand_id = ''
                            bug_or_demand = str(j[bugid_index].value)
                            bug_or_demand = bug_or_demand.strip()
                            if bug_or_demand != 'None':
                                if str(bug_or_demand)[0:1].isalpha() and str(bug_or_demand)[0:3].lower() != 'bug':
                                    demand_id = bug_or_demand
                                else:
                                    bug_id = bug_or_demand
                            ws_new.append(
                                ['', bug_id, sheet.title, demand_id, '', '', j[modification_index].value, '', ''])
                    row_flag += 1
        except  Exception as bug:
            ws_new.append(['we have a problme. i have a bug'])
            print(bug)
            # print(j[bugid_index].value)
        finally:
            try:
                wb_new.save(output)
            except  Exception as err:
                print('无法保存文件，文件可能正在被编辑')
        return


    def create_upgrade_package(self,pack_path=None,version=None,last_version=None):
        """自动整理要发布的补丁
        1、拷贝待验证补丁的文件；2、修改程序版本号、修改数据库版本号；3、根据文档标签，删除不需要的内容"""


    def unfinished_test(self,excel_file=None):
        """根据补丁文档，提取出完成（测试结果非空）、未完成测试（测试结果为空）的结果"""
        excel_data = self.read_excel(excel_file,pack="dict")
        if not excel_data:
            return None
        check_result = {}
        for key in excel_data:
            sheet_data = excel_data[key]
            # print(key)
            # state_index = 0
            try:
                state_index = sheet_data[0].index(r'验证状态')
            except:
                state_index = 0
                # print('err')
            # print(key,":",state_index)
            undone = 0
            done = -1 # 会把标题也算进去，故要减掉标题的那行计数
            for rows in sheet_data:
                # 遍历每一行
                for cell in rows:
                    # 有单元格非空表示此行要做检查，否则认为是空行
                    if cell != '':
                        # 【验证状态】这一列没有结果的，统计出来
                        if rows[state_index] == '':
                            undone += 1
                        else:
                            done += 1
                        break
            check_result[key] = {'done':done, 'undone': undone}
        return check_result
            # print(key,"(undone):",undone)
            # print(key, "(done):", done)


    def specify_data_list(self, excel_file=None):
        excel_data = self.read_excel(excel_file,pack="dict")
        if not excel_data:
            return None
        check_result = {}
        for key in excel_data:
            sheet_data = excel_data[key]
            print(sheet_data)
            # state_index = 0
            try:
                state_index = sheet_data[0].index(r'验证状态')
            except:
                state_index = 0
                # print('err')
            # print(key,":",state_index)

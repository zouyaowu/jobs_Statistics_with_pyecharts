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
import copy
import shutil
from xml.etree.ElementTree import ElementTree,Element
import sqlite3
import xml.etree.ElementTree as xml_ET


class To_be_verified(public_methods):

    def __init__(self):
        # 数据库连接
        self.con = sqlite3.connect(":memory:") #  内存数据库
        # self.con = sqlite3.connect('erp_i.db3')  # 存入文件中
        self.cur = self.con.cursor()
        self.table_name = "check_in_datas"


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


    def get_file_list(self,file_path=None):
        """获取文件夹列表"""
        if not file_path:
            return None
        # file_set = set()
        file_list = []
        files_modify_date = {}
        try:
            for fpath, dirs, fs in os.walk(file_path):
                # file_set = file_set | set(fs)
                # file_list.extend(fs)
                # 获取文件修改时间
                for file in fs:
                    full_path = os.path.join(fpath, file)
                    mtime = os.stat(full_path).st_mtime
                    file_modify_time = time.strftime('%Y-%m-%d', time.localtime(mtime))
                    files_modify_date[file] = file_modify_time
        except Exception as err:
            print("Get file ist err :%s", str(err))
            # return (file_set)
        return (files_modify_date)


    def __clean_verified_excel(self,excelfile=None):
        """清空待验证补丁文档"""
        pass


    def __creat_sqlite(self):
        """创建sqlite数据库存放数据"""
        # 对应DLL文件, 是否与人力相关, 问题/需求编号, 功能/问题修改说明, SQL脚本/报表/其它配置文件(含路径), 修改人, 修改日期,
        # 验证状态, 验证人, 验证日期, 打包日期, 是否接口（EDI接口、电商服务、端点）配合升级，模块名称, ERP版本，行号，是否挑出
        # self.cur.executescript("""drop table if exists """ + tb_name)
        self.cur.executescript("""drop table if exists """ + self.table_name)
        self.cur.executescript("""
            create table if not exists check_in_datas(
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            row_number char(255),
            dll char(255),
            hr_related char(1),
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
            erp_version char(255),
            not_update char(1)
        )""")
        self.cur.executescript("""
            create table if not exists dlls(
                rid INTEGER PRIMARY KEY AUTOINCREMENT,
                row_number char(255),
                dll char(255),
                not_update char(1)
        )""")
        self.cur.executescript("""
            create table if not exists sqls(
                rid INTEGER PRIMARY KEY AUTOINCREMENT,
                row_number char(255),
                sql_script char(1024),
                not_update char(1)
        )""")
        # self.cur.close()
        return True


    def insert_to_db(self,cur=None,table_name=None,**data):
        """插入数据到数据库
        data：要插入的参数，字典类型，按照下面字段
        dll,hr_related,demand_number,change_describe,sql_script,author,date_commit,status,tester,date_test,date_pack
        other_api,sheet_name,erp_version,row_number"""
        # 没有数据库连接、插入的表名
        if not cur or not table_name:
            return "没有数据库连接或插入的表名称"
        # 插入数据库的字段，必须要用 列表，因为先后顺序有要求
        setment = ["row_number","dll","hr_related","demand_number","change_describe","sql_script","author","date_commit",
                    "status","tester","date_test","date_pack","other_api","sheet_name","erp_version","not_update"]
        # 传入的参数超过了预期
        if len(data) > len(setment):
            return "传入参数个数超过预期数量"
        # 插入数据库的字段、对应的值
        insert_setment = []
        # 数据表中第一行是自增数据库，在插入时，此字段传None值
        insert_values = [None]
        for k in setment:
            insert_setment.append(k)
            if k in data.keys():
                insert_values.append(data[k])
            else:
                insert_values.append("0")
        # 根据数据库中的字段，自动匹配sql语句的占位符
        insert_tmp = ('?,'*(len(setment)+1))[:-1]
        # 插入字段，需要元组的格式，并且需要是字符串类型
        cur.execute('insert into ' + table_name + " values (" + insert_tmp + ')', (tuple(insert_values)))
        # 不实时提交，否则性能太低
        # self.con.commit()
        return True


    def pack_insert_to_db_data(self,**data):
        """把插入数据库的数据进行整理，把excel表格中一个单元格的多行数据分成多条记录
        data是一个字典，与 insert_to_db 里面的data格式一致"""
        v_tmp = []
        # print(type(data))
        # 记录拆分后的记录最长的长度
        cnt = 0
        for k, v in data.items():
            if v:
                # tmp.append(str(v).split('\n'))
                # 按照【逗号，换行符，空格】把他们分成多个记录
                v_tmp = re.split(r'[ ,\n]',str(v))
                # 在分拆成记录时，会有部分空格被当成单独的记录，清理掉这些空值
                while '' in v_tmp:
                    v_tmp.remove('')
                # 把成多个记录的列表覆盖原来的值
                data[k] = v_tmp
                # 记录拆成记录后最长是多少
                if len(v_tmp) > cnt:
                    cnt = len(v_tmp)

        # 根据最多的记录数量，把整个字典复制对应次，反回的数据即可直接插入数据库
        copy_data = []
        for i in range(0, cnt):
            # 用于存放临时复制的字典
            copy_dict = {}
            for key_word in data:
                # print(data[key_word])
                if data[key_word]:
                    # 如果没有多行，跳过
                    try:
                        copy_dict[key_word] = data[key_word][i]
                        # print(data[key_word][i])
                    except Exception as bug:
                        # copy_dict[key_word] = data[key_word][0]
                        # print(bug)
                        copy_dict[key_word] = None
                else:
                    copy_dict[key_word] = None
            copy_data.append(copy_dict)

        return copy_data


    def excel_date_to_db(self,excel_file=None,version=None):
        """把excel内容存入数据库
        """
        if not self.__creat_sqlite():
            print("创建表失败")
            return False
        excel_data = self.read_excel(excel_file,read_type='column',pack="dict")
        # print(self.get_excel_max_rows_and_colums(excel_file))
        # print(excel_data)
        # exit(0)
        # 如果没有传版本号进来，读取日期
        # if not version:
            # tmp = excel_file.split('\\')[-1]
            # version = tmp.split('服装')[0]
            # version = str((time.strftime("%Y%m%d%H%M%S", time.localtime())))
        if not excel_data:
            print("can not get data from:",excel_file)
            return None
        # 对应excel表格中的字段，通过这些作为关键字形成字典
        # sql_files = {"对应DLL文件":None, "是否与人力相关":None, "问题/需求编号":None, "功能/问题修改说明":None,
                            # "SQL脚本/报表/其它配置文件(含路径)":None, "修改人":None, "修改日期":None, "验证状态":None,
                            # "验证人":None, "验证日期":None,"打包日期":None,
                            # "是否接口（EDI接口、电商服务、端点）配合升级":None}

        # {excel表格字段 : [数据库字段(外键), 从表格读取到的值]
        # sql_files = {"对应DLL文件": ["dll", None], "是否与人力相关": ["hr_related", None], "问题/需求编号": ["demand_number", None],
        #              "功能/问题修改说明": ["change_describe", None],
        #              "SQL脚本/报表/其它配置文件(含路径)": ["sql_script", None], "修改人": ["author", None],
        #              "修改日期": ["date_commit", None], "验证状态": ["status", None],
        #              "验证人": ["tester", None], "验证日期": ["date_test", None], "打包日期": ["date_pack", None],
        #              "是否接口（EDI接口、电商服务、端点）配合升级": ["other_api", None]}

        sql_files = {"对应DLL文件": "dll", "是否与人力相关": "hr_related", "问题/需求编号": "demand_number",
                     "功能/问题修改说明": "change_describe","SQL脚本/报表/其它配置文件(含路径)": "sql_script","修改人": "author",
                     "修改日期": "date_commit", "验证状态": "status","验证人": "tester","验证日期": "date_test",
                     "打包日期": "date_pack","是否接口（EDI接口、电商服务、端点）配合升级": "other_api"}
        # {数据库字段(外键) : 要插入数据库的值}
        insert_data_mod = {"row_number":None,"dll":None,"hr_related":None,"demand_number":None,"change_describe":None,
                       "sql_script":None,"author":None,"date_commit":None,"status":None,"tester":None,"date_test":None,
                       "date_pack":None,"other_api":None,"sheet_name":None,"erp_version":None,"not_update":None}

        # {数据库字段名称:{excel表字段名称, 准备写入数据库的值}, ...}
        # sql_files = {"dll": {"对应DLL文件", None}, "hr_related": {"是否与人力相关", None}, "demand_number": {"需求编号",None},
        #             "change_describe": {"功能/问题修改说明", None}, "sql_script": {"SQL脚本/报表/其它配置文件", None},
        #             "author": {"修改人", None}, "date_commit": {"修改日期", None}, "status": {"验证状态", None},
        #             "tester": {"验证人", None}, "date_test": {"验证日期",None}, "date_pack": {"打包日期",None},
        #             "other_api": {"是否接口（EDI接口、电商服务、端点）配合升级", None}}
        # len(excel_data) 读取的excel 里面有多少个【工作表】
        # len(excel_data[0]) 每个【工作表】有多少列
        # len(excel_data[0][0]) 每列有多少个数据
        # for sheet in excel_data:  # 表长度 (遍历所有【工作表】)
        #    for row in column: # 行长度
        #        for column in sheet: # 列长度（遍历列）

        for sheets_name in excel_data:
            # 表格第一行第一列，如果不是“对应DLL文件”，则认为这个表格不是目标表格，跳过
            try:
                if excel_data[sheets_name][0][0] != "对应DLL文件":
                    raise NoData
            except Exception as NoData:
                continue
            # 表格数据行数
            row_len = len(excel_data[sheets_name][0])
            # 每行
            for row in range(1, row_len):
                # 每次都要清空数据
                insert_data = copy.deepcopy(insert_data_mod)
                # 每列
                for column in excel_data[sheets_name]:
                    # 第一列第一个，表格的字段名称
                    field = column[0]
                    # 有些第一行为空的列）
                    if not field:
                        continue
                    # insert_data[sql_files[field]] 对应数据库中的字段名，如：dll、demand_number、sql_script
                    try:
                        insert_data[sql_files[field]] = column[row]
                    except:
                        print("处理数据失败")
                        print(excel_file)
                        print(sheets_name)
                        print(column)
                        return False
                # 版本号
                insert_data["erp_version"] = str(version)
                insert_data["row_number"] = row
                insert_data["sheet_name"] = sheets_name
                # 每一行插入一条数据
                self.insert_to_db(self.cur, self.table_name, **insert_data)
        self.con.commit()
        # self.cur.close()
        return True


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

    def time_tag(self):
        return time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))

    def check_update_files_and_local_files(self,check_path='./', excel_file=None):
        """
        升级文件检查
        :return:字典 {resulst: true/false, excel_file_miss_in_local:[], local_miss_in_excel:[], files_time_mstake:[]}
        """
        # 记录日志
        log_info = []
        # 默认返回
        res = {'result': False, 'excel_file_miss_in_local': [], 'local_miss_in_excel': [], 'files_time_mstake': [], 'log_info': []}

        # 获取本地文件列表（文件名、修改日期）
        file_name_and_modify_date = self.get_file_list(check_path)
        file_name_keys = list(file_name_and_modify_date.keys())
        file_name = set(s.lower() for s in file_name_keys if isinstance(s, str) == True)
        log_info.append([self.time_tag, "找到的文件", file_name])

        # 排除的文件记录在一个文本文件每次读出，本地文件列表中，删掉这些要排除的
        ignore_file_name = ()
        with open("ignore.txt", "r") as f:
            ignore_file_name_tmp = f.readlines()
        ignore_file_name = set(s.replace("\n","").lower() for s in ignore_file_name_tmp)
        file_name = file_name - ignore_file_name
        # 逐行对比excel记录（先存入表格中），检查文件名、修改日期
        # version = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
        version = self.time_tag
        if not self.excel_date_to_db(excel_file, version):
            print("无法创建数据表")
            log_info.append([self.time_tag, "创建数据表失败"])
            res['log_info'] = log_info
            return res
        # 此处应该要动态配置表名，但是用 (?) 方式会导致报错，待解决
        getfile_sql = "select sheet_name,row_number,dll,sql_script,date_pack from check_in_datas"
        cor = self.cur.execute(getfile_sql)
        # 记录找到的 文件名称
        excel_dll_files_found_in_local = []
        excel_sql_files_found_in_local = []
        # 未找到的文件
        excel_dll_files_not_found_in_local = []
        excel_sql_files_not_found_in_local = []
        for i in cor.fetchall():
            # 数据库里面的程序列
            row_number = i[1]
            excel_dll = i[2]
            # 数据库记录的excel脚本列
            excel_sql = i[3]
            excel_date_pack = i[4]
            excel_sql = excel_sql.replace("\\", "/")
            excel_dll = excel_dll.replace("\\","/")
            # 逐行检查
            for k in excel_dll.split("\n"):
                # dll这栏可能没写后缀名,是 dll 或 exe，目前暂未出现dll与exe的文件名一致的
                k = k.strip()
                if len(k) > 4:
                    if k[-4:].lower() == ".dll" or k[-4:].lower() == ".exe":
                        tmp_exe = tmp_dll = k.lower()
                    else:
                        tmp_dll = k + ".dll"
                        tmp_exe = k + ".exe"
                else:
                    tmp_dll = k + ".dll"
                    tmp_exe = k + ".exe"
                # print(tmp_dll.lower(), "in ", file_name)
                if tmp_dll.lower() in file_name:
                    excel_dll_files_found_in_local.append(tmp_dll.lower())
                elif tmp_exe.lower() in file_name:
                    excel_dll_files_found_in_local.append(tmp_exe.lower())
                else:
                    # 没有找到文件
                    if k:
                        log_info.append([self.time_tag, "excel行：",row_number, "==没找到的程序==" , k, file_name])
                        excel_dll_files_not_found_in_local.append(k)
            for j in excel_sql.split("\n"):
                j = j.strip()
                tmp_sql = j.split("/")[-1]
                if tmp_sql.lower() in file_name:
                    excel_sql_files_found_in_local.append(tmp_sql.lower())
                else:
                    if tmp_sql:
                        log_info.append([self.time_tag, "excel行：", row_number, "==没找到的脚本==", tmp_sql, file_name])
                        excel_sql_files_not_found_in_local.append(tmp_sql)

        log_info.append(["excel中统计到文件数量：%s / 本地找到的文件数：%s " % ((len(set(excel_sql_files_found_in_local)) + \
                                                                    len(set(excel_dll_files_found_in_local))) , len(file_name))])
        log_info.append("****************")
        # 本地找到，excel没有
        log_info.append(["本地找到，excel中没有的文件: ", set(file_name) - set(excel_dll_files_found_in_local) - set(excel_sql_files_found_in_local)])
        log_info.append("****************")
        # excel 有，本地没有的
        log_info.append(["excel中的程序文件，在本地没找到：", set(excel_dll_files_not_found_in_local)])
        log_info.append(["excel中的脚本文件，在本地没找到：", set(excel_sql_files_not_found_in_local)])
        log_info.append("****************")
        res = {'result': False, 'excel_file_miss_in_local': [], 'local_miss_in_excel': [], 'files_time_mstake': [],
               'log_info': []}
        res['result'] = True
        res['excel_file_miss_in_local'] = list(set(excel_dll_files_not_found_in_local) | set(excel_sql_files_not_found_in_local))
        res['local_miss_in_excel'] = list(set(file_name) - set(excel_dll_files_found_in_local) - set(excel_sql_files_found_in_local))
        res['files_time_mstake'] = ''
        res['log_info'] = log_info
        # test
        return res


    def patch_check(self,path='./', excel_file=None):
        """
        功能：待验证补丁检查，通过待验证补丁文档内的内容与本地实际文件做对比
        参数：
            入参：path=补丁目录（如果没有则默认当前目录）;
                      execel_file=表格文件路径（可选）如果没有表格路径，则读取目录中的第一个 .xlsx 文件
        """
        # 如果不传 excel 文件名，则在当前目录查找
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
            local_file.extend(self.__data_format(self.get_file_list(path + k)))
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
        """
        自动整理要发布的补丁
        1、拷贝待验证补丁的文件；2、修改程序版本号、修改数据库版本号；3、根据文档标签，删除不需要的内容
        """
        if not (version and last_version):
            return False
        pack_path = r'G:\soucre\flask-echarts\jobs_Statistics_with_pyecharts\testCase\补丁版本\待验证补丁'
        # 复制文件夹，都只能是目录，且目标目录必须不存在
        version_path = os.path.join(os.getcwd(), version)
        # 如果存在有版本目录，先删除
        if os.path.exists(version_path):
            pass
            # shutil.rmtree(version_path)
        # shutil.copytree(pack_path, version_path)
        version_xml = os.path.join(version_path,"程序\\Versionconfig.xml")
        version_sql = os.path.join(version_path,"脚本\\版本脚本.sql")

        # 处理程序版本号文件
        tree = xml_ET.parse(version_xml)
        root = tree.getroot()
        sub = root.find("VersionInfo")
        for i in sub:
            if i.tag == "VersionNo":
                i.text = version + '(' + (time.strftime("%Y-%m-%d", time.localtime())) + ')'
            elif i.tag == "LastVersionNo":
                i.text = str(last_version)
            elif i.tag == "IsNeedCompareDBVersion":
                i.text = "1"
            elif i.tag == "IsShowVersionNoInText":
                i.text = "0"
        tree.write(version_xml,encoding='UTF-8', xml_declaration='yes')

        # 处理数据库版本号

        # 根据文档，删除不需要的内容


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

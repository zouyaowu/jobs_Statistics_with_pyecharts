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

from openpyxl import Workbook, load_workbook
import operator
import os
import re
import time,datetime

class public_methods(object):

    def read_excel(self,data=None, read_type='row',pack="dict"):
        """
        参数：
            data=excel文件路径，read_type=row/column按行读还是按列读，
            pack=dict/set/list 返回结果是字典还是集合（如果是集合，所有的工作簿单元格都放到一个集合中）
        功能：遍历excel文件，返回数据列表或集合（默认按行）
        返回：包含列表的字典（每个工作簿名称作为一个字典key，此字典的值是一个 包含 子列表 的 列表a，就是整个excel表格；）
             如果按行读：列表a 的每个子列表 就是 一行；
             如果按列读：列表a 的每个子列表 就是 一列；
             egg: {"sheet1":[[v1,v1-1], [v2,v2-1], [...]], "sheet2":[[...]], ...}
        备注：按列读取有BUG，取出来的数据不全，而且没有了 key
        """

        try:
            # 打开文件
            workbook = load_workbook(data)
            # 获取所有sheet，返回列表，格式：[u'sheet1', u'sheet2']
            # workbook_sheets_list = workbook.get_sheet_names()
            workbook_sheets_list = workbook.sheetnames
            wb_sheets = {}
            data_set = set()
            data_list = list()
            for sheet_name in workbook_sheets_list:
                # sheet = workbook.get_sheet_by_name(sheet_name)
                sheet = workbook[sheet_name]
                # 统计空行的数量，如果连续空一定数量行，则认为表格后面都是空的，跳过
                # 避免有些单元格设置了格式，但是没有实际数据时，会一直在遍历这些单元格
                # print(sheet.title, sheet.max_row, sheet.max_column)
                null_cnt = 0
                sheet_all_rows = []
                if read_type =='row':
                    sheet_item = sheet.rows
                else:
                    sheet_item = sheet.columns
                # 遍历工作簿所有单元格
                for colu_row in sheet_item:
                    # 遍历每行或列
                    # 遍历每个单元格
                    for cel_index in range(len(colu_row)):
                        if colu_row[cel_index].value:
                            # null_cnt = 0
                            # tmp.append(colu_row[cel_index].value)
                            # data_set.add(colu_row[cel_index].value)
                            data_list.append(colu_row[cel_index].value)
                        else:
                            # tmp.append("")
                            # data_set.add("")
                            data_list.append("")
                            # null_cnt += 1

                    # sheet_all_rows.append(tmp)
                    # 如果是字典返回，需要每行/列作为一个列表，没循环一次，要清空一次（用于记录下一列/行）
                    if pack == "dict":
                        # 每列、每行一个列表记录，注意这里是  append 方法
                        # sheet_all_rows.append(tmp)
                        sheet_all_rows.append(data_list)
                        data_list = []

                # 清除空行
                if read_type=='column':
                    child_list_len = len(sheet_all_rows[0]) # 每列有多少个元素
                    parent_list_len = len(sheet_all_rows) # 有多少列
                    # 记录空行的位置
                    empty_list = []
                    for j in range(child_list_len):
                        flag = 0
                        for k in range(parent_list_len):
                            if sheet_all_rows[k][j] != '':
                                # 非空
                                flag = 1
                                break
                        if flag == 0:
                            # 整【行】都是空的
                            empty_list.append(j)
                    # print("empty cloum: ", empty_list)
                    # 删除空行所在位置的列表元素
                    # 先倒序排列，从最后删起，否则会报错
                    empty_list.sort(reverse=True)
                    for j in sheet_all_rows:
                        for k in empty_list:
                            j.pop(k)

                # 生成字典，每个sheet一个字典节点
                wb_sheets[sheet.title] = sheet_all_rows
        except Exception as err:
            print(err)
            return None

        if pack == "dict":
            return wb_sheets
        elif pack == "set":
            return data_set
        else:
            return data_list


    def write_excel(self,data=None,file_name=None,sheet_name=None,rows=0,cl=0):
        """
        功能：把数据写入 excel
        入参：data=要写入的数据（支持 列表、元组、字符串）; file_name=要写入的文件; rows,cl 开始写的行、列
        返回值：写入成功 Ture; 写入失败 False
        """

        if not isinstance(data,list):
            # return "The data to write , not a list"
            return None
        if not file_name:
            return None
        if os.path.exists(file_name):
            wb = load_workbook(file_name)
        else:
            # 新建一个工作簿（内存中），用来存放输出结果
            wb = Workbook()
            # 新建一张表
            ws_new = wb.active
            try:
                ws_new.append(data)
            except  Exception as bug:
                ws_new.append(['we have a problme. i have a bug'])
                ws_new.append([bug])
            finally:
                try:
                    wb.save(file_name)
                except  Exception as err:
                    print('无法保存文件，或许在编辑中')
        return


    def get_week_day(self,y=1970,m=1,d=1):
        """日期转换为星期"""
        t = time.strptime("%s - %s - %s" % (y, m, d), "%Y - %m - %d")
        y, m, d = t[0:3]
        week_day_dict = {
            0:'星期一',
            1:'星期二',
            2:'星期三',
            3:'星期四',
            4:'星期五',
            5:'星期六',
            6:'星期天',
        }
        date = datetime.datetime(y, m, d)
        day = date.weekday()
        return week_day_dict[day]

    def get_balance_day(self,y=1970,m=1,d=1,y1=1970,m1=1,d1=1):
        """获取两个日期相差天数
        入参：2个日期的年、月、日
        返回：相差的天数"""
        t = datetime.datetime.strptime("%s - %s - %s" % (y, m, d), "%Y - %m - %d")
        t1 = datetime.datetime.strptime("%s - %s - %s" % (y1, m1, d1), "%Y - %m - %d")
        return (t1 - t).days

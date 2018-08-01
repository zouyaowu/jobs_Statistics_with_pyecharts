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
        返回：包含元组的字典（每个工作簿名称作为一个字典key，元组内容为一个2纬列表）
                  egg: {"key1":[[v1,v1-1], [v2,v2-1], [...]], "key2":[[...]], ...}
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
                null_cnt = 0
                sheet_all_rows = []
                if read_type =='row':
                    sheet_item = sheet.rows
                else:
                    sheet_item = sheet.columns
                # 遍历工作簿所有单元格
                for colu_row in sheet_item:
                    # 遍历每行或列
                    tmp = []
                    # 遍历每个单元格
                    for cel_index in range(len(colu_row)):
                        if colu_row[cel_index].value:
                            null_cnt = 0
                            tmp.append(colu_row[cel_index].value)
                            data_set.add(colu_row[cel_index].value)
                            data_list.append(colu_row[cel_index].value)
                        else:
                            tmp.append("")
                            data_set.add("")
                            data_list.append("")
                        # print(sheet_all_rows)
                        # for cell in colu_row:
                        null_cnt +=1
                    sheet_all_rows.append(tmp)

                    # 连续10行空
                    if null_cnt > 10:
                        break
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
        t = datetime.datetime.strptime("%s - %s - %s" % (y, m, d), "%Y - %m - %d")
        t1 = datetime.datetime.strptime("%s - %s - %s" % (y1, m1, d1), "%Y - %m - %d")
        return (t1 - t).days

# -*- coding:utf-8 -*-
import erp_i

excel_file = "testCase/补丁文档/V1.29服装待验证补丁文档20200315.xlsx"
version = "V1.29.46.001"

a = erp_i.To_be_verified()
a.excel_date_to_db(excel_file,version)
# a.create_upgrade_package(version=version, last_version="V1.29.45.001(2019-3-20)")

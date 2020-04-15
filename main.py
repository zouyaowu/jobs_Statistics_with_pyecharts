# -*- coding:utf-8 -*-
import erp_i


excel_file = r"testCase\1.1、本地有，excel中没有（脚本部分）\1.1本地有，excel中没有（脚本）.xlsx"
check_path = r"testCase\1.1、本地有，excel中没有（脚本部分）"
version = "V1.29.46.001"

a = erp_i.To_be_verified()
a.check_update_files_and_local_files(check_path, excel_file)
# a.create_upgrade_package(version=version, last_version="V1.29.45.001(2019-3-20)")

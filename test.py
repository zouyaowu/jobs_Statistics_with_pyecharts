import get_check_in_time_line
from pyecharts import Page
import os
import erp_i
import re


page = Page()
page = get_check_in_time_line.check_in_time_line()
page.render()
exit(0)
excel_path = r'./testCase/'
publ = erp_i.To_be_verified()
file_list = publ.get_file_list(excel_path)
for i in file_list:
    file_name = i.upper()
    if file_name[-5:] == '.XLSX':
        version = re.split("服装|\(",file_name)[0]
        print(excel_path + i, version)
        publ.excel_date_to_db(excel_path + i,version)

exit(0)

# -*- coding:utf-8 -*-
import erp_i
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def patch_check():
    excel_file = [r"\\192.168.100.15\品质管制部_内部文件$\客户升级版本\V1.29版本\补丁\服装版本\待验证补丁\V1.29服装待验证补丁文档 - 最新.xlsx",\
                  r"\\192.168.100.15\品质管制部_内部文件$\内部测试更新\宝胜项目\V1.42版本\待验证补丁\V1.42宝胜服装待验证补丁文档.xlsx",\
                  r"\\192.168.100.15\品质管制部_内部文件$\内部测试更新\宝胜项目\V1.43版本\待验证补丁\V1.43宝胜服装待验证补丁文档.xlsx",\
                  r"\\192.168.100.15\品质管制部_内部文件$\内部测试更新\夏普项目\V1.29版本\待验证补丁\夏普V1.29版本待验证文档 .xlsx"\
                  ]
    version = ["V1.29","BS_42","BS_43", "XP_29"]
    # version = ["V1.29", "BS_42"]
    results = []
    for i in range(len(excel_file)):
        update_list = {}
        check_list = []
        a = erp_i.To_be_verified()
        update_list['version'] = version[i]
        check_path = "\\".join(excel_file[i].split("\\")[0:-1])
        tmp = a.check_update_files_and_local_files(check_path, excel_file[i])
        if tmp['result']:
            if tmp['excel_file_miss_in_local']: check_list.append(tmp['excel_file_miss_in_local'])
            if tmp['local_miss_in_excel']: check_list.append(tmp['local_miss_in_excel'])
        update_list['check_list'] = check_list
        results.append(update_list)
    print(results)
    return render_template('patch_check.html', list_datas=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5099', debug=True)
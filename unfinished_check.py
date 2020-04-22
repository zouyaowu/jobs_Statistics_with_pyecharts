import  erp_i
from pyecharts.charts import Bar, Grid, Page, Timeline


def unfiished_excel_check_result(version=None):
    """待验证补丁结果汇总"""

    file_name = [
     r'\\192.168.100.15\品质管制部_内部文件$\客户升级版本\V1.29版本\补丁\服装版本\待验证补丁\V1.29服装待验证补丁文档 - 最新.xlsx',
     r'\\192.168.100.15\品质管制部_内部文件$\内部测试更新\V1.31版本\V1.31服装版本\待验证补丁\V1.31服装待验证补丁文档.xlsx',
     r'\\192.168.100.15\品质管制部_内部文件$\客户升级版本\卡门项目\V1.29版本\补丁\待验证补丁\KM_V1.29服装待验证补丁文档 .xlsx',
     r'\\192.168.100.15\品质管制部_内部文件$\客户升级版本\宝胜项目\V1.34版本\补丁\待验证补丁\V1.34宝胜服装待验证补丁文档.xlsx',
     r'\\192.168.100.15\品质管制部_内部文件$\内部测试更新\宝胜项目\V1.35版本\待验证补丁\V1.35宝胜服装待验证补丁文档.xlsx'
    ]
    """
    file_name = [
     r'\\192.168.100.15\品质管制部_内部文件$\客户升级版本\V1.29版本\补丁\服装版本\待验证补丁\V1.29服装待验证补丁文档.xlsx',\
     r'\\192.168.100.15\品质管制部_内部文件$\客户升级版本\卡门项目\V1.29版本\补丁\待验证补丁\KM_V1.29服装待验证补丁文档 .xlsx',\
     r'\\192.168.100.15\品质管制部_内部文件$\客户升级版本\宝胜项目\V1.32版本\补丁\待验证补丁\V1.32宝胜服装待验证补丁文档  .xlsx',\
     r'\\192.168.100.15\品质管制部_内部文件$\客户升级版本\宝胜项目\V1.33版本\补丁\待验证补丁\V1.33宝胜服装待验证补丁文档.xlsx'
    ]
    """
    page = Page()
    tl = unfiished_check_result(file_name, version)
    if tl:
        page.add(tl)
    return page


def jobs_test_result_per(file_name=None):
    """对每人签入做一个记录，统计一段时间内容的测试进度"""
    if not file_name:
        # return None
        file_name = r'\\192.168.100.15\品质管制部_内部文件$\客户升级版本\宝胜项目\V1.33版本\补丁\待验证补丁\V1.33宝胜服装待验证补丁文档.xlsx'
    check = erp_i.To_be_verified()
    tmp_dict = {}
    timeline = Timeline(is_auto_play=True, timeline_bottom=2, page_title="待验证补丁", width="90%", is_timeline_show=True,
                        timeline_play_interval=5000)
    check.specify_data_list(file_name)


def unfiished_check_result(file_name=None, version=None):
    """检查待验证补丁的结果填写情况"""
    # 待验证补丁中未完成的测试
    if not file_name:
        return None
    check = erp_i.To_be_verified()
    tmp_dict = {}
    timeline = Timeline(is_auto_play=True, timeline_bottom=2, page_title="待验证补丁", width="90%", is_timeline_show=True, timeline_play_interval=5000)
    # 时间轮播报表需要每个图形的X轴是等长，否则以最短的那个图为基准显示
    attr_modul = ['进销存', '电商', '商场', '会员', '仓储', '人力', '生产', '会员服务', '公共财务', '公共', '报表平台', '货品管理APP', '人事web', '羽绒',  'HKWEB平台']
    for file in file_name:
        tmp_dict = check.unfinished_test(file)
        if not version:
            tmp = file.split('\\')[-1]
            version = tmp.split('服装')[0]
        if not tmp_dict:
            print(version + "read excel err")
            continue
        attr = []
        done_v = []
        undone_v = []
        for key in attr_modul:
            try:
                attr.append(key)
                undone_v.append(tmp_dict[key]['undone'])
                done_v.append(tmp_dict[key]['done'])
            except:
                undone_v.append(0)
                done_v.append(0)
        bar = Bar(version + "待验证补丁测试情况", width="100%")
        # bar.add("已测试", attr, done_v, is_label_show=True, label_pos='inside', is_stack=True, xaxis_interval=0)
        bar.add("待测试", attr, undone_v, is_label_show=True, label_pos='inside', is_stack=True, xaxis_interval=0)
        timeline.add(bar, version)
        version = None
    return timeline


def unfiished_check_result_file(file_name=None):
    """检查待验证补丁的结果填写情况"""
    # 待验证补丁中未完成的测试
    if not file_name:
        return None
    check = erp_i.To_be_verified()
    tmp_dict = {}
    timeline = Timeline(is_auto_play=True, timeline_bottom=2, page_title="待验证补丁", width="90%", is_timeline_show=True, timeline_play_interval=5000)
    # 时间轮播报表需要每个图形的X轴是等长，否则以最短的那个图为基准显示
    attr_modul = ['进销存', '电商', '商场', '会员', '仓储', '人力', '生产', '会员服务', '公共财务', '公共', '报表平台', '货品管理APP', '人事web', '羽绒',  'HKWEB平台']
    for file in file_name:
        tmp_dict = check.unfinished_test(file)
        tmp = file.split('\\')[-1]
        version = tmp.split('服装')[0]
        if not tmp_dict:
            print(version + "read excel err")
            continue
        attr = []
        done_v = []
        undone_v = []
        for key in attr_modul:
            try:
                attr.append(key)
                undone_v.append(tmp_dict[key]['undone'])
                done_v.append(tmp_dict[key]['done'])
            except:
                undone_v.append(0)
                done_v.append(0)
        bar = Bar(version + "待验证补丁测试情况", width="100%")
        # bar.add("已测试", attr, done_v, is_label_show=True, label_pos='inside', is_stack=True, xaxis_interval=0)
        bar.add("待测试", attr, undone_v, is_label_show=True, label_pos='inside', is_stack=True, xaxis_interval=0)
        timeline.add(bar, version)
    return timeline
    # timeline.render()
    # page.render("page.html")

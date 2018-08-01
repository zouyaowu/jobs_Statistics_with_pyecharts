import erp_i
import sqlite3
import re
from pyecharts import Line,Page,Grid


def __week_data_line(data1=None,data2=None,paging=True,title=None):
    """
    :param data1: 第一组数据（字典类型，数据项:数值,[数值1,数值2,...]）
    :param data2:  第二组数据（字典类型，数据项:数值,[数值1,数值2,...]）
    :param paging: 是否并列显示2个图形（默认是）
    :param Summary: 有多个数据项时，是否汇总，还是每个数据项一条线
    :param title: 数据标题
    :return: grid图形数据
    """
    grid = Grid(width="100%")
    attr = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]
    line1 = Line(str(title))
    line2 = Line()
    # 遍历每个 data 下面的值，分别统计每个星期日期的个数（如：星期一3个，星期二2个）
    if paging:
        for key in data1:
            tmp_list = []
            for t in attr:
                tmp_list.append(data1[key].count(t))
            data1[key] = tmp_list
            line1.add(key, attr, data1[key], is_label_show=False, is_legend_show=False, legend_pos="70%" )
        grid.add(line1, grid_left="60%")
        if data2:
            for key in data2:
                tmp_list = []
                for t in attr:
                    tmp_list.append(data2[key].count(t))
                data2[key] = tmp_list
                line2.add(key, attr, data2[key], is_label_show=False, is_legend_show=False, legend_pos="70%" )
            grid.add(line2, grid_right="60%")
    else:
        for key in data1:
            tmp_list = []
            for t in attr:
                tmp_list.append(data1[key].count(t))
            data1[key] = tmp_list
            line1.add(key, attr, data1[key], is_label_show=True, is_legend_show=True)
        if data2:
            for key in data2:
                tmp_list = []
                for t in attr:
                    tmp_list.append(data2[key].count(t))
                data2[key] = tmp_list
                line1.add(key, attr, data2[key], is_label_show=True, is_legend_show=True)
        grid.add(line1, grid_left="5%", grid_width="60%")
    return grid


def total_check_in_time_line(db=None,table=None):
    erp = erp_i.To_be_verified()
    con = sqlite3.connect('test.db3')
    cur = con.cursor()
    page=Page("签入时间曲线")
    # print(version[0])
    timeset = set()
    cur.execute('select date_commit, date_test from check_in_datas')
    test_weeks = []
    dev_weeks = []
    weeks_data = {}
    for w,ws in cur.fetchall():
        # 日期存入数据库的格式为 2018-07-29 00:00:00
        # 去掉时间部分
        try:
            w = w.split(' ')[0]
            # 从数据库取回的值可能为空或不是字日期字符串
            y,m,d = re.split("-|/|\*|\.",w)
            dev_weeks.append(erp.get_week_day(y, m, d))
        except Exception as values_err:
            print('开发提交日期，非法日期:', w)

        try:
            ws = ws.split(' ')[0]
            # 从数据库取回的值可能为空或不是字日期字符串
            y1,m1,d1 = re.split("-|/|\*|\.",ws)
            test_weeks.append(erp.get_week_day(y1, m1, d1))
        except Exception as values_err:
            print('测试验证日期，非法日期:', ws)
            continue
    weeks_data["开发提交时间"] = dev_weeks
    weeks_data["测试验证时间"] = test_weeks
    page.add(__week_data_line(weeks_data, paging=False))
    cur.close()
    con.close()
    return page


def evreyone_check_in_time_line(db=None,table=None,paging=True):
    """
    通过读取数据库中的记录，整理出开发人员签入待测试文档的时间，测试人员验证签入的时间，形成时间线。
    参数：db 数据库名称，table 表名称， paging 是否按版本分开显示，默认分开显示
    """
    erp = erp_i.To_be_verified()
    con = sqlite3.connect('test.db3')
    cur = con.cursor()
    cur.execute('select erp_version from check_in_datas Group BY erp_version')
    page=Page("签入时间曲线")
    for version in cur.fetchall():
        # print(version[0])
        cur.execute('select author,tester from check_in_datas where erp_version like ?', (version[0],))
        tester = set()
        author = set()
        for j,k in cur.fetchall():
            author.add(j)
            tester.add(k)
        author_week = {}
        for a in author:
            cur.execute('select date_commit from check_in_datas where author=? and erp_version like ?', (a, version[0],))
            weeks = []
            for w in cur.fetchall():
                # 日期存入数据库的格式为 2018-07-29 00:00:00
                # 去掉时间部分
                w = w[0].split(' ')[0]
                # 从数据库取回的值可能为空或不是字日期字符串
                try:
                    y,m,d = re.split("-|/|\*|\.",w)
                    weeks.append(erp.get_week_day(y, m, d))
                except Exception as values_err:
                    # print('非法日期:', w)
                    continue
            if a:
                author_week[a] = weeks
        tester_week = {}
        for t in tester:
            cur.execute('select date_test from check_in_datas where tester=? and erp_version like ?', (t, version[0],))
            weeks = []
            for w in cur.fetchall():
                # 日期存入数据库的格式为 2018-07-29 00:00:00
                # 去掉时间部分
                w = w[0].split(' ')[0]
                # 从数据库取回的值可能为空或不是字日期字符串
                try:
                    y,m,d = re.split("-|/|\*|\.",w)
                    weeks.append(erp.get_week_day(y, m, d))
                except Exception as values_err:
                    # print('测试人员提交日期，含非法日期格式:', w)
                    continue
            if t:
                tester_week[t] = weeks
        # print(author_week)
        # print(tester_week)

        page.add(__week_data_line(author_week,tester_week,title=str(version[0])))
        """
        grid = Grid(width="100%")
        attr = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]
        line_authoer = Line(str(version[0]) + "开发签入\测试验证 所属星期x曲线图")
        # 遍历每个 author_week 下面的值，分别统计每个星期日期的个数（如：星期一3个，星期二2个）
        for v in author_week:
            tmp_list = []
            for t in attr:
                tmp_list.append(author_week[v].count(t))
            author_week[v] = tmp_list
            line_authoer.add(v, attr, author_week[v], is_label_show=False, is_legend_show=False, legend_pos="70%")
        grid.add(line_authoer,grid_left="60%")

        line_tester = Line("")
        for v in tester_week:
            tmp_list = []
            for t in attr:
                tmp_list.append(tester_week[v].count(t))
            tester_week[v] = tmp_list
            line_tester.add(v, attr, tester_week[v],  is_label_show=False, is_legend_show=False, legend_pos="20%")
        grid.add(line_tester,grid_right="60%")
        page.add(grid)
        """
    cur.close()
    con.close()
    return page
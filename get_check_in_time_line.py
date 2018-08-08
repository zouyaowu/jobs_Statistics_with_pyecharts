import erp_i
import sqlite3
import re
import time,datetime
from pyecharts import Line,Page,Grid,Scatter,Pie


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
    if paging:
        # 遍历每个 data 下面的值，分别统计每个星期日期的个数（如：星期一3个，星期二2个）
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


def total_check_in_time_line(con=None,cur=None,table=None):
    erp = erp_i.To_be_verified()
    page=Page("签入时间曲线")
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
    return page


def evreyone_check_in_time_line(con=None,cur=None,table=None,paging=True):
    """
    通过读取数据库中的记录，整理出开发人员签入待测试文档的时间，测试人员验证签入的时间，形成时间线。
    参数：db 数据库名称，table 表名称， paging 是否按版本分开显示，默认分开显示
    """
    erp = erp_i.To_be_verified()
    cur.execute('select erp_version from check_in_datas Group BY erp_version')
    page=Page("签入时间曲线")
    for version in cur.fetchall():
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

        page.add(__week_data_line(author_week,tester_week,title=str(version[0])))
    return page


def each_workload(con=None,cur=None,table=None,paging=True):
    """
    通过读取数据库中的记录，每人每周的工作量
    参数：db 数据库名称，table 表名称， paging 用户多的时候是否拆成多个图表来显示
    """
    erp = erp_i.To_be_verified()
    cur.execute('select tester from check_in_datas group by tester')
    page=Page("工作量")
    line = Line()
    attr = []
    v = []
    for tester in cur.fetchall():
        cur.execute('select date_test from check_in_datas where tester like ?', (tester[0],))
        for w in cur.fetchall():
            # 日期存入数据库的格式为 2018-07-29 00:00:00
            # 去掉时间部分
            w = w[0].split(' ')[0]
        # 从数据库取回的值可能为空或不是字日期字符串
        try:
            y, m, d = re.split("-|/|\*|\.", w)
            # 第几周
            ww = datetime.date(int(y), int(m), int(d)).isocalendar()[1]
            if ww in attr:
                tmp = attr.index(ww)
                v[tmp] += 1
            else:
                attr.append(ww)
                v.append(1)
        except Exception as values_err:
            print(values_err)
            # print('非法日期:', w)
            continue
    print(attr,v)

"""

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

        page.add(__week_data_line(author_week,tester_week,title=str(version[0])))
    return page
"""

def times_between_pack_finished(con=None,cur=None,table=None):
    """
    :param con:
    :param cur:
    :param table:
    :return:
    """
    erp = erp_i.To_be_verified()
    page = Page("签入时间曲线")
    cur.execute('select date_pack, date_test from check_in_datas')
    diff_time = []
    for pack, test in cur.fetchall():
        if not pack:
            continue

        if not test:
            test = time.strftime('%Y-%m-%d',time.localtime())

        try:
            t = pack.split(" ")[0]
            y, m, d = re.split("-|/|\*|\.", t)
            v = test.split(" ")[0]
            y1, m1, d1 = re.split("-|/|\*|\.", v)
            diff = erp.get_balance_day(y, m, d, y1, m1, d1)
            if diff >= 0:
                diff_time.append(diff)
            else:
                # print('maybe err:',test,'-',pack)
                pass
        except Exception as err:
            pass
            # print(err)
            # print("非法日期:",pack,test)

    attr = ['当天', '隔天', '3天', '7天', '15天', '30天', '30天以上']
    attr_cnt = [[0,0], [1,0], [3,0], [7,0], [15,0], [30,0]]
    tmp = [0, 0, 0, 0, 0, 0, 0]
    for i in diff_time:
        if i == 0:
            tmp[0] += 1
        elif i == 1:
            tmp[1] += 1
        elif i > 1 and (i <= 3):
            tmp[2] += 1
        elif (i > 3) and (i <= 7):
            tmp[3] += 1
        elif i > 7 and (i <= 15):
            tmp[4] += 1
        elif i > 15 and (i <= 30):
            tmp[5] += 1
        else:
            tmp[6] += 1

    print(tmp)
    pie = Pie()
    pie.add("", attr, tmp, is_label_show=True)
    # scatter = Scatter("打包到验证完成时间的时间间隔")
    # scatter.add("",diff_time,diff_time)
    return page.add(pie)


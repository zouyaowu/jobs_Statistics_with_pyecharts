import erp_i
import sqlite3
import re
from pyecharts import Line,Page,Grid


def check_in_time_line(db=None,table=None,paging=True):
    """
    通过读取数据库中的记录，整理出开发人员签入待测试文档的时间，测试人员验证签入的时间，形成时间线。
    参数：db 数据库名称，table 表名称， paging 是否按版本分开显示，默认分开显示
    """
    erp = erp_i.To_be_verified()
    con = sqlite3.connect('test.db3')
    cur = con.cursor()
    cur.execute('select erp_version from check_in_datas Group BY erp_version')
    page=Page("签入时间曲线")
    for verion in cur.fetchall():
        cur.execute('select author,tester from check_in_datas')
        tester = set()
        author = set()
        for j,k in cur.fetchall():
            author.add(j)
            tester.add(k)
        author_week = {}
        for a in author:
            cur.execute('select date_commit from check_in_datas where author=?', (a,))
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
            cur.execute('select date_test from check_in_datas where tester=?', (t,))
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

        grid = Grid(width="100%")
        attr = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]
        line_authoer = Line(str(verion) + "开发签入\测试验证 所属星期x曲线图")
        # 遍历每个 author_week 下面的值，分别统计每个星期日期的个数（如：星期一3个，星期二2个）
        for v in author_week:
            tmp_list = []
            for t in attr:
                tmp_list.append(author_week[v].count(t))
            author_week[v] = tmp_list
            line_authoer.add(v, attr, author_week[v], is_stack=True, is_label_show=False, is_legend_show=False, legend_pos="70%")
        grid.add(line_authoer,grid_left="60%")

        line_tester = Line("")
        for v in tester_week:
            tmp_list = []
            for t in attr:
                tmp_list.append(tester_week[v].count(t))
            tester_week[v] = tmp_list
            line_tester.add(v, attr, tester_week[v], is_stack=True, is_label_show=False, is_legend_show=False, legend_pos="20%")
        grid.add(line_tester,grid_right="60%")
    page.add(grid)
    return page
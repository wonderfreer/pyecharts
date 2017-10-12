#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import HeatMap
from test.constants import X_TIME, Y_WEEK


def test_heatmap():
    import random
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap("热力图示例")
    heatmap.add("热力图直角坐标系", X_TIME, Y_WEEK, data, is_visualmap=True,
                visual_text_color="#000", visual_orient='horizontal',
                xaxis_name='XNAME', yaxis_name='YNAME',
                yaxis_name_pos='end', yaxis_name_gap=5)
    heatmap.render()


def test_heatmap_date():
    import random
    import datetime
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)),
            random.randint(0, 100)] for i in range((end - begin).days + 1)]
    heatmap = HeatMap("日历热力图示例")
    heatmap.add("日历热力图", data,
                is_visualmap=True, is_legend_show=False,
                is_date_heatmap=True, date_range="2017",
                visual_orient="horizontal", visual_pos="center",
                visual_top="top")
    heatmap.render()

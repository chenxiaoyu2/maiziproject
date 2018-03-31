# -*- coding:utf-8 -*-
from django import template
import  datetime
import pytz
register = template.Library()

# 计算时间差
@register.filter(name="cdate")
def time_before(time):
    time_list=[
        (60*60*24*365,u'年'),
        (60*60*24*30,u'月'),
        (60*60*24*7,u'周'),
        (60*60*24,u'天'),
        (60*60,u'小时'),
        (60,u'分钟'),
        (1,u'秒'),
    ]
    if not isinstance(time,datetime.datetime):
        time=datetime.datetime(time.year,time.month,time.day)
    now=datetime.datetime.now()
    before_time=now-time
    print(before_time)
    before=before_time.days*60*60*24+before_time.seconds
    if before<=60:
        return u'刚刚'
    for seconds,unit in time_list:
        count = before//seconds
        if count != 0:
            break
    return str(count)+str(unit)+u'前发布'

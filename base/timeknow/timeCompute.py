# coding: utf-8
import re
import datetime
from datetime import datetime


def calc_hours(old, new):
    # 计算两个datetime格式时间的小时差
    """
    :param old:datetime.比较旧的时间
    :param new:datetime.比较新的时间
    :return: hours.两个时间的差值，单位:小时.若时间反了，可能出现负数.
    """
    old = str(old)
    if '+' in old:
        old = old.split('+')[0]
    new = str(new)
    if '+' in new:
        new = new.split('+')[0]
    # 取datetime格式数据中的年月日小时分秒部分
    old = old.split('.')[0]
    new = new.split('.')[0]
    old_time = datetime.datetime.strptime(old, "%Y-%m-%d %H:%M:%S")
    new_time = datetime.datetime.strptime(new, "%Y-%m-%d %H:%M:%S")
    # print('newtime:', new_time.day, new_time.hour, new_time.minute, new_time.second)
    days = (new_time - old_time).days  # 日
    sec = (new_time - old_time).seconds  # 秒
    hours = days * 24 + round(sec / 3600, 3)  # 小时
    # print('days:', days, 'hours:', hours, 'second:', sec)
    return hours


def hoursToDHM(hours):
    # 小时转换成天、小时、分钟
    """
    :param hours:float.用时.单位：小时
    :return: days.小时中的天数
             hours.小时中的小时
             minutes.小时中的分钟
    """
    time1 = datetime.timedelta(hours=hours)
    days = time1.days
    seconds = time1.seconds
    time2 = datetime.timedelta(seconds=seconds)
    hours = str(time2).split(':')[0]
    minutes = str(time2).split(':')[1]
    return days, hours, minutes


def cuoAndDatetimeEachChange(src_t):
    # 时间戳转datetime
    if type(src_t) == int:
        goal_t = datetime.fromtimestamp(src_t)
    # datetiem转时间戳
    else:
        goal_t = int(src_t.timestamp())
    return goal_t


def datetimeAndStrEachChange(src_t):
    # 字符串/datetime格式时间相互转换
    # datetime转str
    if type(src_t) == (type(datetime.now())):
        try:
            goal_t = src_t.strftime('%Y-%m-%d %H:%M:%S')
        except:
            goal_t = src_t.strftime("%d/%b/%Y:%H:%M:%S")
    # str转datetime
    elif type(src_t) == str:
        if '/' in src_t:
            goal_t = datetime.strptime(src_t, '%Y/%m/%d')
        elif ':' in src_t:
            goal_t = datetime.strptime(src_t, '%Y-%m-%d %H:%M:%S')
        elif len(re.findall('^(\d{6})$', src_t)) == 0:
            goal_t = datetime.strptime(src_t, '%Y%m%d')
        else:
            goal_t = datetime.strptime(src_t, '%Y/%m/%d')
    else:
        return src_t
    return goal_t


if __name__ == '__main__':
    s = '20220515'
    t = datetimeAndStrEachChange(s)
    print(t)

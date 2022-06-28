# coding: utf-8
import time
import datetime

"""
时间戳(float)，例如：1656358846.753544。它的左边代表左侧是自1970年1月1日00:00:00以来的秒数。右边因为秒数可以是非整数，可以用毫秒理解。
time.localtime(sec) sec为时间戳，可以不输入sec参数，这样默认以当前时间作为输入，返回一个结构化时间
"""

cuoNow = time.time()  # 获取当前时间的时间戳
date = datetime.datetime.now()  # 读取系统本地时间
dateGlobe = datetime.datetime.utcnow()  # 读取系统的世界标准时间，不随系统默认时区变化
st = str(date).split('.')[0]  # datetime.datetime时间转为str并去除后面的小数点
# ————————————————————————————————————————————————————————————————————————————
# 字符串转为结构化时间，t1:time.struct_time
t1 = time.strptime(st, '%Y-%m-%d %H:%M:%S')
print('字符串转为结构化时间')
print('src:', st, type(st))
print('res:', t1, type(t1))
print('-' * 10)
# 结构化时间转为时间戳，t2:float
t2 = time.mktime(t1)
print('结构化时间转为时间戳')
print('src:', t1, type(t1))
print('res:', t2, type(t2))
print('-' * 10)
# 时间戳转为结构化时间
t3 = time.localtime(t2)
print('时间戳转为结构化时间')
print('src:', t2, type(t2))
print('res:', t3, type(t3))
print('-' * 10)
# 结构化时间转str时间格式，t3:str(例:2022-06-28 11:21:58)
t4 = time.strftime('%Y-%m-%d %H:%M:%S', t1)
print('结构化时间转datetime')
print('src:', t1, type(t1))
print('res:', t4, type(t4))
print('-' * 10)
# 时间格式(str)转datetime.datetime格式
t5 = datetime.datetime.strptime(t4, '%Y-%m-%d %H:%M:%S')
print('str时间格式转datetime.datetime格式')
print('src:', t4, type(t4))
print('res:', t5, type(t5))
print('-' * 10)
# 时间格式(datetime.datetime)转为字符串(str)
t6 = date.strftime("%Y-%m-%d %H:%M:%S")
print('时间格式(datetime.datetime)转为字符串(str)')
print('src:', date, type(date))
print('res:', t6, type(t6))
print('-' * 10)
# 时间格式(datetime.datetime)转为时间戳(float)
# 第一种方法datetime->str->struct_time->float不带毫秒
srctime = datetime.datetime.utcnow()
tpstr = srctime.strftime("%Y-%m-%d %H:%M:%S")  # str类型的时间
tm = time.strptime(tpstr, '%Y-%m-%d %H:%M:%S')  # 转为时间结构体
timeStamp = time.mktime(tm)  # 转为时间戳
print('时间格式(datetime.datetime)转为时间戳(float)')
print('first')
print('src:', srctime, type(srctime))
print('res:', timeStamp, type(timeStamp))
# 第二种方法datetime.datetime->float带毫秒
print('second')
print(srctime.timestamp(), type(srctime.timestamp()))
print('-' * 10)
# 结构化时间转换为带月日的str时间，无参默认以time.localtime()为参数
t7 = time.asctime(t3)
print('结构化时间转换为带月日的str时间')
print('src:', t3, type(t3))
print('res:', t7, type(t7))
print('-' * 10)
# 时间戳转换为带月日的str时间，无参默认以time.time()为参数
t8 = time.ctime(cuoNow)
print('结构化时间转换为带月日的str时间')
print('src:', cuoNow, type(cuoNow))
print('res:', t8, type(t8))
print('-' * 10)
# 时间戳整数转datetime.datetime
cuoNowInt = int(cuoNow)
t9 = datetime.datetime.fromtimestamp(cuoNowInt)
print('时间戳整数转datetime.datetime')
print('src:', cuoNowInt, type(cuoNowInt))
print('res:', t9, type(t9))
print('-' * 10)
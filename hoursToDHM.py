# coding: utf-8
import datetime


# thistime = datetime.datetime.now()
# print(thistime)
# print(thistime.weekday() + 1)
# print(type(thistime.weekday() + 1))
def hoursToDHM(hours):
    time1 = datetime.timedelta(hours=hours)
    days = time1.days
    seconds = time1.seconds
    time2 = datetime.timedelta(seconds=seconds)
    hours = str(time2).split(':')[0]
    minutes = str(time2).split(':')[1]
    print(time1)
    print('days:' + str(days), 'hours:' + hours, 'minutes:' + minutes)
    return days, hours, minutes


print('\u2011')

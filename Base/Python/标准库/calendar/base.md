# 日历模块，使用它可以直接生成某月的日历
import calendar
cal = calendar.month(2015, 1)
print(cal)

# calendar.calendar(year,w=2,l=1,c=6)
返回year年年历，3个月一行，间隔距离为c。每日宽度间隔为w字符。每行长度为21w+18+2c。l是每星期行数。
例：
cal = calendar.calendar(2015)
print(cal)

# isleap(year)
判断是否为闰年，是则返回true，否则false.
calendar.isleap(2000)

# leapdays(y1,y2)
返回在Y1，Y2两年之间的闰年总数，包括y1，但不包括y2
calendar.leapdays(2000,2004)

# month(year,month,w=2,l=1)
返回year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
print(calendar.month(2015, 5))

# monthcalendar(year,month)
返回一个列表，列表内的元素还是列表，这叫做嵌套列表。每个子列表代表一个星期，都是从星期一到星期日，如果没有本月的日期，则为0。

# monthrange(year,month)
返回一个元组，里面有两个整数。第一个整数代表着该月的第一天从星期几是（从0开始，依次为星期一、星期二，直到6代表星期日）。第二个整数是该月一共多少天。
calendar.monthrange(2015, 5)
(4, 31)

# weekday(year,month,day)
输入年月日，知道该日是星期几（注意，返回值依然按照从0到6依次对应星期一到星期六）。


from datetime import datetime, timedelta


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # 判断闰年还是平年
        def checkRN(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        if date1 > date2:
            date1, date2 = date2, date1
        date1 = date1.split("-")
        date2 = date2.split("-")
        y1, m1, d1 = int(date1[0]), int(date1[1]), int(date1[2])
        y2, m2, d2 = int(date2[0]), int(date2[1]), int(date2[2])
        # 判断是闰年还是平年
        flag1 = 0
        if checkRN(y1):
            flag1 = 1
        flag2 = 0
        if checkRN(y2):
            flag2 = 1
        res = 0
        # 计算年
        for i in range(y1, y2):
            # 判断是闰年还是平年
            if checkRN(i):
                res += 366
            else:
                res += 365
        # 计算开始日期是当年的第几天
        start = d1
        for i in range(1, m1):
            if i in {1, 3, 5, 7, 8, 10, 12}:
                start += 31
            elif i == 2:
                # 判断是闰年还是平年
                if flag1:
                    start += 29
                else:
                    start += 28
            else:
                start += 30

        # 计算结束日期是当年的第几天
        end = d2
        for i in range(1, m2):
            if i in {1, 3, 5, 7, 8, 10, 12}:
                end += 31
            elif i == 2:
                # 判断是闰年还是平年
                if flag2:
                    end += 29
                else:
                    end += 28
            else:
                end += 30

        return res + end - start


def countday(data1, data2):
    pass


# d1 = str(input("日期1："))
# d2 = str(input("日期2："))
d1 = "20200101"
d2 = "20210306"
y1, y2 = int(d1[0:4]), int(d2[0:4])
month1, month2 = int(d1[5:6]), int(d2[5:6])
day1, day2 = int(d1[7:8]), int(d2[7:8])

outday = 0
outday += abs(y1 - y2) * 365 + abs(month1 - month2) * 30 + abs(day1 - day2)
print(outday)

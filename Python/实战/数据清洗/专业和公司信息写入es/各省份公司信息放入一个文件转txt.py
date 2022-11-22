# coding: utf-8

import os
import xlrd
import csv
path = "./data/company/"
filelst = os.listdir(path)
print(filelst)
alldata = []
for i, file in enumerate(filelst):
    print(file)
    wb = xlrd.open_workbook(path + file)
    # 按工作簿定位工作表
    sh = wb.sheet_by_name("details")
    for i in range(sh.nrows):
        if i == 0:
            continue
        data = sh.row_values(i)
        del data[23]
        data = "\t".join(data)
        alldata.append(data)
    wb.release_resources()

with open("./allcompany.txt", "w", encoding="utf8", newline="") as f:
    for d in alldata:
        f.write(d + "\n")

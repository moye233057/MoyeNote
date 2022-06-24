import pandas as pd
import xlrd

# xlsx文件路径
xlsxpath = '../data/企业名录.xlsx'
xlspath = '../data/company_name.xls'
# 工作表的名字
xlsxsheetname = 'Sheet2'
xlssheetname = "高新技术企业"
# 利用xlrd库打开xlsx后缀的excel表格
wb = xlrd.open_workbook(xlsxpath)
# #按工作簿定位工作表
sh = wb.sheet_by_name(xlsxsheetname)

# print(sh.nrows)#有效数据行数
# print(sh.ncols)#有效数据列数
#
# # 取第一列的值，即序号
# serialnum = sh.col_values(0)
# print(serialnum)
# print(sh.cell(0,1).value)#输出第一行第一列的值
# print(sh.row_values(0))#输出第一行的所有值
# #将数据和标题组合成字典
# #取第一行为键，第二行为值，一一对应
# print(dict(zip(sh.row_values(0),sh.row_values(1))))
# #遍历excel，打印所有数据
# for i in range(sh.nrows):
#     print(sh.row_values(i))


# 读取xlsx后缀的excel文档，将它清洗转换为csv
# #日期格式转换成整数类型
# def to_integer(dt_time):
#     return 10000*dt_time.year + 100*dt_time.month + dt_time.day

#读取excel中对应的列
# df1 = pd.read_excel(xlsxpath,sheet_name=xlsxsheetname,usecols=[1,5,7,10,11,12,14,])
# data = df1.values.tolist()
# #读取第一行
# df2 = pd.read_excel(xlsxpath,sheet_name=xlsxsheetname,nrows=1)
# data = df2.values
# print(data)
# print(type(data))

# 对源公司名录的时间列进行格式转变
# infor = []
title = ['公司名','所属行业','成立日','类型','注册资本','登记地','经营范围']
# # infor.append(title)
# for row in data :
#     # infor.append(row)
#     # print(type(row[3]))
#     if row[2] is None :
#         row[2] = 0
#         infor.append(row)
#     elif type(row[2]) is  time:
#         row[2] = 0
#         infor.append(row)
#     else:
#         row[2] = to_integer(row[2])
#         # print(type(row))
#         infor.append(row)
# print(infor)
# test=pd.DataFrame(columns=title,data=infor)
# print(test)
# test.to_csv(outpath,encoding='utf-8')
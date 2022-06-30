# -*-encoding:utf-8-*-

import pandas as pd
import numpy as np

# pandas有两种数据结构
# 第一种是Series.表示一维标记数组
# 第二种是DataFrame数据框.表示二维数据结构

# mySeries = pd.Series([3,-5,7,4], index=['a','b','c','d'])
# # print(mySeries)
# print(type(mySeries))#Series格式
#
# data = {'Country' : ['Belgium', 'India', 'Brazil' ],
#         'Capital': ['Brussels', 'New Delhi', 'Brassilia'],
#         'Population': [1234,1234,1234]}
# datas = pd.DataFrame(data, columns=['Country','Capital','Population'])
# print(type(data))#字典格式
# # print(datas)
# print(type(datas))#DataFrame格式


# # 读取数据
# # 读取csv
# df = pd.read_csv('./data/policy.csv')
# type(df)#DataFrame格式
# pd.read_excel('filename')
# pd.read_sql(query,connection_object)
# pd.read_table(filename)
# pd.read_json(json_string)
# pd.read_html(url)
# pd.read_clipboard()

# # 数据存储
# df.to_csv(filename)
# df.to_excel(filename)
# df.to_sql(table_name, connection_object)
# df.to_json(filename)
# df.to_html(filename)
# df.to_clipboard()

df = pd.DataFrame(np.random.rand(20, 5))
print(df.info())
# RangeIndex:指定有多少数据。
# Data Columns:指定找到多少列。
# Columns:提供关于Columns的信息。
# dtypes:它说你有什么类型的数据，你有多少这些数据。
# Memory Usage:表示内存使用量。

# 显示了行数和列数
df.shape()
# 找到的索引总数
df.index()
# 数据框的所有列
df.columns
# 每一行有多少数据
df.count()
# 每一列中的求和
df.sum()
# 每一列最大值
df.max()
# 每一列最小值
df.min()
# cum系列函数是作为DataFrame或Series对象的方法出现的，因此命令格式为D.cumsum()
# cumsum() 依次给出前n项的和
# cummax() 依次给出前n项的最大值
# cummin() 依次给出前n项的最小值
# cumprod() 依次给出前n项的积

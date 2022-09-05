# f.read()读取的是整个文本，类型是str
# f.readline()读取文本第一行，类型是str
# f.readlines()读取所有文本，类型是list
# split()后的是列表
import csv
import re

import pandas as pd


def cleanzltxt(srcpath, outpath):
    l = [['公开号', '专利名称', '申请人', '发明人', '申请号', '公开日', '申请日', '摘要', '专利类型', '国省代码', '分类号', '法律状态', '地址']]

    with open(srcpath, 'r', encoding='utf-8') as f:
        # text = f.readlines()
        # print(text)
        # print(type(text))
        line = f.readline()
        # print(line)
        # print(type(line))
        # readline读取的每行代表每个专利的数据，是str格式，可以用split函数分割一条专利的各个信息
        # 分割后的数据是一个列表，将这个列表当成另一个列表的一个数据，用append函数逐个连接
        while line:
            li = line.split('==')
            # print(li)
            l.append(li)
            line = f.readline()
    f.close()
    # newline=''能够解决生成的CSV数据每行之间有空行的问题
    with open(outpath, 'w', encoding='utf-8', newline='') as csvf:
        writer = csv.writer(csvf)
        # 列表l每个列表数据逐个写入
        for row in l:
            # print(row)
            writer.writerow(row)
    csvf.close()


def cleanzlcsv(srcpath, outpath):
    csvd = pd.read_csv(srcpath, low_memory=False)  # 防止弹出警告
    data = pd.DataFrame(csvd)
    data['专利类型'] = data['专利类型'].apply(lambda x: x.replace('###', '').replace('$$$', ''))
    data['摘要'] = data['摘要'].apply(lambda x: re.sub('\<.*?\>', '', x))
    # print(data['摘要'])
    # for row in data.head():
    #     print(row)
    data.to_csv(outpath, header=True, index=True)


if __name__ == "__mian__":
    txtsrcpath = "./data/zhiwang_fin2016_bu.txt"
    txtoutpath = "./data/zhiwang_fin2016_bu.csv"
    csvsrcpath = ""
    csvoutpath = ""

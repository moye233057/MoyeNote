# coding: utf-8
import json
import re

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


def insertNumAndSort(arr, x):
    t = 0
    for i in range(len(arr)):
        if x < arr[i]:
            t = i
            break  # 循环结束时，i=5
    for j in range(len(arr) - 1, t, -1):  # 数从后面依次后移直到遇到a[t]
        arr[j] = arr[j - 1]
    arr[t] = x
    return arr


es = Elasticsearch('192.168.1.11:9200')
#  ------输入的专业------
text = "汉语言文学"
#  --------------------

# 在专业表索引professional中按专业查找，获取对应的大类
s1 = Search(using=es, index='professional')
s1 = s1.query("multi_match", query=text, fields=['categories'])
res1 = s1.execute()
cats = []
for indexid, hit in enumerate(res1):
    pro_name = hit.pro_name.replace("学", "")
    if pro_name not in cats:
        cats.append(pro_name)
print("关联专业大类", cats)
print("-" * 10)
# 在公司信息索引company中按公司行业查找，获取对应的公司列表
q = ""
for cat in cats:
    q += " " + cat
s2 = Search(using=es, index='company')
s2 = s2.query("multi_match", query=q.strip(), fields=['industry'])
s2 = s2[0:5000]
res2 = s2.execute()
companys = []
shebaosort = []
for indexid, hit in enumerate(res2):
    name = hit.name
    business_scope = hit.business_scope  # 经营范围
    business_scope = re.sub(u'[（](.*?)[）]|[(](.*?)[)]', '', business_scope)
    business_scope = business_scope.replace("一般项目", "").replace("许可项目", "").replace("-", "").replace("\u3000", "")
    business_scope = re.split(u"[;；、。：，]", business_scope)
    business_scope = list(filter(None, business_scope))
    business_scope = list(set(business_scope))
    try:
        num_social_security = hit.num_social_security  # 社保人数
        int(num_social_security)
    except:
        continue
    pay_capital = hit.pay_capital.replace("万美元", "").replace("-", "")  # 注册资本
    if "." in pay_capital:
        pay_capital = pay_capital.split(".")[0]
    if pay_capital == '':
        pay_capital = '0'
    label = hit.label  # 标签
    if name not in companys:
        companys.append(
            {
                "name": name,  # 公司名称
                "business_scope": business_scope,  # 经营范围
                "num_social_security": num_social_security,  # 社保人数
                "pay_capital": pay_capital,  # 实缴金额
                "label": label,  # 标签
            }
        )

# 获取社保人数不为0的列表first，并根据社保人数排序
first = list(filter(lambda x: x["num_social_security"] != "0", companys))
first = sorted(first, key=lambda x: int(x['num_social_security']), reverse=True)  # 社保不为0列表
# 获取社保人数为0的列表second
second = list(filter(lambda x: x["num_social_security"] == "0", companys))
# second根据实缴资本划分实缴资本不为0的列表second1和为0的列表second2
second1 = list(filter(lambda x: x["pay_capital"] != "0", second))
second2 = list(filter(lambda x: x["pay_capital"] == "0", second))
# 不为0的列表second1根据实缴资本排序
second1 = sorted(second1, key=lambda x: int(x['pay_capital']), reverse=True)  # 社保为0，实缴不为0列表
# 实缴资本为0的列表根据标签中是否有特定标签牌子前面
importlabel = ["科技小巨人企业", "雏鹰企业", "专精特新小巨人企业", "瞪羚企业", "企业技术中心", "民营科技企业", "专精特新企业",
               "高新技术企业", "科技型中小企业"]
third1 = []
third2 = []
for company in second2:
    flag = False
    label = company["label"]
    for lab in label:
        if lab in importlabel:
            third1.append(company)
            flag = True
    if flag:
        third2.append(company)
third = third1 + third2  # 社保为0，实缴为0，按是否有标签排序列表
print("各个字段排序得到的列表长度:")
print("社保人数不为0:", len(first), "实缴金额不为0:", len(second1), "标签:", len(third))
print("-" * 10)

# 组合各个情况排序得到的三个列表
print("最终公司列表信息(排序后n条):")
finallst = first + second1 + third
for lst in finallst[:10]:
    # print(lst["num_social_security"], lst["pay_capital"], lst["label"])
    print(lst)
print("-" * 10)

# 根据公司名称获取经营范围，公司全名必须是finallst中有的
#  ------输入的专公司全名-----
com_name = "厦门市火之辉文化创意有限公司"
#  ------------------------
print("输入(点击)公司全名:", com_name)
scope = list(filter(lambda x: x["name"] == com_name, finallst))
if scope is not None:
    bs = scope[0]["business_scope"]
    bs.sort(key=lambda x: len(x), reverse=False)
    print("经营范围为:", bs)
    # 得到经营范围，下面写根据经营范围生成标题代码
else:
    print("找不到该公司")

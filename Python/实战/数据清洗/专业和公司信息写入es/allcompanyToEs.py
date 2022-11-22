# coding: utf-8
# http://192.168.1.11:9200/_cat/indices?v&pretty
import json

from elasticsearch import Elasticsearch

es = Elasticsearch('119.29.115.135:9200')

mapping = {
    'properties': {
        'name': {
            'type': 'string',
            'analyzer': 'jieba',
            'search_analyzer': 'jieba'
        },
        'industry': {
            'type': 'string',
            'analyzer': 'jieba',
            'search_analyzer': 'jieba'
        },
        'business_scope': {
            'type': 'string',
            'analyzer': 'jieba',
            'search_analyzer': 'jieba'
        },
        'num_social_security': {
            'type': 'string',
            'analyzer': 'jieba',
            'search_analyzer': 'jieba'
        },
        'pay_capital': {
            'type': 'string',
            'analyzer': 'jieba',
            'search_analyzer': 'jieba'
        },
        "label": {
            'type': 'string',
            'analyzer': 'jieba',
            'search_analyzer': 'jieba'
        },
    }
}
# 删除索引
es.indices.delete(index='company', ignore=[400, 404])

# 创建索引
# es.indices.create(index='company', ignore=400)

# 创建映射
# 设置mapping 信息：指定字段的类型 type 为 text
# 分词器 analyzer 和 搜索分词器 search_analyzer 为 ik_max_word，即中文分词插件，默认的英文分词器。
# result = es.indices.put_mapping(index='company', doc_type='com', body=mapping)
# print(result)

# 插入数据
# datas = [
#     {
#         "pro_name": "哲学",
#         "categories": "哲学",
#     },
#     {
#         "pro_name": "哲学",
#         "categories": "逻辑学",
#     },
#     {
#         "pro_name": "哲学",
#         "categories": "宗教学",
#     },
#     {
#         "pro_name": "哲学",
#         "categories": "伦理学",
#     },
# ]
import re

# 取出csv文件创建索引
path = "./allcompany.csv"
datas = []
importlabel = ["科技小巨人企业", "雏鹰企业", "专精特新小巨人企业", "瞪羚企业", "企业技术中心", "民营科技企业", "专精特新企业",
               "高新技术企业", "科技型中小企业"]
with open(path, "r", encoding="utf8") as f:
    for i, line in enumerate(f):
        if i < 256804:
            continue
        line = line.split(",")
        try:
            business_scope = line[20]
            business_scope = re.sub(u'[（](.*?)[）]|[(](.*?)[)]', '', business_scope)
            business_scope = business_scope.replace("一般项目", "").replace("许可项目", "").replace("-", "").replace("\u3000",                                                                                                             "")
            business_scope = re.split(u"[;；、。：，/]", business_scope)
            business_scope = list(filter(None, business_scope))
            business_scope = list(set(business_scope))
            business_scope = ";".join(business_scope)
        except:
            business_scope = ""
        try:
            pay_capital = str(line[5]).replace("万美元", "").replace("万元人民币", "").replace("-", "")  # 注册资本
        except:
            continue
        if "." in pay_capital:
            pay_capital = pay_capital.split(".")[0]
        if pay_capital == '':
            pay_capital = '0'
        # print(line)
        label = "".join(line[23:-1])
        # print(label, type(label))
        items = []
        for item in importlabel:
            if item in label:
                items.append(item)
        try:
            onedata = {"name": line[0], "industry": line[14], "business_scope": business_scope, "num_social_security": line[18],
                       "pay_capital": pay_capital, "label": str(items)}
        except:
            continue
        print(i)
        es.index(index='company', doc_type='politics', body=onedata)

# 查询索引
# result = es.search(index='professional', doc_type='politics')
# print(result)    # 返回所有结果

# 使用 DSL 语句来进行查询： match 指定全文检索，检索字段 title，检索内容 “中国领事馆”
# dsl = {
#     'query': {
#         'match': {
#             'name': '黑龙江'
#         }
#     }
# }
# result = es.search(index='company', doc_type='politics', body=dsl)
# print(json.dumps(result, indent=2, ensure_ascii=False))

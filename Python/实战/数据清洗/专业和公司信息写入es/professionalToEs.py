# coding: utf-8
# http://192.168.1.11:9200/_cat/indices?v&pretty
import json

from elasticsearch import Elasticsearch

es = Elasticsearch('192.168.1.11:9200')

mapping = {
    'properties': {
        'pro_name': {
            'type': 'string',
            'analyzer': 'jieba',
            'search_analyzer': 'jieba'
        },
        'categories': {
            'type': 'string',
            'analyzer': 'jieba',
            'search_analyzer': 'jieba'
        }
    }
}
# 删除索引
# es.indices.delete(index='professional', ignore=[400, 404])

# 创建索引
# es.indices.create(index='professional', ignore=400)

# 创建映射
# 设置mapping 信息：指定字段的类型 type 为 text
# 分词器 analyzer 和 搜索分词器 search_analyzer 为 ik_max_word，即中文分词插件，默认的英文分词器。
# result = es.indices.put_mapping(index='professional', doc_type='pro', body=mapping)
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

# 取出csv文件创建索引
# path = "./data/professional.csv"
# datas = []
# with open(path, "r", encoding="utf8") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         if i == 0:
#             continue
#         else:
#             line = line.split(",")
#             # print(line)
#             onedata = {"pro_name": line[1], "categories": line[4]}
#             datas.append(onedata)
# print(datas)
# for data in datas:
#     es.index(index='professional', doc_type='politics', body=data)

# 查询索引
# result = es.search(index='professional', doc_type='politics')
# print(result)    # 返回所有结果

# 使用 DSL 语句来进行查询： match 指定全文检索，检索字段 title，检索内容 “中国领事馆”
dsl = {
    'query': {
        'match': {
            'pro_name': '哲学'
        }
    }
}
result = es.search(index='professional', doc_type='politics', body=dsl)
print(json.dumps(result, indent=2, ensure_ascii=False))
## 查询通用代码
```
"""
index： 要查询的索引
doc_type:  索引数据的存储类型
body:  查询的请求体,dict
"""
result = es.search(index='index_name', doc_type='doc', body=body)
hits = result["hits"]["hits"]
```

## 一、普通查询
```
# 查询多个字段中至少一个满足(包含)检索词
# text:检索词，fields:匹配字段
text = "" 
client = Elasticsearch('159.75.133.10:9200')
s = Search(using=client, index='title_ci')
s = s.query("multi_match", query=text, fields=['title', 'hao', 'keyword'])
s = s[0:5000]
res = s.execute()

# 自由构建body，单个字段包含检索词
body = {
    "query": {
        "match": {"title": label},
    },
    "from": 1,
    "size": 30,
}
```

## 二、与查询
```
# 查询某个字段同时包含多个字符的数据
body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "smallword": text1,
                        }
                    },
                    {
                        "match": {
                            "smallword": text2,
                        }
                    },
                ]
            },
        },
        "size": 50,
    }

# 不确定输入，且输入的是一段连续文本，需要分词
text = "沉积作用 贝类"
body = {
    "query": {
        "bool": {
            "must": []
        },
    },
    "size": 500,
}
# 对搜索词进行分词，以xinqi_fenxi的bigword大类进行或匹配
texts = jieba.cut_for_search(text)
texts = list(texts)
texts = list(filter(None, texts))
print("es检索词:", texts)
for text in texts:
    if text == " ":
        continue
    body["query"]["bool"]["should"].append(
        {
            "match": {
                "bigword": text,
            }
        },
    )
```

## 三、或查询
```
# 查询多个match只需要满足一个的情况
body = {
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "smallword": text1,
                        }
                    },
                    {
                        "match": {
                            "smallword": text2,
                        }
                    },
                ]
            },
        },
        "size": 50,
    }

# 不确定输入，且输入的是一段连续文本，需要分词
text = "沉积作用 贝类"
body = {
        "query": {
            "bool": {
                "should": []
            },
        },
        "size": 500,
}
# 对搜索词进行分词，以xinqi_fenxi的bigword大类进行或匹配
texts = jieba.cut_for_search(text)
texts = list(texts)
texts = list(filter(None, texts))
print("es检索词:", texts)
for text in texts:
    if text == " ":
        continue
    body["query"]["bool"]["should"].append(
        {
            "match": {
                "bigword": text,
            }
        },
    )
```


## 四、整合Query方法
```
def diffWordOrQuery(field, texts, size):
    """
    作用: 构建es分词或查询query查询体
    field:str.要检索的字段
    texts:list.对检索文本进行分词后的词列表
    size:int.单次检索要返回的数量
    """
    body = {
        "query": {
            "bool": {
                "should": []
            },
        },
        "size": size,
    }
    for text in texts:
        if text == " ":
            continue
        body["query"]["bool"]["should"].append(
            {
                "match": {
                    field: text,
                }
            },
        )
    return body


def oneWordQuery(field, text, size):
    """
    作用: 对单个检索词匹配单个字段检索
    field:str.要检索的字段
    text:str.检索文本
    size:int.单次检索要返回的数量
    """
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            field: text,
                        }
                    },
                ]
            }
        },
        "size": size,
    }
    return body


def matchQuery(field, text, size):
    """
    作用: 最简单单个检索词匹配单个字段检索
    field:str.要检索的字段
    text:str.检索文本
    size:int.单次检索要返回的数量
    """
    body = {
        "query": {
            "match": {field: text},
        },
        "size": size,
    }
    return body


def matchAllQuery(size):
    """
    作用: 单个检索词匹配所有
    size:int.单次检索要返回的数量
    """
    body = {
        "query": {
            "match_all": {},
        },
        "size": size,
    }
    return body

```
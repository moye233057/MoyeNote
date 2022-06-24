import codecs
import re
import json
from elasticsearch import Elasticsearch

es = Elasticsearch(['192.168.1.106:9200'])

# 查找第一个{前的内容
part = re.compile(u'^([^\{]*)\{.*$')
# 打开数据文件
lines = codecs.open("G:\doc_2018050600", 'r', 'utf_8_sig').readlines()
for line in lines:
    try:
        doc = []
        deletext = ''.join(re.findall(part, line))
        t2 = re.sub(deletext, '', line)
        t3 = json.loads(t2)
        t3['contents'] = t3['contents'][0]['cont']
        doc.append({'index': {}})
        doc.append(t3)
        es.bulk(index='doc_2018050600', doc_type='test-type', body=doc)
        print('sucess')
    except:
        print('false')
        print(t3['title'])
        continue

# 逐行读取
import os
import codecs
import re
import json
import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(['192.168.1.106:9200'], timeout=180)
part = re.compile(u'^([^\{]*)\{.*$')
# 需要写入的文件路径列表
paths = [
    "G:\doc_2018050607",
    "G:\doc_2018050608",
    "G:\doc_2018050609",
]
for path in paths:
    # 当前文件第一次写入时间
    start_time = datetime.datetime.now()
    f = codecs.open(path, 'r', 'utf_8_sig')
    line = f.readline()
    name = path.replace('G:\\', '')
    i = 0
    while line:
        # 每一千条记录一次时间
        if i % 1000 == 0:
            record = open("G:\\" + name + ".txt", "a")
            record.write(str(start_time) + "\n")
            mid_time = datetime.datetime.now()
            record.write(str(i - 1000) + "到" + str(i) + "所需时间为:" + str((mid_time - start_time).seconds) + "\n")
        try:
            doc = []
            deletext = ''.join(re.findall(part, line))
            t2 = re.sub(deletext, '', line)
            t3 = json.loads(t2)
            t3['contents'] = t3['contents'][0]['cont']
            doc.append({'index': {}})
            doc.append(t3)
            # 写入数据，name为索引名称
            es.bulk(index=name, doc_type='test-type', body=doc)
            print('sucess')
            i += 1
            line = f.readline()
        except:
            print('false')
            print(t3['title'])
            i += 1
            line = f.readline()

print(doc)
print(len(t3['contents']))
print(es.indices.exists(index="test"))
print(os.path.exists('G:\doc_2018050523'))
doc = [
    {"index": {}},
    {"test": "测试"},
]

# 报错一
# elasticsearch.exceptions.RequestError: TransportError(400, 'illegal_argument_exc
# eption
# ')
# 表现形式: 集群健康值颜色变黄，出现一个Unassigned表示有数据未分片的信息
# 出现原因: 该集群只有一个主节点
# 解决办法: 可以本机或其他同局域网机器多开一个子节点
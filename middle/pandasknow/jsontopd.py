import json
import os
import pandas as pd

path_to_json = '/content/drive/MyDrive/englishsum/jsondata'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
jsons_data = pd.DataFrame(columns=['paper_id', 'abstract', 'body_text'])

id2abstract = []
for index, js in enumerate(json_files[:100]):  # Using 1000 files only to reduce memory load and resources
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        paper_id = json_text['paper_id']

        abstract = ''
        for entry in json_text['abstract']:
            abstract += entry['text']
        id2abstract.append({paper_id: abstract})

        body_text = ""
        for entry in json_text['body_text']:
            body_text += entry['text']

        jsons_data.loc[index] = [paper_id, abstract, body_text]

df = jsons_data
stopwords = ['word1', 'word2']
# 字数统计
df['word_count'] = df['word'].apply(lambda x: len(x.strip().split()))  # word count in abstract
# 删除所有行中字数统计为0的行
df.drop(df.index[df['word'] == 0], inplace=True)
# 变小写
df["abstract"] = df["abstract"].str.lower()
# 去除停用词
df['abstract'] = df['abstract'].apply(
    lambda x: " ".join([word for word in x.split() if word not in stopwords]))
# 数据清洗时，会将带空值的行删除，此时DataFrame或Series类型的数据不再是连续的索引
# 删除行后，原来的行索引不能用作索引，需要建立新的索引，drop=True代表不保留原来的index
data = df.reset_index(drop=True)

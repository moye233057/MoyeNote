import jieba

path = 'words.txt'

with open(path,'r',encoding='utf-8-sig') as f:
    word = f.readline().replace('\n','')
    cut = jieba.cut(word)
    print(list(cut))
    while word:
        word = f.readline().replace('\n', '')
        cut = jieba.cut(word)
        print(list(cut))

# 文本相似度
from fuzzywuzzy import fuzz
# aa=fuzz.partial_ratio(u"??????????fd??", u""" """)
# print(aa)
aa = fuzz.ratio("this is a test", "this is a test!")
if aa>80:
    print ('good')

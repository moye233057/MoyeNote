# segs = jieba.cut(content)
# segs = jieba.cut(content, cut_all=True) #全模式

# for seg in segs:
#         if len(seg) > 1 and seg != '\r\n':
# 如果说分词得到的结果不是单字，且不是换行符，则加入到数组中

# jieba.add_word(str) 添加单个关键词
# jieba.load_userdict() 批量设置关键词
# 1、步骤一：创建文件，将自己想要添加的词输入进去。格式为词-换行-词。。。
# 2、导入文件并命名，并使用jieba.load_userdict()方法。
# word_file = "word.txt"
# jieba.load_userdict(word_file)
# 3、利用pandas统计词频
# df = pandas.DataFrame({'关键词':words})
# words_count = df.groupby(by=['关键词'])['关键词'].agg({"出现次数":numpy.size})
# words_count = words_count.reset_index().sort_values(by="出现次数",ascending=False)

# 删除停止词
# x = ' '.join([word for word in x.split(' ') if word not in stop_words])

# 删除unicode字符
# x = x.encode('ascii', 'ignore').decode()


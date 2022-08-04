1.jieba是python中的中文分词第三方库，可以将中文的文本通过分词获得单个词语，返回类型为列表类型。

2.jieba分词共有三种模式：精确模式、全模式、搜索引擎模式。
（1）精确模式语法：
jieba.lcut(字符串,cut_all=False)，默认时为cut_all=False,表示为精确模型。精确模式是把文章词语精确的分开，并且不存在冗余词语，切分后词语总词数与文章总词数相同。
（2）全模式语法：
jieba.lcut(字符串,cut_all=True)，其中cut_all=True表示采用全模型进行分词。全模式会把文章中有可能的词语都扫描出来，有冗余，即在文本中从不同的角度分词，变成不同的词语。
（3）搜索引擎模式：在精确模式的基础上，对长词语再次切分。
jieba.lcut_for_search(str)
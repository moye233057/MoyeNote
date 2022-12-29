## 安装pyhanlp和hanlp
```
pip install pyhanlp
pip install hanlp[full] -U  # 整个安装过程比较长，且可能安装多个版本的不同库，运行到最后即可，中途断了也会有缓存
pip install --upgrade termcolor  # 如果提示缺少termcolor这个模块单独安装
pip install --upgrade numpy  # 如果提示numpy相关的错误，有可能是numpy版本过低，需要更新
```

## 主程序代码
```
# 一*-coding : utf-8 -*-
from 关键词 import *
from pyhanlp import HanLP
import re, hanlp

HanLP.Config.ShowTermNature = False
model_zdxj = hanlp.load('MRP2020_AMR_ENG_ZHO_XLM_BASE')


def judge(content, keys):
    sentence_seg = HanLP.parseDependency(content)
    # print(sentence_seg)
    senDanci = []
    danci, daici, key_find = [], [], ''
    for word in sentence_seg.iterator():
        danci.append(word.LEMMA)
        senDanci.append((word.LEMMA, word))
        if AttributeMatch.get(word.POSTAG, "") == "代词":  # 判断是否需要指代消解
            daici.append(word.LEMMA)
    # print("单词:", danci)
    # print("keys:", keys)
    for word in senDanci:
        if word[0] in keys:
            if AttributeMatch.get(word[1].POSTAG, "") == "动词":  # 判断是否是有效关键词
                key_find = word[0]
                break
            # else:
                # print(f'警告！{word}非动词')
    return danci, daici, key_find


def zdxj(content, keys):  # 指代消解
    danci, daici, key_find = judge(content, keys)
    if not daici:
        return content, key_find
    zdxj_res = model_zdxj(danci, output_amr=False)
    sentence = list(zdxj_res["input"])
    zdxj_nodes = zdxj_res["nodes"]
    for node in zdxj_nodes:
        if len(node["anchors"]) >= 2:
            replace = node["anchors"][0]
            for i, j in enumerate(node["anchors"]):
                if i > 0:
                    sentence[j['from']:j['to']] = sentence[replace['from']:replace['to']]
    return "".join(sentence).replace(" ", ""), key_find


def text_process(content):
    find = re.findall(r"(说　明　书.*?.*?)[\s\u4e00-\u9fa5]", content)
    for i in find:
        content = content.replace(i, "")
    return re.sub(r"\(.*?\)|\[.*?]", "", content)


def setences_get(content):
    setence = content.split('。')
    setence = list(filter(None, setence))
    setences = []
    for i in setence:
        setences.extend(i.split('；'))
    return setences


def main(content):
    content = text_process(content)
    setences = setences_get(content)
    key_find, res, keys = '', [], set(key_dic.keys())
    for setence in setences:
        setence_new = setence + "。"
        setence_new, key_find = zdxj(setence_new, keys)
        if not key_find:
            continue
        index = setence_new.find(key_find)
        _s = setence_new[:index]
        s_ = key_dic[key_find] + setence_new[index + len(key_find):].replace("了", "").replace("。", "？").replace(
            key_find, '')
        res.append(s_ if len(s_) > 5 else "")
    change_txt = "".join(res)
    print("关键词", key_find, "转化后：", change_txt)
    print("-" * 10)
    return key_find, change_txt


# def main(content):
#     content=text_process(content)
#     setences=setences_get(content)
#     find,res,keys= False,[],set(key_dic.keys())
#     for setence in setences:
#         for key in key_dic.keys():
#             if key in setence:
#                 find,key_value=True,False
#                 setence_new = setence+"。"
#                 try:
#                     setence_new,key_value=zdxj(setence_new,key)
#                 except:
#                     pass
#                 if not key_value:
#                     continue
#                 index = setence_new.find(key)
#                 _s=setence_new[:index]
#                 s_=key_dic[key]+setence_new[index+len(key):].replace("了","").replace("。","？").replace(key,'')
#                 res.append(s_ if len(s_)>5 else "")
#                 if key_value:
#                     break
#     if find:
#         print("转化后：", "".join(res))
#     else:
#         print("不存在关键匹配词，匹配失败。")
#     return find


if __name__ == "__main__":
    path = "./有益效果.txt"
    res_path = "./转化结果.txt"
    cut = " " * 3  # 每一列的分割符
    with open(path, "r") as f:
        with open(res_path, "w", encoding="utf-8") as save_f:
            lines = f.readlines()
            for line in lines:
                spline = line.split("	")
                try:
                    youyi = spline[2]
                except:
                    print("错误数据:", youyi)
                    continue
                key_find, change_txt = main(youyi)
                if len(change_txt) != 0:
                    write_txt = change_txt + cut + key_find + cut + youyi   +  "\n"
                    save_f.write(write_txt)

    # 测试数据
    # content1 = "因此比传统的社交媒体事件抽取方法所得到的结果更准确，应用场景也更加广泛。"
    # content2 = "本发明能有效地汇聚分散的社交媒体信息，直观地用实体关系模型多粒度地表达中间和最终的事件探测结果，因此比传统的社交媒体事件抽取方法所得到的结果更准确，应用场景也更加广泛。"
    # content3 = "在实际应用中，网络运营商可通过本发明技术方案获得用户感兴趣的网页类型特征，更加有针对性的为用户提供服务。"
    # content4 = "3)通过本发明所提供的文学作品竞猜方法构建好竞猜知识库后，竞猜者可使用竞猜知识库以多种竞猜方式进行答题，系统根据竞猜者答题过程中花费的时间、正确率进行综合评价，并给出得分，以此定量地反映竞猜者对该文学作品的熟悉程度。"
    # content5 = "混合模型的优点是在较高的精度和较高的计算速度之间提供平衡。"
    # content6 = "这种语音交互的方式更容易吸引用户，而且智能交互一方面可以使用户更方便、快捷地获取列多感兴趣的金融信息说　明　书1/4页3CN 106126624 A3内容，另一方面可以使金融信息的投放更有针对性。"
    # content7 = "3.本发明提供一种大数据的存储方式，通过可扩展的列族数据，能够存储非常大量的录波文件。通过这些大量的录波数据，可以进行机器学习，智能分析，产生更大的价值，改变了录波文件远程调取，人为分析的旧的模式。"
    # content8 = "当使用几何链接时，搜索和检索可以得到改善且更高效。"
    # content9 = "有益效果：本发明与现有技术相比，其显著优点是：本发明提供的潮沟壁稳定计算方法，结合河口海岸动力学与土力学，综合考虑潮流对潮沟壁下部的侵蚀掏空过程和潮沟壁在自身重力作用下的坍塌过程，可以模拟出潮沟壁的破坏过程、判断潮沟壁失稳的破坏类型、确定破坏区，为潮沟壁稳定计算提供新方法，促进了潮沟蜿蜒摆动研究的发展。"
    # content10 = "本发明提供的方案能够简便高效地对空调进行选型，并能够对选出的机型的部件和配件进行调整，增加了空调选型的可选范围。"
    # content11 = r".通过采用离散特征选取与深度语义相结合的策略，一方面利用未标注语料扩充已有的训练语料，增加训练打分过程的准确率，另一方面将隐式篇章关系各个层次的语义信息相结合，在隐式篇章关系类别标签的指导下提升分析精度的同时，实现了各层次语义向量的互相优化。"
    # content12 = r".能够有效地利用未标注语料及不同层次语义信息进行分析，使用户能够更快速而准确地获得隐式篇章关系的分析结果。"
    # content13 = r"其次，多语言动态编译和执行引擎还增加了异步编程执行队列模型，可以减少网络交互节约大量IO网络流量，以此缩短响应时间，提高吞吐量。"
    # lst = [content1, content2, content3, content4, content5, content6, content7, content8, content9, content10,
    #        content11, content12]
    # 测试一:
    # for con in lst:
    #     main(con)
    # 测试二:
    # sentence_seg=HanLP.parseDependency(content)
    # sentence_seg1=HanLP.parseDependency(content1)
    # sentence_seg2=HanLP.parseDependency(content2)
    # print(sentence_seg)
    # print(sentence_seg1)
    # print(sentence_seg2)
    # for word in sentence_seg.iterator():
    #     print(type(word.ID))

    # with open("Sample.txt","r",encoding="GBK") as fp:
    #     for i,f in enumerate(fp.readlines()):
    #         get=f.split("\t")
    #         if len(get) <= 2:
    #             continue
    #         num,title,content=get[0],get[1],get[2].strip().replace("\n","")
    #         print("原句：",content)
    #         main(content)

```

## 关键词.py
```
# 一*-coding : utf-8 -*-
# author: Canden Cao time: 2022/12/19
key_dic = {
    "加快": "如何加快",
    "实现": "如何实现",
    "解决": "如何解决",
    "简化": "如何简化",
    "提高": "如何提高",
    "降低": "如何降低",
    "减小": "如何减小",
    '减少': "如何减少",
    "免除": "如何免除",
    '避免': '如何避免',
    '摆脱': '如何摆脱',
    '保证': '如何保证',
    '节省': '如何节省',
    '防止': '如何防止',
    '指导': '如何指导',
    '提供': '如何提供',
    '弥补': '如何弥补',
    '克服': '如何客服',
    '增强': '如何增强',
    '处理': '如何处理'
}
key_words = {'从而', '提供', '服务', '简便', '能够', '有效', '平衡', '可以'}
AttributeMatch = {
    "a": r'形容词',
    "ad": r'副形词',
    "ag": r'形容词性语素',
    "al": r'形容词性惯用语',
    "an": r'名形词',
    "b": r'区别词',
    "begin": "begin",
    "bg": r'区别语素',
    "bl": r'区别词性惯用语',
    "c": r'连词',
    "cc": r'并列连词',
    "d": r'副词',
    "dg": r'辄,俱,复之类的副词',
    "dl": r'连语',
    "e": r'叹词',
    "end": r'仅用于终##终',
    "f": r'方位词',
    "g": r'学术词汇',
    "gb": r'生物相关词汇',
    "gbc": r'生物类别',
    "gc": r'化学相关词汇',
    "gg": r'地理地质相关词汇',
    "gi": r'计算机相关词汇',
    "gm": r'数学相关词汇',
    "gp": r'物理相关词汇',
    "h": r'前缀',
    "i": r'成语',
    "j": r'简称略语',
    "k": r'后缀',
    "l": r'习用语',
    "m": r'数词',
    "mg": r'数语素',
    "Mg": r'甲乙丙丁之类的数词',
    "mq": r'数量词',
    "n": r'名词',
    "nb": r'生物名',
    "nba": r'动物名',
    "nbc": r'动物纲目',
    "nbp": r'植物名',
    "nf": r'食品，比如“薯片”',
    "Ng": r'名词性语素',
    "nh": r'医药疾病等健康相关名词',
    "nhd": r'疾病',
    "nhm": r'药品',
    "ni": r'机构相关（不是独立机构名）',
    "nic": r'下属机构',
    "nis": r'机构后缀',
    "nit": r'教育相关机构',
    "nl": r'名词性惯用语',
    "nm": r'物品名',
    "nmc": r'化学品名',
    "nn": r'工作相关名词',
    "nnd": r'职业',
    "nnt": r'职务职称',
    "nr": r'人名',
    "nr1": r'复姓',
    "nr2": r'蒙古姓名',
    "nrf": r'音译人名',
    "nrj": r'日语人名',
    "ns": r'地名',
    "nsf": r'音译地名',
    "nt": r'机构团体名',
    "ntc": r'公司名',
    "ntcb": r'银行',
    "ntcf": r'工厂',
    "ntch": r'酒店宾馆',
    "nth": r'医院',
    "nto": r'政府机构',
    "nts": r'中小学',
    "ntu": r'大学',
    "nx": r'字母专名',
    "nz": r'其他专名',
    "o": r'拟声词',
    "p": r'介词',
    "pba": r'介词“把”',
    "pbei": r'介词“被”',
    "q": r'量词',
    "qg": r'量词语素',
    "qt": r'时量词',
    "qv": r'动量词',
    "r": r'代词',
    "rg": r'代词性语素',
    "Rg": r'古汉语代词性语素',
    "rr": r'人称代词',
    "ry": r'疑问代词',
    "rys": r'处所疑问代词',
    "ryt": r'时间疑问代词',
    "ryv": r'谓词性疑问代词',
    "rz": r'指示代词',
    "rzs": r'处所指示代词',
    "rzt": r'时间指示代词',
    "rzv": r'谓词性指示代词',
    "s": r'处所词',
    "t": r'时间词',
    "tg": r'时间词性语素',
    "u": r'助词',
    "ud": r'助词',
    "ude1": r'的 底',
    "ude2": r'地',
    "ude3": r'得',
    "udeng": r'等 等等 云云',
    "udh": r'的话',
    "ug": r'过',
    "uguo": r'过',
    "uj": r'助词',
    "ul": r'连词',
    "ule": r'了 喽',
    "ulian": r'连 （“连小学生都会”）',
    "uls": r'来讲 来说 而言 说来',
    "usuo": r'所',
    "uv": r'连词',
    "uyy": r'一样 一般 似的 般',
    "uz": r'着',
    "uzhe": r'着',
    "uzhi": r'之',
    "v": r'动词',
    "vd": r'副动词',
    "vf": r'趋向动词',
    "vg": r'动词性语素',
    "vi": r'不及物动词（内动词）',
    "vl": r'动词性惯用语',
    "vn": r'名动词',
    "vshi": r'动词“是”',
    "vx": r'形式动词',
    "vyou": r'动词“有”',
    "w": r'标点符号',
    "wb": r'百分号千分号，全角：％ ‰ 半角：%',
    "wd": r'逗号，全角：， 半角：,',
    "wf": r'分号，全角：； 半角： ;',
    "wh": r'单位符号，全角：￥ ＄ ￡ ° ℃ 半角：$',
    "wj": r'句号，全角：。',
    "wky": r'右括号，全角：） 〕 ］ ｝ 》 】 〗 〉 半角： ) ] { >',
    "wkz": r'左括号，全角：（ 〔 ［ ｛ 《 【 〖 〈 半角：( [ { <',
    "wm": r'冒号，全角：： 半角： :',
    "wn": r'顿号，全角：、',
    "wp": r'破折号，全角：—— －－ ——－ 半角：— —-',
    "ws": r'省略号，全角：…… …',
    "wt": r'叹号，全角：！',
    "ww": r'问号，全角：？',
    "wyy": r'右引号，全角：” ’ 』',
    "wyz": r'左引号，全角：“ ‘ 『',
    "x": r'字符串',
    "xu": r'网址URL',
    "xx": r'非语素字',
    "y": r'语气词(delete yg)',
    "yg": r'语气语素',
    "z": r'状态词',
    "zg": r'状态词'
}

```
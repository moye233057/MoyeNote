# coding: utf-8
import datetime
from collections import Counter
import pyfpgrowth
from elasticsearch import Elasticsearch

nowyear = datetime.datetime.now().year


def classifyByBigOrSamll(filepath, end=-1):
    """
    Args:
        filepath: 文件路径，txt
        end: 统计多少行的数据，默认-1表示所有
    Returns:

    """
    entry = []
    finalbigdata = []
    finalsmalldata = []
    oneBigType = []
    oneSmallType = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        thisbig = None
        thissmall = None
        for i, line in enumerate(lines):
            line = line.split("	")
            big = line[5]  # 获取这一行数据的大类划分符
            if not thisbig:
                thisbig = big
            elif thisbig != big:
                thisbig = big
                finalbigdata.append(oneBigType)
                oneBigType = entry.copy()
            small = line[4]  # 获取这一行数据的小类
            if not thissmall:
                thissmall = small
            elif thissmall != small:
                thissmall = small
                finalsmalldata.append(oneSmallType)
                oneSmallType = entry.copy()
            word = line[6]
            info = line[7]
            year = int(info.split("=")[0][2:6])
            bigdata = {
                "big": big,
                "small": small,
                "word": word,
                "year": year,
            }
            oneBigType.append(bigdata)
            smalldata = {
                "big": big,
                "small": small,
                "word": word,
                "year": year,
            }
            oneSmallType.append(smalldata)

            if i == end:
                break

    # print("大类数量", len(finalbigdata))
    # print(finalbigdata)
    # print("小类数量", len(finalsmalldata))
    # print(finalsmalldata)
    return finalbigdata, finalsmalldata


def createBigAndSmall(finalbigdata, finalsmalldata):
    bigdata = []
    for big in finalbigdata:
        # print(len(big), big)
        patterns = getWordCountByYear(big)
        # print(len(patterns), "fp-grop生成词组数据:", patterns)
        bigword = max(patterns.items(), key=lambda x: x[1])
        # print("----大类及其频次----")
        # print(bigword)
        bigwordlst = list(bigword[0])
        biglst = list(filter(lambda x: bigwordlst[0] in x["word"] and bigwordlst[1] in x["word"], big))
        # print("----与大类有关的专利----")
        for big in biglst:
            big["bigword"] = " ".join(list(bigword[0]))
            big["bignum"] = bigword[1]
        # print(len(biglst), biglst)
        bigdata += biglst
    # print("----大类初步统计----")
    # print(bigdata)

    # print("+++++小类统计+++++")
    for i, small in enumerate(finalsmalldata):
        bigflag = small[0]["big"]
        smallflag = small[0]["small"]

        patterns = getWordCountByYear(small)
        fpgrowCount = len(patterns)
        if len(patterns) == 0:
            sword = ""
            smallwordCount = 0
        else:
            smallword = max(patterns.items(), key=lambda x: x[1])
            sword = " ".join(list(smallword[0]))
            smallwordCount = smallword[1]
        if fpgrowCount == 0:
            flag = '*'
        elif (smallwordCount / fpgrowCount) < 0.125:
            flag = '*'
        else:
            flag = ''

        replacebigdata = list(filter(lambda x: x['big'] == bigflag and x['small'] == smallflag, bigdata))
        for onebigdata in replacebigdata:
            onebigdata['smallword'] = sword
            onebigdata['smallnum'] = smallwordCount
            onebigdata['smallflag'] = flag
            # bigdata.append(onebigdata)
        # print('\n')
    return bigdata


def getWordCountByYear(lst, year=2100, mincount=1):
    """
    Args:
        lst: 要统计的列表，二维列表[[word11, word12...], [word21, word22...]...]，一个[]代表一个整体
        year: 年份，2015表示2015年之前的数据
        mincount: 出现的最小词频，例如输入3，词频为0,1,2的词不会被统计
    Returns:

    """
    year = int(year)
    lst = list(filter(lambda x: x['year'] <= year, lst))
    allwords = []
    for data in lst:
        words = data['word']
        words = words.split(" ")
        allwords.append(words)
    # print(allwords, type(allwords))
    patterns = pyfpgrowth.find_frequent_patterns(allwords, mincount)
    removeword = []
    for key, value in patterns.items():
        if len(key) < 2 or len(key) > 3:
            removeword.append(key)
    for word in removeword:
        patterns.pop(word)
    return patterns


def wordForTrend(text, increase_year=nowyear, new_year=nowyear):
    """
    Args:
        text: str, 要查询的热点词
        increase_year: int, 要查询哪一年的近期热点(某一年最快增长的词组)
        new_year: int, 要查询哪一年的新生问题(上一年没有但这一年出现的词组)
    Returns:
        newWordOfYear: 新生问题词组
        increaseWordOfYear:  近期热点词组
    """
    es = Elasticsearch('119.29.115.135:9200')
    start = 2015

    if not text:
        body = {
            "query": {
                "match_all": {}
            },
            "size": 10000
        }
    else:
        body = {
            "query": {
                "match": {"smallword": text.strip()}
            },
        }
    result = es.search(index='trend', doc_type='doc', body=body)
    hits = result["hits"]["hits"]
    res_data = []
    for indexid, hit in enumerate(hits):
        data = hit["_source"]
        res_data.append(data)

    # 获取上一年未出现但这一年第一次出现的词组
    datalater = list(filter(lambda x: x["year"] < new_year, res_data))
    # print(datalater)
    datanow = list(filter(lambda x: x["year"] == new_year, res_data))

    laterwords = []
    for data in datalater:
        try:
            smallword = data["smallword"]
        except:
            continue
        laterwords.append(smallword)
    laterwords = list(set(laterwords))

    newWordOfYear = []
    for data in datanow:
        smallword = data["smallword"]
        smallnum = data["smallnum"]
        if smallword not in laterwords:
            js = {
                "smallword": smallword,
                "smallnum": smallnum,
            }
            if js not in newWordOfYear:
                newWordOfYear.append(js)

    # 获取每年有新增数量的词语列表，降序排序，同时获取增长最大的词语
    # 获取每一年及其之前，词组出现评率的统计数据
    beforeYearData = []
    for year in range(start, increase_year + 1):
        data = list(filter(lambda x: x["year"] <= year, res_data))
        beforeYearData.append(data)

    countOfYear = {}
    for yeardata in beforeYearData:
        oneYearCount = {}
        for data in yeardata:
            try:
                word = data['smallword']
            except:
                continue
            oneYearCount[word] = oneYearCount.get(word, 0) + 1
        countOfYear[str(start)] = oneYearCount
        start += 1
    # print(countOfYear)
    # 用这一年的词组:数量字典减去上一年的词组:数量数组，并进行排序和找最大值
    increaseWordOfYear = []
    for year, count in countOfYear.items():
        if year == str(increase_year):
            break
        countOfYearIncrease = dict(Counter(countOfYear[str(int(year) + 1)]) - Counter(countOfYear[year]))
        if len(countOfYearIncrease) == 0:
            YearData = {
                "year": str(int(year) + 1),
                "Increase": [],
                "maxIncrease": {"smallword": None, "smallnum": 0}
            }
        else:
            maxIncrease = max(countOfYearIncrease.items(), key=lambda x: x[1])
            # print("maxIncrease", maxIncrease)
            sortIncrease = sorted(countOfYearIncrease.items(), key=lambda d: d[1], reverse=True)
            formatData = []
            for data in sortIncrease:
                js = {"smallword": data[0], "smallnum": data[1]}
                formatData.append(js)
            YearData = {
                "year": str(int(year) + 1),
                "Increase": formatData,
                "maxIncrease": {"maxword": maxIncrease[0], "maxnum": maxIncrease[1]},
            }
        increaseWordOfYear.append(YearData)
    # print(newWordOfYear)
    # print('-'*10)
    # print(increaseWordOfYear)
    # 某一年的上一年没有但这一年有的词组列表
    lastyearnowword = sorted(newWordOfYear, key=lambda d: d["smallnum"], reverse=True)
    # 某一年增长最快的词组排序列表
    lastyearincreaseword = list(filter(lambda x: x["year"] in [increase_year, str(increase_year)], increaseWordOfYear))
    returndata = {
        "newWordOfYear": lastyearnowword,
        "increaseWordOfYear": lastyearincreaseword,
    }
    return returndata


if __name__ == '__main__':
    filepath = './趋势分析语料.txt'  # 文件路径
    end = 1000  # 抽取多少条统计,负数代表所有
    finalbigdata, finalsmalldata = classifyByBigOrSamll(filepath=filepath, end=end)
    bigdata = createBigAndSmall(finalbigdata, finalsmalldata)
    # for data in bigdata:
    #     print(data)

    # 数据写入es索引
    # from elasticsearch import Elasticsearch
    # es = Elasticsearch('119.29.115.135:9200')
    # for i, data in enumerate(bigdata):
    #     print(i)
    #     es.index(index='trend', doc_type='doc', body=data)

    # 从es查询数据，分析形成近期热点和新生问题
    text = None
    returndata = wordForTrend(text, increase_year=2022, new_year=2022)
    print(returndata)

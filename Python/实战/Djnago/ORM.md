## 一、大量数据，分状态判断，分标签查询
```
"""django想要防止数据过多导致查询速度过慢最好的方法还是对queryset进行切片"""
# 获取页码和页码个数
try:
    pageNum = int(request.GET.get('pageNum'))
    needNum = int(request.GET.get('needNum'))
except:
    return responseJson(404, True, None, "页面或页码个数未收到")

def ClassifiedAccordingToKind(data, kind):
    """判断投资项目状态"""
    lst0 = []
    lst50 = []
    lst100 = []
    if kind == "0":
        print("提取50%")
        # lst0 = list(filter(lambda x: x["invest_status"] == "0%", data))
        lst50 = list(filter(lambda x: x["invest_status"] == "50%", data))
    elif kind == "1":
        print("提取100%")
        lst100 = list(filter(lambda x: x["invest_status"] == "100%", data))
    else:
        lst0 = list(filter(lambda x: x["invest_status"] == "0%", data))
        lst50 = list(filter(lambda x: x["invest_status"] == "50%", data))
        lst100 = list(filter(lambda x: x["invest_status"] == "100%", data))
    lst = lst50 + lst0 + lst100
    return lst

# 根据标签查询投资项目
tag = request.GET.get('tag', '')
# print("标签:", tag)
if len(tag) == 0:
    invests = Investment.objects.all()
    manualinvestments = invests.filter(entry_status="i_manual")
    autoinvestments = invests.filter(entry_status="i_auto")
else:
    try:
        investtag = InvestTag.objects.get(name=tag)
    except:
        return responseJson(404, True, None, "标签不存在")
    try:
        invests = investtag.investment_set.all()
        manualinvestments = invests.filter(entry_status="i_manual")
        autoinvestments = invests.filter(entry_status="i_auto")
    except:
        return responseJson(404, True, None, "找不到该标签对应的文章")
# 根据页码和页码个数筛选和缩减返回的数据数量
leftnum = 0 + (pageNum - 1) * needNum
rightnum = leftnum + needNum
if len(manualinvestments) > rightnum:
    print("手动大于需要")
    lst = manualinvestments
else:
    lst = manualinvestments | autoinvestments
total = len(lst)  # 符合条件的数据总数
# 对queryset结果集进行切割，防止序列化时执行太多次数据库查询
lst = lst[leftnum: rightnum]
# 对录入状态为手动和自动的数据分别进行序列化
serializers = InvestmentSerializers(lst, many=True)
# 根据搜索的Kind投资状态对每一份数据进行划分
kind = str(request.GET.get("kind"))
data = ClassifiedAccordingToKind(serializers.data, kind)
```
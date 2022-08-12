# 一、反转字典
方法一:
for k,v in myinfor.items():
     infor[v]=k
方法二:
myinfor =  {"name":"qiwsir","site":"qiwsir.github.io","lang":"python"}
reverseDict = dict(zip(myinfor.values(),myinfor.keys()))


json = {"zhangsan": 90, "lisi": 78, "wangermazi": 39}
# """求字典值的平均"""
lst = sum(list(json.values())) / len(json)
# """字典值的排序，利用sorted函数"""
sor = sorted(json.items(), key=lambda x: x[1], reverse=False)
turJson = [(json[i], i) for i in json]
sor1 = sorted(turJson, reverse=False)
print(lst)
print(sor)
print(sor1)

## 一、反转字典
`ˋ
#方法一:
for k,v in myinfor.items():
     infor[v]=k
#方法二:
myinfor =  {"name":"qiwsir","site":"qiwsir.github.io","lang":"python"}
reverseDict = dict(zip(myinfor.values(),myinfor.keys()))
`ˋ

## 二、求字典值的平均值
`ˋ
js = {"zhangsan": 90, "lisi": 78, "wangermazi": 39}
lst = sum(list(json.values())) / len(json)
print(lst)
`ˋ

## 三、字典值的排序，利用sorted函数
`ˋ
js = {"zhangsan": 90, "lisi": 78, "wangermazi": 39}
sor1 = sorted(js.items(), key=lambda x: x[1], reverse=False)
print(sor1)
turJson = [(js[i], i) for i in json]
sor2 = sorted(turJson, reverse=False)
print(sor2)
`ˋ
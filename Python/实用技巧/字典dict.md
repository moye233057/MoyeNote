## 一、反转字典
```
#方法一:
for k,v in myinfor.items():
     infor[v]=k
#方法二:
myinfor =  {"name":"qiwsir","site":"qiwsir.github.io","lang":"python"}
reverseDict = dict(zip(myinfor.values(),myinfor.keys()))
```

## 二、求字典值的平均值
```
js = {"zhangsan": 90, "lisi": 78, "wangermazi": 39}
lst = sum(list(js.values())) / len(js)
print(lst)
```

## 三、字典值的排序，利用sorted函数
```
js = {"zhangsan": 90, "lisi": 78, "wangermazi": 39}
# 方法一:
# 字典排序，reverse=False代表逆序
sor1 = sorted(js.items(), key=lambda x: x[1], reverse=False)
print(sor1)
# [('wangermazi', 39), ('lisi', 78), ('zhangsan', 90)]
# 方法二:
turJson = [(js[i], i) for i in js]
sor2 = sorted(turJson, reverse=False)
print(sor2)
```

## 四、利用字典统计可迭代对象的数量
```
lst = [1, 2, 3, 4, 5, 1, 1, 5, 3, 5, 2, 4]
count = {}
for num in lst:
    count[num] = count.get(num, 0) + 1
print(count)
```

## 五、两个字典相同键的值相减
```
# 例: 统计2022年出现，但2021年未出现的字母及其新增的次数
from collections import Counter
dic = {
    "2022": {"a": 3, "b": 2, "c": 2, "d": 2, "e": 3},
    "2021": {"a": 3, "b": 2, "c": 3, "d": 1, "f": 1},
}

res = dict(Counter(dic["2022"]) - Counter(dic["2021"]))
print(res)
# {'d': 1, 'e': 3}
```

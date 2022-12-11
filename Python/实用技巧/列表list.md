## 一、将数组中的元素进行类型转换
```
lst = list(map(type, lst))
type可以是int、str...,取决与数组中的数据类型
```

## 二、对两个不同长度的列表进行迭代操作
```
a = [1,2,3,4,5]
b = ["python","www.itdiffer.com","qiwsir"]
(1)
d = []
for x, y in zip(a, b)
    d.append(x+y)
(2)
length = len(a) if len(a)<len(b) else len(b)
for i in range(length):
    c.append(str(a[i]) + ":" + b[i])
```

## 三、list列表推导式
```
(1)循环平方
squares = [x**2 for x in range(1,10)]
(2)循环去除空格
mybag = [' glass',' apple','green leaf ']   #有的前面有空格，有的后面有空格
[one.strip() for one in mybag]
```

## 四、将列表中的第一个移到最后一位。
```
lst = [0,1,2,3,4,5]
last = lst.pop(0)
lst.append(last)
```

## 五、不保留原始顺序的列表去重
```
lst = [1,1,2,2,2,3,3,3,3]
lst = list(set(lst))
```

## 六、多维列表数据过滤特定条件的列表
```
# 例: 取出以字典为元素的列表中year为2022的值
year = 2022
data = [
    {
        "year": 2021,
        "word": "鼠标",
    },
    {
        "year": 2019,
        "num": "电话",
    },
    {
        "year": 2022,
        "num": "智能",
    },
    {
        "year": 2022,
        "num": "足球",
    },
    {
        "year": 2018,
        "num": "家电"
    },
]
new_data = list(filter(lambda x: x["year"] == year, data))
print(new_data)
```

## 求两个列表之间的相似度

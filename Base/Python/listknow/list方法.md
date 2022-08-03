# 一.将数组中的元素进行类型转换
lst = list(map(type, lst))
type可以是int、str...,取决与数组中的数据类型

# 二、对两个不同长度的列表进行迭代操作
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

# 三、list解析应用
(1)循环平方
squares = [x**2 for x in range(1,10)]
(2)循环去除空格
mybag = [' glass',' apple','green leaf ']   #有的前面有空格，有的后面有空格
[one.strip() for one in mybag]    
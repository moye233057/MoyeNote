# 练习一
1、产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数。<br>
2、如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出。<br>
3、对上面的列表元素从大到小排序

```python
# coding: utf-8
import random
lst = [random.randint(0, 100) for i in range(40)]
print("随机40个1到100整数:", lst)
num = len(lst)
total = sum(lst)
ava = round(total/num, 1)
# print(total, num, ava)
lowerAva = [x for x in lst if x < ava]
print("小于平均数的个数:", len(lowerAva))
sortlst = sorted(lst, reverse=True)
print("列表元素从大倒小排序", sortlst)

```

# 练习二
如果将一句话作为一个字符串，那么这个字符串中必然会有空格（这里仅讨论英文），比如"How are you."，但有的时候，会在两个单词之间多大一个空格。现在的任务是，如果一个字符串中有连续的两个空格，请把它删除。
```python
# 解法一:
# coding: utf-8
s = How are  you.
s = s.replace("  ", " ")
# 解法二:
# coding: utf-8
string = "I love  code."
str_lst = string.split(" ")
string = [s for s in str_lst if s != ""]
string = " ".join(string)
print(string)
```

## 练习三 斐波那契数列
a0 = 0                (n=0)
a1 = 1                (n=1)
a[n] = a[n-1] + a[n-2]  (n>=2)

```python
a, b = 0, 1
for i in range(4):
    a, b = b, a+b
```
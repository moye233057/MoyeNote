# -*-encoding:utf-8-*-
import string
import random

# 返回1~255之间的任意一个整数
r1 = random.randint(1, 255)
# print(r1)
# 从可迭代对象中随机连续取指定数量个
l1 = string.hexdigits
l2 = [1, 2, 3, 4, 5]
r2 = random.sample(l2, 5)
# print(r2)
# 返回0~1之间的随机浮点数
r3 = random.random()
# print(r3)
# 返回指定范围的浮点数
r4 = random.uniform(0.1, 0.5)
# print(r4)
# 返回序列中的随机元素
l3 = [1, 2, 3, 4]
r5 = random.choice(l3)
# print(r5)
# 将一个序列中的元素，随机打乱
random.shuffle(l3)
# print(l3)
# 从指定范围内,按指定基数递增的集合中,获取一个随机数.
# 相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数
r6 = random.randrange(10, 100, 2)
print(r6)

# 特殊用法:
1、每次运行固定随机输出可迭代对象中的值:
# 使用random.seed(0)设置随机种子，使用seed后random每次选取的随机数会固定。
例如：
import random
lst = ["华为", "苹果", "诺基亚", "OPPO", "小米"]
random.seed(0)
name = random.sample(lst, 1)
print(name)
这样会出现，每次运行都只固定输出华为/苹果...中的一个的现象
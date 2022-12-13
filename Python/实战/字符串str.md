## 一、检查字符串是否包含中文
```
def is_chinese(string):
    for ch in string:
        if ch.isalpha():
            return True
    return False
```

## 二、去除空格
```
s = "   aaaaaaaa  aaa  "
# 去除左右
s = s.strip()
# 去除左
s = s.lstrip()
# 去除右
s = s.rstrip()
```

## 三、字符串反转
```
s = "aabbcc"
s = s[::-1]
print(s)
```

## 四、变形词检查
```
# 想检查一对字符串中，其中一个字符串是否是另一个字符串的变形词
from collections import Counter
s1 = "listen"
s2 = "lstnie"
res = Counter(s1) == Counter(s2)
print(res)
```

## 五、生成四位验证码
```
import string
import random

length = 4
al = string.ascii_letters
di = string.digits
print(al, di)
li = random.sample(al + di, length)
print(li)
```
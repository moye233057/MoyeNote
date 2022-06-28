import string
import random
"""
str1 = string.ascii_letters    # 所有的字母大写和小写
str2 = string.digits           # 0 -9 数字
str3 = string.ascii_lowercase  # 小写字母
str4 = string.ascii_uppercase  # 大写字母 
random.choice(列表) # 随机在列表中选择一个元素
random.sample(列表，个数) # 随机在列表中选择固定个数的元素
"""
# 连续生成十个验证码
str1 = string.ascii_letters + string.digits
result = [''.join(random.sample(str1, 6)) for k in range(10)]
print(result)

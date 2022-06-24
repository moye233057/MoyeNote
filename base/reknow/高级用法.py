import re

# +至少一个
# \d数字
text1 = "Cats are smarter than dogs A23G4HFD567"


# 将匹配的数字乘以2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = re.findall('(?P<value>\d+)', text1)
print(s)
# print(re.sub('(?P<value>\d+)', double, text1))

# match从头开始匹配，search匹配整个字符串
# 前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符
# (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
# (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
# 后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
matchObj = re.match(r'(.*) are (.*?) .*', text1, re.M | re.I)
print(matchObj.group())
# t1 = re.match(r'(Cat).*', text1)
# t2 = re.search(r'(are).*', text1)
# print(t1.group())
# print(t2.group())

phone = "2004-959-559 # 这是一个国外电话号码"
# 去掉字符串#后面的注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
# 删除非数字的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

# 匹配第一位为大写字母，第二位为小写字母的字符子串，空格分隔后，第二个子串同第一个
# 第二个参数如果re.I 表示忽略大小写
pattern = re.compile(r'([A-Z]+[a-z]+)')
m = pattern.findall('Hello World Wide Web')
print(m)

import regex

string = '10010101000132165465101354654101'
str_re = '101'
print(regex.findall(str_re, string, overlapped=True))

# 返回身份证号码的省市和出生年份
sfz = "1102231990xxxxxxxx"
# ?P<>是将后面匹配的\d数据取一个组名，组名必须唯一不重复且没有特殊符号
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', sfz)
print(res.groupdict())

for w in content:
    if w >= u'\u4e00' and w <= u'\u9fa5':
        s += w
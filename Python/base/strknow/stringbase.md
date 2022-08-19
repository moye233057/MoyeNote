# -*-encoding:utf-8-*-

import string

# 所有大写+小写英文字母,str
s1 = string.ascii_letters
print(s1)
print(type(s1))
# 所有小写英文字母
s2 = string.ascii_lowercase
print(s2)
print(type(s2))
# 所有大写英文字母
s3 = string.ascii_uppercase
print(s3)
# 0-9
s4 = string.digits
# 标点符号
s5 = string.punctuation
print(s5)
# 0-9a-fA-F(十六进制字符)
s6 = string.hexdigits
print(s6)
# 0-9a-zA-Z标点符号(所有可打印字符)
s7 = string.printable
print(s7)
# 获取所有的八进制进制数字字符
s8 = string.octdigits
print(s8)


# 插入某个位置
# .insert(位置int，插入的东西str)
# .strip()可以去掉字符串中的空格
# .join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
#
# title() 返回字符串的标题版本，即单词首字母大写其余字母小写
# upper() 返回字符串全部大写的版本
# lower() 返回字符串的全部小写版本
# swapcase() 返回字符串大小写交换后的版本
# isalnum() 检查所有字符是否只有字母和数字
# isalpha() 检查字符串之中是否只有字母
# 前面加is可以变为判断方法
#
# find() 能帮助你找到第一个匹配的子字符串，没有找到则返回 -1
#
# z = s[::-1] #把输入的字符串s 进行倒序处理形成新的字符串z
#
# 格式化操作符：
# * %s 字符串（用 str() 函数进行字符串转换）
# * %r 字符串（用 repr() 函数进行字符串转换）
# * %d 十进制整数
# * %f 浮点数
# * %% 字符 %


# 判断一个字符是不是中文(范围为：['/u4e00'，'/u9fa5']。)
（1）
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False
print(is_Chinese("中文"))

（2）
str.isalpha()
中文的汉字会被 isalpha 判定为 True
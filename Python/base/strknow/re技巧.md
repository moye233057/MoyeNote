#### 1、匹配括号
```
# 匹配括号里面的内容
https://blog.csdn.net/weixin_43235307/article/details/120219815
# 匹配左括号前的内容
s = "水电费(1000元)1月30日前需要上交"
pat = re.compile(u'.*?(?=\\()')
res = re.match(pat, s)
print(res.group())
# 删除三种括号及里面的内容
text = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", '', text)
```

#### 2、只保留中文、英文和指定标点符号
```
con = "b0111111;1:cs<=7'b0000110;2:cs<=7'b1011011;endcase//选定一个数码管//在数码管上显示bs的值."
# 不想保留哪些就去掉哪些
cop = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9_.!+-=——,$%^，。？、~@#￥%……&*《》<>「」{}【】()/\\\[\]'\"]")
subcon = re.sub(cop, "", con)
print(subcon)
```

#### 3、字符串的标点符号
```
import string
text = 'adfadf,.,d.,sf.;,we;,f;d,fw;efw;elf;wle,fw;'
enbiaodian = string.punctuation
pat = r"[%s]+" % enbiaodian
res = re.sub(pat, "", text)  # 去除英文标点符号
print(res)
# pip install zhon
from zhon.hanzi import punctuation
text = "中文标点: ！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［"
zhbiaodian = punctuation
pat = r"[%s]+" % zhbiaodian
res = re.sub(pat, "", text)  # 去除标点符号
print(res)
```

#### 4、删除URL
```
text = "网址是:https://www.baidu.com,欢迎大家访问"
t1 = re.sub("http*\S+", " ", text)  # 删除http及之后
print(t1)
t2 = re.sub(r'http(.?)://(.*?)\.(net|com|cn|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)', '', text)
print(t2)
t3 = re.sub(r'www\.(.*?)\.(net|com|cn|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)', '', text)
print(t3)
```

#### 5、获取路径中包含的某个中间路径之后的内容
```
pat2 = re.compile('(?<=/yourmidpath).*$')
# 例如:
path = 'D:/test/yourmidpath/needpathorfile'
s1 = re.findall(pat2, path)
print(s1)
# 运行结果
# ['/needpathorfile']
```

#### 6、匹配任意多个空格
```
pat3 = re.compile(r' +')
s1 = '前        后'
s2 = re.sub(' +', ' ', s1)
或者
s2 = re.sub(r'\s+', ' ', s1)
print(s2)
# 运行结果:
# 前 后
```

#### 7、匹配字符串中头字母大写，第二个字母小写的字符子串
```
# 第二个参数如果re.I 表示忽略大小写
pattern = re.compile(r'([A-Z]+[a-z]+)')
m = pattern.findall('Hello World Wide Web')
print(m)
```

#### 8、匹配字符串中任意由两个英文字母和四个数字组成的字符串，并将英文和数字分开变为元组形式
```
pat = re.compile('([a-zA-Z]{2})([0-9]{4})')
# 例如：
s1 = 'sf2134dsfs32dsfdfs3421fsdf'
s2 = re.findall(pat, s1)
print(s2)
print(type(s2[0]))
# 运行结果:
# [('sf', '2134'), ('fs', '3421')]
# <class 'tuple'>
```

#### 9、匹配区域单位名称
```
data_list = ['北京市南瓜村', '陕西省西安市雁塔区大村', '西班牙镇街道', '北京市海淀区', '黑龙江省佳木斯市汤原县大村', '内蒙古自治区赤峰市',
            '贵州省黔南州贵定县', '新疆维吾尔自治区伊犁州奎屯市']
pat = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|镇|街)){1}'
for data in data_list:
    pattern = re.compile(pat)
    try:
        m = pattern.search(data)
        print(m.group())
    except:
        continue
```

#### 10、匹配字符串所有指定字符串，进行修改
```
import re

text1 = "Cats are smarter than dogs A23G4HFD567"

# 获取所有数字段
# ?P<>是将后面匹配的\d数据取一个组名，组名必须唯一不重复且没有特殊符号
s = re.findall('(?P<value>\d+)', text1)  # +至少一个，\d数字
print(s)

# 将匹配的数字乘以2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

print(re.sub('(?P<value>\d+)', double, text1))

# 返回身份证号码的省市和出生年份，并转化成{变量名:值}的字典
sfz = "1102231990xxxxxxxx"
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', sfz)
print(res.groupdict())
```

#### 11、输出字符串中所有101组成的列表
```
import regex

string = '10010101000132165465101354654101'
str_re = '101'
print(regex.findall(str_re, string, overlapped=True))
```

#### 12、登录注册模块
```
# 校验密码强度，不能特殊字符，长度限定8-10
pwd_pat = re.compile(^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$)
# 设定用户名规则，包含数字、字母、下划线并限制字符个数,例子是长度为3~15
uname_pat = re.compile('^[1-9a-z_-]{3,15}$')
```

#### 其他
```
删除提及。x = re.sub("@\S+", " ", x)
删除。URL 链接。x = re.sub("https*\S+", " ", x)
删除标签。x = re.sub("#\S+", " ", x)
删除记号和下一个字符。x = re.sub("\'\w+", '', x)
删除标点符号。x = re.sub('[%s]' % re.escape(string.punctuation), ' ', x)
删除数字。x = re.sub(r'\w*\d+\w*', '', x)
替换空格。x = re.sub('\s{2,}', " ", x)
# 校验E-Mail 地址
 email_pattern = '^[*#\u4e00-\u9fa5 a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$'
 [\\w!#$%&'*+/=?^_`{|}~-]+(?:\\.[\\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\\w](?:[\\w-]*[\\w])?\\.)+[\\w](?:[\\w-]*[\\w])?
# 校验身份证号码
# 15位：
 ^[1-9]\\d{7}((0\\d)|(1[0-2]))(([0|1|2]\\d)|3[0-1])\\d{3}$
# 18位：
 ^[1-9]\\d{5}[1-9]\\d{3}((0\\d)|(1[0-2]))(([0|1|2]\\d)|3[0-1])\\d{3}([0-9]|X)$
 “yyyy-mm-dd“ 格式的日期校验，已考虑平闰年。
 ^(?:(?!0000)[0-9]{4}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|1[02])-31)|(?:[0-9]{2}(?:0[48]|[2468][048]|[13579][26])|(?:0[48]|[2468][048]|[13579][26])00)-02-29)$
# 校验金额，精确到2位小数。
 ^[0-9]+(.[0-9]{2})?$
# 判断IE的版本
 ^.*MSIE [5-8](?:\\.[0-9]+)?(?!.*Trident\\/[5-9]\\.0).*$
# 校验IP-v4地址
 \\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b
# 校验IP-v6地址
 (([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))
# 提取URL链接
 ^(f|ht){1}(tp|tps):\\/\\/([\\w-]+\\.)+[\\w-]+(\\/[\\w- ./?%&=]*)?
# 文件路径及扩展名校验，以txt为例
 ^([a-zA-Z]\\:|\\\\)\\\\([^\\\\]+\\\\)*[^\\/:*?"<>|]+\\.txt(l)?$
# 提取Color Hex Codes（网页中的颜色代码）
 ^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$
# 提取网页图片
 \\< *[img][^\\\\>]*[src] *= *[\\"\\']{0,1}([^\\"\\'\\ >]*)
# 提取页面超链接
 (<a\\s*(?!.*\\brel=)[^>]*)(href="https?:\\/\\/)((?!(?:(?:www\\.)?'.implode('|(?:www\\.)?', $follow_list).'))[^"]+)"((?!.*\\brel=)[^>]*)(?:[^>]*)>
# 查找CSS属性
 ^\\s*[a-zA-Z\\-]+\\s*[:]{1}\\s[a-zA-Z0-9\\s.#]+[;]{1}
# 抽取注释
 <!--(.*?)-->
# 匹配HTML标签
 <\\/?\\w+((\\s+\\w+(\\s*=\\s*(?:".*?"|'.*?'|[\\^'">\\s]+))?)+\\s*|\\s*)\\/?>
```
# 一、创建字典
（1）直接创建
1、空字典：
dic = {}
2、有内容：dic = {"name":"zhangsan", "age": 14}
（2）元组构建
1、
name = (["first","Google"],["second","Yahoo"])      
website = dict(name)
2、
ad = dict(name = "qiwsir", age = 42)
（3）fromkeys
website = {}.fromkeys(("third","forth"),"facebook")
这种方法是重新建立一个dict。
需要提醒注意的是，在字典中的“键”，必须是**不可变**的数据类型；“值”可以是任意数据类型。
错误示范：
dd = {[1,2]:1}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

# 二、应用方法
# .item()
列表返回可遍历的(键, 值) 元组数组，例： [(),()...]
# .keys()
返回一个字典所有的键组成的数组，如dict = {'Name': 'Zara', 'Age': 7}，中的Name和Age,表现为['Name', 'Age']
# .values()
返回一个字典所有的值组成的数组，如dict = {'Name': 'Zara', 'Age': 7}, 中的Zara和7，表现为['Zara', 7]
# .zip()
同时遍历两个序列类型

# .copy()
复制一个新的字典，新字典与原字典的id不相同，即一个新的dict对象
需要注意的是：
***python只存储基本类型的数据，比如int,str，对于不是基础类型的，比如字典的值是列表，python不会在被复制的那个对象中重新存储，而是用引用的方式，指向原来的值。**
例如：
x = {"name":"qiwsir", "lang":["python", "java", "c"]}
y = x.copy()
y["lang"].remove("c")
结果：
print(y)
{'lang': ['python', 'java'], 'name': 'qiwsir'}
print(x)
{'lang': ['python', 'java'], 'name': 'qiwsir'}
即使y是由x.copy()而来的，修改y中的列表，也会导致x中的列表值发生改变。
但是修改值为非基础类型的，例如y中的name，就不会影响x中的name。
在编程语言中，把实现上面那种拷贝的方式称之为**浅拷贝**。顾名思义，没有解决深层次问题。
在python中，有一个“深拷贝”(deep copy)。不过，要用import来导入一个模块。
import copy
z = copy.deepcopy(x)

# .clear()
清空一个字典
如果要清空一个字典，还能够使用a = {}这种方法，但这种方法本质是将变量a转向了{}这个对象，原来的对象就变为了“垃圾”，会被python的
**垃圾自动回收机制**处理

# .get(key,defult)
得到字典中某个键的值，但它不会像dict[key]那样直接报错
如果只有key，.get找不到值会返回None,如果有defult，.get找不到值会返回defult
例如：
d = {"lang":"python"}
newd = d.get("name",'qiwsir')
print(newd)
qiwsir

# dict.setdefault(key, default)
如果键不存在于字典中，将会添加键并将值设为默认值。
往字典中的元素添加数据，我们首先要判断这个元素是否存在，不存在则创建一个默认值。
如果在循环里执行这个操作，每次迭代都需要判断一次，降低程序性能
 
对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值


# 三、格式化输出
（1）
city_code = {"suzhou":"0512", "tangshan":"0315", "hangzhou":"0571"}
"Suzhou is a beautiful city, its area code is %(suzhou)s" % city_code
（2）
temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name":"qiwsir", "lang":"python"}
temp % my
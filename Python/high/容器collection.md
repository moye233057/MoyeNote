# 一、defaultdict
（1）与dict类型不同，你不需要检查key是否存在，所以我们能这样做：
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

当你在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发keyError异常。 defaultdict允许我们用一个聪明的方式绕过这个问题。
问题：

some_dict = {}
some_dict['colours']['favourite'] = "yellow"

## 异常输出：KeyError: 'colours'
解决方案：

import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
可以用json.dumps打印出some_dict，例如：
import json
print(json.dumps(some_dict))


# 二、counter
Counter是一个计数器，它可以帮助我们针对某项数据进行计数。
比如
（1）计算每个人喜欢多少种颜色：
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

（2）统计一个文件。
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)


# 三、deque
deque提供了一个双端队列，你可以从头/尾两端添加或删除元素。
从collections中导入deque模块：
from collections import deque
创建一个deque对象：
d = deque()
限制这个列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出去(pop)。
d = deque(maxlen=30)
当你插入30条数据时，最左边一端的数据将从队列中删除。
从任一端扩展这个队列中的数据：
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)


# 四、命名元组namedtuple
一个元组是一个不可变的列表，你可以存储一个数据的序列，它和命名元组(namedtuples)非常像，但有几个关键的不同。
主要相似点是都不像列表，不能修改元组中的数据。
为了获取元组中的数据，需要使用整数作为索引：
man = ('Ali', 30)
print(man[0])
## 输出: Ali

namedtuples把元组变成一个针对简单任务的容器。你不必使用整数索引来访问一个namedtuples的数据。你可以像字典(dict)一样访问namedtuples，但namedtuples是不可变的。
from collections import namedtuple
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry)
## 输出: Animal(name='perry', age=31, type='cat')
print(perry.name)
## 输出: 'perry'

一个命名元组(namedtuple)有两个必需的参数。它们是元组名称和字段名称。
在上面的例子中，我们的元组名称是Animal，字段名称是'name'，'age'和'type'。

# 五、namedtuple的优点
让元组变得自文档了。你只要看一眼就很容易理解代码是做什么的。
不必使用整数索引来访问一个命名元组，这代码更易于维护。
namedtuple的每个实例没有对象字典，所以它们很轻量，与普通的元组比，并不需要更多的内存。这使得它们比字典更快。
然而，要记住它是一个元组，属性值在namedtuple中是不可变的


# 六、命名元组的用处
1、你应该使用命名元组来让代码自文档，它们**向后兼容**于普通的元组，这意味着你可以既使用整数索引，也可以使用名称来访问namedtuple：
from collections import namedtuple
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])
## 输出: perry

2、可以将一个命名元组转换为字典，方法如下：
from collections import namedtuple
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())
## 输出: OrderedDict([('name', 'Perry'), ('age', 31), ...


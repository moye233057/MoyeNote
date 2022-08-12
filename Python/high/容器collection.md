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
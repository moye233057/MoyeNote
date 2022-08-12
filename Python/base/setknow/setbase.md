一、set(集合)的特点。
set有类似dict的特点:可以用{}花括号来定义;
set的元素没有序列,也就是是非序列类型的数据;
set中的元素不可重复,类似dict的键.
set也有一点list的特点:有一种集合可以原处修改.

二、集合的方法。
（1）创建
1、用set方法创建
s1 = set('abccde')
print(s1)
set(['a', 'c', 'b', 'd'])
特点：元素不重复,排列顺序随意
     用set()建立起来的集合是可变集合，可变集合都是unhashable类型的。
2、用{}创建
s2 = {"python", 123}
注意：{}内必须有值，如果为{}，python会默认创建字典

(2)查找
1、由于集合是无序的，不能通过索引方法进行查找
2、使用list()和set()能够实现列表和集合之间的转换，想要查找set可以先转换为list

(3)增加集合元素
set.add()

(4)合并另一个集合
set.update(otherSet)

(5)随机去除集合中的元素
set.pop()
集合的.pop()不能有参数，否则会报错

(6)去除集合中的指定元素
set.remove(obj)
obj必须是集合中已有的元素，否则会报错

(7)去除集合中的指定元素,但不会报错
set.discard(obj)

(8)清空集合
set.clear()


三、不变的集合
以set()来建立集合，这种方式所创立的集合都是可原处修改的集合，或者说是可变的，也可以说是unhashable
还有一种集合，不能在原处修改。这种集合的创建方法是用**frozenset()**，顾名思义，这是一个被冻结的集合，当然是不能修改了，那么这种集合就是**hashable类型——可哈希**。

f_set = frozenset("qiwsir")
f_set.add('a') 会报错


四、集合的运算。
(1)元素与集合关系。
包含：'a' in set
(2)集合与集合关系。
1、等于 
    set1 == set2
2、不等于 
    set1 != set2
3、子集和超集
    判断set1是不是set2的子集：
    1.  set1 < set2
    返回True是子集
    2.  set1.issubset(set2)
    返回True是子集
    判断set1是不是set2的超集：
    set1.issuperset(set2)
4、并集
    1.set1 | set2
    2.set1.union(set2)
5、交集
    1.set1 & set2
    2.set1.intersetion(set2)
6、补集
    1.set1 - set2
    2.set1.difference(set2)
7、对称差集
    set1.symmetric_difference(set2)


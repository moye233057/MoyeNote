一、元组的基本概念
# 元组是用圆括号括起来的，其中的元素之间用逗号隔开。（都是英文半角）
# 元组中的元素类型是任意的python数据。
# tuple是一种序列类型的数据，这点上跟list/str类似。它的特点就是其中的元素不能更改，这点上跟list不同，倒是跟str类似；
# 它的元素又可以是任何类型的数据，这点上跟list相同，但不同于str。
# 如果一个元组中只有一个元素的时候，应该在该元素后面加一个半角的英文逗号。例如 tup = (1,)

二、元祖的几种运用例子:
# (1)变量赋值
t = 123,'abc',["come","here"]
print(t)
(123, 'abc', ['come', 'here'])
# (2)格式化输出
print( "I love %s, and I am a %s" % ('python', 'programmer'))
其中 %后面的括号就是元组
# (3)django中给CharFiled设置默认值：
type = models.CharField(verbose_name='草稿类型', default='0', max_length=32,
                        choices=(('0', '草稿'), ('1', '撰写模板'), ('2', '审核模板'), ('3', '构思')))
choices参数需要的就是元组

三、元组的用处：
1、Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
2、如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
3、Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。Dictionary key 必须是不可变的。Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
4、Tuples 可以用在字符串格式化中。
# 一个函数中，只要包含了yield语句，它就是生成器，也是迭代器。
# 迭代器
在迭代器中必有的方法__inter__()和next()

# 生成器
我们把含有yield语句的函数称作生成器。生成器是一种用普通函数语法定义的迭代器。
生成器：
my_generator = (x*x for x in range(4))
print(my_generator)
for i in my_generator:
    print(i)
列表解析式：
my_list = [x*x for x in range(4)]

生成器解析式是有很多用途的，在不少地方替代列表，是一个不错的选择。特别是针对大量值的时候
列表占内存较多，迭代器（生成器是迭代器）的优势就在于少占内存，因此无需将生成器（或者说是迭代器）实例化为一个列表，直接对其进行操作，方显示出其迭代的优势。
比如：
sum(i*i for i in range(10))

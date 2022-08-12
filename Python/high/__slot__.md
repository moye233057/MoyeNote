一、概念。
在Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性。它允许我们在运行时去设置任意的新属性。
这个字典浪费了很多内存。Python不能在对象创建时直接分配一个固定量的内存来保存所有的属性。因此如果你创建许多对象（我指的是成千上万个），它会消耗掉很多内存。

# __slots__
# 告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。
这里是一个使用与不使用__slots__的例子：

不使用 __slots__:
class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
    # ...
使用 __slots__:
class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
第二段代码会为你的内存减轻负担。



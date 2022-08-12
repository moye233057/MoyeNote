lambda表达式
lambda表达式是一行函数。
它们在其他语言中也被称为匿名函数。如果你不想在程序中对一个函数使用两次，你也许会想用lambda表达式，它们和普通的函数完全一样。

原型
    lambda 参数:操作(参数)
例子
    add = lambda x, y: x + y
    print(add(3, 5))
    # Output: 8
这还有一些lambda表达式的应用案例，可以在一些特殊情况下使用：

列表排序
    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    a.sort(key=lambda x: x[1])
    print(a)
    # Output: [(13, -3), (4, 1), (1, 2), (9, 10)]
列表并行排序
    data = zip(list1, list2)
    data.sort()
    list1, list2 = map(lambda t: list(t), zip(*data))
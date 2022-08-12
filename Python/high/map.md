Map
Map会将一个函数映射到一个输入列表的所有元素上。
规范
map(function_to_apply, list_of_inputs)
大多数时候，我们要把列表中所有元素一个个地传递给一个函数，并收集输出。
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
Map可以让我们用一种简单而漂亮得多的方式来实现。
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
大多数时候，我们使用匿名函数(lambdas)来配合map。
不仅用于一列表的输入， 我们甚至可以用于**一列表的函数**！
def multiply(x):
        return (x*x)
def add(x):
        return (x+x)
funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))
    # 译者注：上面print时，加了list转换，是为了python2/3的兼容性
    #        在python2中map直接返回列表，但在python3中返回迭代器
    #        因此为了兼容python3, 需要list转换一下

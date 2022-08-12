1、*args 和 **kwargs 主要用于函数定义。
可以将不定数量的参数传递给一个函数。

2、标准参数与*args、**kwargs在使用时的顺序
那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
some_func(fargs, *args, **kwargs)

3、*args 
是用来发送一个非键值对的可变数量的参数列表给一个函数。
例如：
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')


4、**kwargs 
允许你将不定长度的键值对, 作为参数传递给一个函数。
例如：
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="yasoob")
name == yasoob

5、*args和**args的用处：
1.最常见的用例是在写函数装饰器的时候
2.此外它也可以用来做猴子补丁(monkey patching)。
猴子补丁的意思是在程序运行时(runtime)修改某些代码。 
打个比方，你有一个类，里面有个叫get_info的函数会调用一个API并返回相应的数据。如果我们想测试它，可以把API调用替换成一些测试数据。
例如：
import someclass

def get_info(self, *args):
    return "Test data"

someclass.get_info = get_info
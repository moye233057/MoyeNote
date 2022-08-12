# 一、CTypes
Python中的ctypes模块可能是Python调用C方法中最简单的一种。
ctypes模块提供了和C语言兼容的数据类型和函数来加载dll文件，因此在调用时不需对源文件做任何的修改。

实现两数求和的C代码，保存为add.c
//sample C file to add 2 numbers - int and floats
#include <stdio.h>

int add_int(int, int);
float add_float(float, float);

int add_int(int num1, int num2){
    return num1 + num2;

}

float add_float(float num1, float num2){
    return num1 + num2;
}

接下来将C文件编译为.so文件(windows下为DLL)。下面操作会生成adder.so文件
#For Linux
$  gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c
#For Mac
$ gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c

现在在你的Python代码中来调用它
from ctypes import *

#load the shared object file
adder = CDLL('./adder.so')
#Find sum of integers
res_int = adder.add_int(4,5)
print "Sum of 4 and 5 = " + str(res_int)
#Find sum of floats
a = c_float(5.5)
b = c_float(4.1)
add_float = adder.add_float
add_float.restype = c_float
print "Sum of 5.5 and 4.1 = ", str(add_float(a, b))

输出如下:
Sum of 4 and 5 = 9
Sum of 5.5 and 4.1 =  9.60000038147


# 二、SWIG
SWIG是Simplified Wrapper and Interface Generator的缩写。是Python中调用C代码的另一种方法。在这个方法中，开发人员必须编写一个额外的接口文件来作为SWIG(终端工具)的入口。

Python开发者一般不会采用这种方法，因为大多数情况它会带来不必要的复杂。而当你有一个C/C++代码库需要被多种语言调用时，这将是个非常不错的选择。


# 三、Python/C API
Python/C API可能是被最广泛使用的方法。它不仅简单，而且可以在C代码中操作你的Python对象。

这种方法需要以特定的方式来编写C代码以供Python去调用它。所有的Python对象都被表示为一种叫做PyObject的结构体，并且Python.h头文件中提供了各种操作它的函数。

例如，如果PyObject表示为PyListType(列表类型)时，那么我们便可以使用PyList_Size()函数来获取该结构的长度，类似Python中的len(list)函数。大部分对Python原生对象的基础函数和操作在Python.h头文件中都能找到。

编写一个C扩展，添加所有元素到一个Python列表(所有元素都是数字)
来看一下我们要实现的效果，这里演示了用Python调用C扩展的代码
import addList
l = [1,2,3,4,5]
print "Sum of List - " + str(l) + " = " +  str(addList.add(l))


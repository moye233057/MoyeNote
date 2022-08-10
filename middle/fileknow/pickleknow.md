pickle是标准库中的一个模块，还有跟它完全一样的叫做cpickle，两者的区别就是后者更快。所以，下面操作中，不管是用import pickle，还是用import cpickle as pickle，在功能上都是一样的。

import pickle
integers = [1, 2, 3, 4, 5]
f = open("22901.dat", "wb")
pickle.dump(integers, f)
f.close()
用pickle.dump(integers, f)将数据integers保存到了文件22901.dat中。如果你要打开这个文件，看里面的内容，可能有点失望，但是，它对计算机是友好的。这个步骤，可以称之为将对象序列化。用到的方法是：

pickle.dump(obj,file[,protocol])

obj：序列化对象，上面的例子中是一个列表，它是基本类型，也可以序列化自己定义的类型。
file：一般情况下是要写入的文件。更广泛地可以理解为为拥有write()方法的对象，并且能接受字符串为为参数，所以，它还可以是一个StringIO对象，或者其它自定义满足条件的对象。
protocol：可选项。默认为False（或者说0），是以ASCII格式保存对象；如果设置为1或者True，则以压缩的二进制格式保存对象。
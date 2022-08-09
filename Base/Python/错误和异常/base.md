异常	描述
NameError	尝试访问一个没有申明的变量
ZeroDivisionError	除数为0
SyntaxError	语法错误
IndexError	索引超出序列范围
KeyError	请求一个不存在的字典关键字
IOError	输入输出错误（比如你要读的文件不存在）
AttributeError	尝试访问未知的对象属性

异常捕获：
try:
   pass
except NameError:
   pass
except SyntaxError:
   pass
else:  # 没有异常执行else
   pass
finally:  # 不管有没有异常都执行
   pass

assert 断言
assert是一句等价于布尔真的判定，发生异常就意味着表达式为假。
什么是使用断言的最佳时机？
防御性的编程
运行时对程序逻辑的检测
合约性检查（比如前置条件，后置条件）
程序中的常量
检查文档
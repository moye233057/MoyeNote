#__getatter__ 
作用：在查找不到属性的时候调用
class User:
    def __init__(name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info
    
    # 如果用User实例去查找不存在的属性，例如user.age,就会触发
    def __getatter__ (self, item):
        retrun "not found atter"
    
    #又比如User类的属性存放在一个字典中，想用实例.属性的方式访问info里的值
    # 如果用User实例去查找不存在的属性，例如user.age,就会触发
    def __getatter__ (self, item):
        retrun self.info[item]

#__getattribute__
比__getatter__更高级，无论是否存在要查找的属性，都会先进入__getattribute__
class User:
    def __init__(name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info
    
    def __getatter__ (self, item):
        retrun "not found atter"
    
    # 可以作为所有属性访问的入口，慎用
    def __getattribute__ (self, item):
        retrun “bobo”
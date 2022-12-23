# 一、概念
```
1、文本文件
  存储的是普通“字符”文本，默认unicode字符集，可以用记事本程序打开。但是，像word软件编辑的文档不是文本文件
2、二进制文件
  二进制文件把数据内容用“字节”进行存储，无法用记事本打开，必须使用专用软件解码。例如：MP4视频文件、MP3音频文件、JPG图片、doc文档等

```

# 二、open读入读出文件
```
f = open(filepath, 'r', encoding='utf-8')
模式	描述
r	以读方式打开文件，可读取文件信息。
w	以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容
a	以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
r+	以读写方式打开文件，可对文件进行读和写操作。
w+	消除文件内容，然后以读写方式打开文件。
a+	以读写方式打开文件，并把文件指针移到文件尾。
b	以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。

f.seek(0)
# 开始的偏移量，默认为0
# 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
# 可以用于写入文件之后，回到开头读取之前写入的内容
```

# 三、os
```
# -*-encoding:utf-8-*-
import os
env = os.environ


# 文件相关
os.rename(src, dest)  # 重命名文件或目录
os.stat(path)  # 返回文件的所有属性
os.remove(path)  # 删除指定文件
os.listdir(path)  # 返回path目录下的文件和目录列表

# 目录相关
os.mkdir(path)  # 创建目录
os.makedirs(path1/path2/path3/...)  # 递归创建
os.rmdir(path)  # 删除空目录
os.removedirs(path1/path2/...) # 删除多级目录
os.getcwd()  # 返回当前工作目录
os.chdir(path) # 把path设为当前工作目录
os.walk()  # 遍历目录树
os.sep  # 返回当前操作系统使用的路径分隔符

# 路径相关os.path
# os.path.abspath（path）取文件绝对路径的方法
# os.path.basename(abspath) 取文件名字
# os.path.dirname(abspath) 取文件上级路径
# os.pardir() 获取当前目录的父目录（上一级目录），以字符串形式显示目录名
# os.path.dirname(path) 去掉文件名，返回目录
## 文件相关
# 文件重命名
os.rename('', '') 
# 分离后缀名和文件名
print(os.path.splitext('hello.png'))
# 将目录名和文件名分离
print(os.path.split('/tmp/hello/python.jpg'))

```

# 四*、pickle序列化
```
pickle.dump(obj, file)  # obj是要被序列号的对象，file是存储的文件
pickle.load(file)  # 从file读取数据，反序列化成对象  
```

# 五、shutil模块
```
import shutil
# 复制文件或目录
shutil.copyfile("1.txt", "1_copy.txt")
shutil.copytree("movie/港台", "电影")  # 电影目录不存在时才能正常拷贝
shutil.copytree("movie/港台", "电影", ignore=shutil.ignore_patterns("*.txt", "*.html"))  # 拷贝港台目录下所有文件到电影目录中，但不拷贝后缀为txt和html的文件
# 压缩
shutil.make_archive("电影/gg", "zip", "movie/港台")

# zipfile
# 压缩
z1 = zipfile.ZipFile("a.zip", "w")
z1.write("1.txt")
z1.wirte("1.png")
z1.close()
# 解压缩
z2 = zipfile.ZipFile("a.zip", "r")
z2.extractall("a.zip")
```

# shelve实现字典形式写和读
```
# shelve模块也是标准库中的。
# 写入
import shelve
s = shelve.open("22901.db")
s["name"] = "www.itdiffer.com"
s["lang"] = "python"
s["pages"] = 1000
s["contents"] = {"first":"base knowledge","second":"day day up"}
s.close()
# 读出
s = shelve.open("22901.db")
name = s["name"]
print(name)
www.itdiffer.com
contents = s["contents"]
print(contents)
{'second': 'day day up', 'first': 'base knowledge'}

# 当然，也可以用for语句来读：
for k in s:
    print k, s[k]
不管是写，还是读，都似乎要简化了。所建立的对象s，就如同字典一样，可称之为类字典对象。

当试图修改一个已有键的值时，没有报错，但是并没有修改成功。要填平这个坑，需要这样做：
f = shelve.open("22901.db", writeback=True)    #多一个参数True
f["author"].append("Hetz")
f["author"]                #没有坑了
['qiwsir', 'Hetz']
f.close()
```

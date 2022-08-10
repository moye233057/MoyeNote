shelve模块也是标准库中的。先看一下基本操作：写入和读取

import shelve
s = shelve.open("22901.db")
s["name"] = "www.itdiffer.com"
s["lang"] = "python"
s["pages"] = 1000
s["contents"] = {"first":"base knowledge","second":"day day up"}
s.close()
以上完成了数据写入的过程。其实，这更接近数据库的样式了。下面是读取。

s = shelve.open("22901.db")
name = s["name"]
print(name)
www.itdiffer.com
contents = s["contents"]
print(contents)
{'second': 'day day up', 'first': 'base knowledge'}

当然，也可以用for语句来读：
for k in s:
    print k, s[k]
不管是写，还是读，都似乎要简化了。所建立的对象s，就如同字典一样，可称之为类字典对象。

当试图修改一个已有键的值时，没有报错，但是并没有修改成功。要填平这个坑，需要这样做：

f = shelve.open("22901.db", writeback=True)    #多一个参数True
f["author"].append("Hetz")
f["author"]                #没有坑了
['qiwsir', 'Hetz']
f.close()
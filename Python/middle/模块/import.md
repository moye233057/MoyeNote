## 一、该奶奶
```
"""
当导入一个模块时，模块中的代码都会被执行，不过，如果再次导入这个模块，则不会再执行
一个模块无论导入多少次，这个模块在整个解释器进程内有且仅有一个实例对象
"""
```

## 动态导入模块
```
# 不建议使用
s = "math"
m = __import__(s)
m.pi
# 建议使用
import importlib
a = importlib.import_module("math")
print(a.pi)
# 重新加载
importlib.reload("math")
```
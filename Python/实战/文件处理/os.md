```
# (1)获取一个目录下面的全部目标文件
path = "./data"
# 1、一个目录下全是目标文件
filelst = os.listdir(path)
# 2、一个目录下不仅包含目标文件,同时包含文件夹，文件夹里面也有目标文件
    for filepath, dirnames, filenames in os.walk(pdfPath):
        for filename in filenames:
            # 假如需要特定扩展名的文件
            # if filename.split(".")[-1] == "pdf":
                file = os.path.join(filepath, filename)
                filelst.append(file.replace("\\", "/"))
# (2)获取一个路径的文件名
path = "./data/pic/1.png"
imgname = os.path.basename(path)
print(imgname)
# (3)判断一个文件是否存在
os.path.exists(path)
```

```
# (4)递归打印所有目录和文件
import os
allfiles = []
def getAllFiles(path, level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            getAllFiles(path, level+1)
        allfiles.append("\t"*level+filepath)
getAllFiles("", 0)
for f in reversed(allfiles):
    print(f)

```

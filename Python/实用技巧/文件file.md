## 一、os
```
path = "./data"
# 一个目录下全是目标文件
filelst = os.listdir(path)
# 一个目录下不仅包含目标文件,同时包含文件夹，文件夹里面也有目标文件
    for filepath, dirnames, filenames in os.walk(pdfPath):
        for filename in filenames:
            # 假如需要特定扩展名的文件
            # if filename.split(".")[-1] == "pdf":
                file = os.path.join(filepath, filename)
                filelst.append(file.replace("\\", "/"))
```

## 二、
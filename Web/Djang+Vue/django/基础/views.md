## 保存前端传来的文件
```
def savefile(file, save_path):
    f = open(save_path, 'wb')
    for chunk in file.chunks():
        f.write(chunk)
    f.close()
```

## 获取前端传递的多个文件
```
from django.http import JsonResponse
try:
    files = request.FILES.getlist("file", None)
    if len(files) == 0:
        data = {"msg": "收到文件个数为0"}
        return JsonResponse(data)
except:
    data = {"msg": "收不到文件"}
    return JsonResponse(data)

```


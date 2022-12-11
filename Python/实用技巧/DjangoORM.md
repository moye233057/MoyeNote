## 一、可变的与操作
```
# 使用可变的关键字参数字典
# 例: 查询学生类中性别、年龄、班级等不定条件的学生
sex = ""
age = ""
cla = ""
kwarys = {
    "sex": sex,
    "age" = age,
    "cla" = cla, 
}
stus = Student.objects.filter(**kwarg)
```

## 二、可变的或操作
```
# 思路是先把尽可能获取需要的所有数据，再根据条件一个个查询
# 例: 查询学生昵称包含a或b或c或其他字母的
words = ["a", "b", "c"]
stus = Student.objects.all()
ids = []
res = []
for word in words:
    oneWordStu = stus.filter(nickname__icontains=word)
    if len(oneWordStu) > 0:
        for stu in oneWordStu:
            if stu.id not in ids:
                ids.append(stu.id)
                res.append({
                    "id": stu.id,
                    "name": stu.name,
                    "title": stu.title,
                })
```

## 如果A对B设置了多对多关系，那么它们可以互相查询
```
例:
class A:
    b
```
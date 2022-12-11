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

## 三、如果A对B设置了多对多关系，那么它们可以互相查询
```
class B:
    name = models.CharField(max_length=32)

class A:
    b = models.ManyToManyField('B', blank=True)

# A -> B
a = A.objects.get(id=1)
bs = a.b.all()
# B -> A
name = "智能"
b = B.objects.get(name_=name)
as = b.a_set.all() 
```
## 四、ManyToMany属性的修改
```
a = A.objects.get(id=1)
b1 = B.objects.create(name="1")
a.b.add(b1)
b2 = B.objects.create(name="2")
b3 = B.objects.create(name="3")
lst = [b2, b3]
# 多个添加可以用可变参数形式，列表内是关联的模型的实例
a.b.add(*lst)
a.save()
```

## 五、ManyToMany属性清空并重新写入
```
b4 = B.objects.create(name="4")
b5 = B.objects.create(name="5")
new_bs = [b4, b5]
a = A.objects.get(id=1)
a.b.clear()
a.b.add(*new_bs)
```

## 六、账号对每一个文章最多点赞一次的功能实现
```
# 账号模型下有一个like属性，通过多对多关联到文章模型
# 根据登录的账号获取用户名得到该账号实例
username = "zhangsan"
account, res = Account.objects.get(username=username)
id = request.POST.get("id")
# 通过文章id得到要点赞文章实例
try:
    investment = Investment.objects.get(id=id)
except:
    return responseJson(404, True, None, "找不到该投资项目")
# 查找账号下的like属性是否已关联该文章，如果关联说明已点赞，需要去除关联(取消点赞)
invests = account.like_investments.filter(id=id)
if len(invests) > 0:
    account.like_investments.remove(investment)
else:
    account.like_investments.add(investment)
```
# 一、基础
```
(1)创建
obj = modelname.objects.crate(**kwargs)
obj, res = modelname.objects.get_or_create(**kwargs)
update_or_create(**kwargs, default={})  找到更新,如果没有找到创建defaults={} 中的数据

(2)删除
modelname.objects.get().delete()

(3)修改
# 修改方式1 update()
models.Book.objects.filter(id=1).update(price=3)
# 修改方式2 obj.save() 
book_obj=models.Book.objects.get(id=1)
book_obj.price=5
book_obj.save()

(4)查询
1.基本查询
modelname.objects.all()
modelname.objects.get()
modelname.objects.filter(Field__{})
2.范围查询
 __lt:小于
 __lte:小于等于
 __gt:大于
 __gte:大于等于
 __in:符合集合条件的数据
 __icontain:包含，模糊匹配，忽略大小写
 __contain:包含，模糊匹配，精确大小写
 __isnull:是否为空
 __range：范围
 __regex：正则区分大小写
 __iregex：正则不区分大小写
 __date：日期
 __year：年份
 __month：月份
 __day：日
 __week_day:工作日
 __hour:小时
 __minute:分钟
 __second:秒

 3.拓展查询
 .first() 第一个
 .last() 最后一个
 .exclude() 不包含
 .distinct() 去重
 .order_by() 排序
```


# 二、例子
## 1、django文本精确长度查询
```
 模型(表)存储的文本太长时，如果直接用=进行查询，即使匹配文本的内容、类型、长度都一样还是会查询不出来
 使title和content都确认对应上了，返回结果还是为空
 例如：mod = mods.objects.filter(title=title, content=content)
 解决办法，content不用内容改为用内容长度进行正则匹配，title作为第一查询条件缩小范围
 par1 = r'^.{%s}$' % (len(savetext))  # {}内是要匹配的文本长度
 mods = Mod.objects.filter(title=title, content__iregex=par1)
 iregex：大小写不敏感的判断的判断某字段的值是否满足正则表达式的条件。
```

## 2、多条件或查询
```
#一般或运行的想法是利用“|” 或者 “or”
# 但是django需要用到Q语句和“|”进行结合
# 例如：
mods = Mod.objects.filter(Q(title=title)|Q(content=content)) 

# 可变的或操作
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

## 3、外键查询
```
 如果一个模型的字段通过OneToOneField、ForeignKey、ManyToManyField与另一个模型关联起来
 可以通过模型字段__关联模型字段来跨表查询
 例如：mods表通过user字段用OneToOneField与User表进行关联，而User中有username字段，就可以通过
 mods = Mod.objects.filter(user__username='张三')
 意思是：查找User表中username为张三关联的mods表
```

## 4、限定集合查询
```
 如果能够确定查询内容的范围，一般是一个列表，可以用__in进行查询
 例如要查找id为5,6,7的数据，可以这样查：
 ids = [5,6,7]
 mods = Mod.objects.filter(id__in=ids)
```

## 5、模糊查询
```
 如果想要查询表中所有某个字段包含某个内容的数据，可以用__icontains,i代表不区分大小写
 例如：
 mods = Mod.objects.filter(title__icontains='方法')
```

## 6、排除查询
```
 如果想要查询排除掉不符合条件后的数据，可以用exclude
 例如：
 查找用户名为zhangsan但是标题不包含李四的数据
 mods = Mod.objects.filter(username='zhangsan').exclude(title='李四')
```

## 7、动态查询
```
 如果想要查询的字段和内容是动态的，可以将字段和内容用键值对的形式放在字典中，再用**dict形式查询
 例如：
 kwargs = {'title': '测试标题', 'content': '科技'}
 mods = Mod.objects.filter(**kwarg)
```

## 8、时间范围查询
```
 如果要查询的字段的类型为models.DateTimeField,可以通过字段__gt大于/gt大于等于/lt小于/lte小于等于
 对于时间，越晚越大，例如：2022-06-30大于2022-06-28。
 例如：
 1、查询不超过一天的记录:
 start = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
 mods = Mod.objects.filter(recordData__gt=start)
 timezon.now()获取当前时间，在用timedelta减一天，最后查询记录日期大于昨天的数据
 2、查询一段时间内的记录：
 例如10天~30天
 day30 = (datetime.datetime.now() + datetime.timedelta(days=-30)).date()
 day10 = (datetime.datetime.now() + datetime.timedelta(days=-10)).date()
 mods = Mod.objects.filter(recordData__lte=day10, recordData__gte=day30)      
```


## 9.如果A对B设置了多对多关系，那么它们可以互相查询
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

## 10.ManyToMany属性的修改
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

## 11.ManyToMany属性清空并重新写入
```
b4 = B.objects.create(name="4")
b5 = B.objects.create(name="5")
new_bs = [b4, b5]
a = A.objects.get(id=1)
a.b.clear()
a.b.add(*new_bs)
```

## 12.账号对每一个文章最多点赞一次的功能实现
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
# 一、django文本精确长度查询
# 模型(表)存储的文本太长时，如果直接用=进行查询，即使匹配文本的内容、类型、长度都一样还是会查询不出来
# 使title和content都确认对应上了，返回结果还是为空
# 例如：mod = mods.objects.filter(title=title, content=content)
# 解决办法，content不用内容改为用内容长度进行正则匹配，title作为第一查询条件缩小范围
# par1 = r'^.{%s}$' % (len(savetext))  # {}内是要匹配的文本长度
# mods = Mod.objects.filter(title=title, content__iregex=par1)
# iregex：大小写不敏感的判断的判断某字段的值是否满足正则表达式的条件。

# 二、多条件或查询
# 一般或运行的想法是利用“|” 或者 “or”
# 但是django需要用到Q语句和“|”进行结合
# 例如：
# mods = Mod.objects.filter(Q(title=title)|Q(content=content)) 

# 三、外键查询
# 如果一个模型的字段通过OneToOneField、ForeignKey、ManyToManyField与另一个模型关联起来
# 可以通过模型字段__关联模型字段来跨表查询
# 例如：mods表通过user字段用OneToOneField与User表进行关联，而User中有username字段，就可以通过
# mods = Mod.objects.filter(user__username='张三')
# 意思是：查找User表中username为张三关联的mods表

# 四、限定集合查询
# 如果能够确定查询内容的范围，一般是一个列表，可以用__in进行查询
# 例如要查找id为5,6,7的数据，可以这样查：
# ids = [5,6,7]
# mods = Mod.objects.filter(id__in=ids)

# 五、模糊查询
# 如果想要查询表中所有某个字段包含某个内容的数据，可以用__icontains,i代表不区分大小写
# 例如：
# mods = Mod.objects.filter(title__icontains='方法')

# 六、排除查询
# 如果想要查询排除掉不符合条件后的数据，可以用ex
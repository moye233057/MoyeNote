# 一、django文本精确长度查询
# 模型(表)存储的文本太长时，如果直接用=进行查询，即使匹配文本的内容、类型、长度都一样还是会查询不出来
# 例如：ADdraft = AuditDraft.objects.filter(title=title, content=content)
# 即使title和content都确认对应上了，返回结果还是为空
# 解决办法，content不用内容改为用内容长度进行匹配，title作为第一查询条件缩小范围
# 最终得到: ADdraft = AuditDraft.objects.filter(title=title, content__iregex=par1)
# iregex：大小写不敏感的判断的判断某字段的值是否满足正则表达式的条件。par1 = r'^.{%s}$' % (len(savetext)) {}内是要匹配的文本长度

# 二、多条件或查询
#


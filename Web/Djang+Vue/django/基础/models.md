# 一、创建模型
class clsname(model.Model):
    ...
可用字段类型：
# 1、字符串类（以下都是在数据库中本质都是字符串数据类型，此类字段只是在Django自带的admin中生效）
name=models.CharField(max_length=32)
    EmailField(CharField)：
    IPAddressField(Field)
    URLField(CharField)
    SlugField(CharField)
    UUIDField(Field)
    FilePathField(Field)
    FileField(Field)
    ImageField(FileField)
    CommaSeparatedIntegerField(CharField)

models.CharField  对应的是MySQL的varchar数据类型
char 和 varchar的区别 :
char和varchar的共同点是存储数据的长度，不能 超过max_length限制，
不同点是varchar根据数据实际长度存储，char按指定max_length（）存储数据；所有前者更节省硬盘空间；

# 2、时间字段
models.DateTimeField(null=True)
date=models.DateField()

# 3、数字字段
(max_digits=30,decimal_places=10)总长度30小数位 10位）
数字：
num = models.IntegerField()
num = models.FloatField() 浮点
price=models.DecimalField(max_digits=8,decimal_places=3) 精确浮点
 

# 4、枚举字段
 choice=(
        (1,'男人'),
        (2,'女人'),
        (3,'其他')
    )
lover=models.IntegerField(choices=choice) #枚举类型
 
扩展
在数据库存储枚举类型，比外键有什么优势？
1、无需连表查询性能低，省硬盘空间(选项不固定时用外键)
2、在modle文件里不能动态增加（选项一成不变用Django的choice）

db_index = True 表示设置索引
unique(唯一的意思) = True 设置唯一索引

# 其他字段
联合唯一索引
class Meta:
unique_together = (
 ('email','ctime'),
)
联合索引（不做限制）
index_together = (
('email','ctime'),
)
ManyToManyField(RelatedField)  #多对多操作

# 数据库级别生效
AutoField(Field)
        - int自增列，必须填入参数 primary_key=True

BigAutoField(AutoField)
    - bigint自增列，必须填入参数 primary_key=True

    注：当model中如果没有自增列，则自动会创建一个列名为id的列
    from django.db import models

    class UserInfo(models.Model):
        # 自动创建一个列名为id的且为自增的整数列
        username = models.CharField(max_length=32)

    class Group(models.Model):
        # 自定义自增列
        nid = models.AutoField(primary_key=True)
        name = models.CharField(max_length=32)

SmallIntegerField(IntegerField):
    - 小整数 -32768 ～ 32767

PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
    - 正小整数 0 ～ 32767
IntegerField(Field)
    - 整数列(有符号的) -2147483648 ～ 2147483647

PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
    - 正整数 0 ～ 2147483647

BigIntegerField(IntegerField):
    - 长整型(有符号的) -9223372036854775808 ～ 9223372036854775807

自定义无符号整数字段

    class UnsignedIntegerField(models.IntegerField):
        def db_type(self, connection):
            return 'integer UNSIGNED'

    PS: 返回值为字段在数据库中的属性，Django字段默认的值为：
        'AutoField': 'integer AUTO_INCREMENT',
        'BigAutoField': 'bigint AUTO_INCREMENT',
        'BinaryField': 'longblob',
        'BooleanField': 'bool',
        'CharField': 'varchar(%(max_length)s)',
        'CommaSeparatedIntegerField': 'varchar(%(max_length)s)',
        'DateField': 'date',
        'DateTimeField': 'datetime',
        'DecimalField': 'numeric(%(max_digits)s, %(decimal_places)s)',
        'DurationField': 'bigint',
        'FileField': 'varchar(%(max_length)s)',
        'FilePathField': 'varchar(%(max_length)s)',
        'FloatField': 'double precision',
        'IntegerField': 'integer',
        'BigIntegerField': 'bigint',
        'IPAddressField': 'char(15)',
        'GenericIPAddressField': 'char(39)',
        'NullBooleanField': 'bool',
        'OneToOneField': 'integer',
        'PositiveIntegerField': 'integer UNSIGNED',
        'PositiveSmallIntegerField': 'smallint UNSIGNED',
        'SlugField': 'varchar(%(max_length)s)',
        'SmallIntegerField': 'smallint',
        'TextField': 'longtext',
        'TimeField': 'time',
        'UUIDField': 'char(32)',

BooleanField(Field)
    - 布尔值类型

NullBooleanField(Field):
    - 可以为空的布尔值

CharField(Field)
    - 字符类型
    - 必须提供max_length参数， max_length表示字符长度

TextField(Field)
    - 文本类型

EmailField(CharField)：
    - 字符串类型，Django Admin以及ModelForm中提供验证机制

IPAddressField(Field)
    - 字符串类型，Django Admin以及ModelForm中提供验证 IPV4 机制

GenericIPAddressField(Field)
    - 字符串类型，Django Admin以及ModelForm中提供验证 Ipv4和Ipv6
    - 参数：
        protocol，用于指定Ipv4或Ipv6， 'both',"ipv4","ipv6"
        unpack_ipv4， 如果指定为True，则输入::ffff:192.0.2.1时候，可解析为192.0.2.1，开启刺功能，需要protocol="both"

URLField(CharField)
    - 字符串类型，Django Admin以及ModelForm中提供验证 URL

SlugField(CharField)
    - 字符串类型，Django Admin以及ModelForm中提供验证支持 字母、数字、下划线、连接符（减号）

CommaSeparatedIntegerField(CharField)
    - 字符串类型，格式必须为逗号分割的数字

UUIDField(Field)
    - 字符串类型，Django Admin以及ModelForm中提供对UUID格式的验证

FilePathField(Field)
    - 字符串，Django Admin以及ModelForm中提供读取文件夹下文件的功能
    - 参数：
            path,                      文件夹路径
            match=None,                正则匹配
            recursive=False,           递归下面的文件夹
            allow_files=True,          允许文件
            allow_folders=False,       允许文件夹

FileField(Field)
    - 字符串，路径保存在数据库，文件上传到指定目录
    - 参数：
        upload_to = ""      上传文件的保存路径
        storage = None      存储组件，默认django.core.files.storage.FileSystemStorage

ImageField(FileField)
    - 字符串，路径保存在数据库，文件上传到指定目录
    - 参数：
        upload_to = ""      上传文件的保存路径
        storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
        width_field=None,   上传图片的高度保存的数据库字段名（字符串）
        height_field=None   上传图片的宽度保存的数据库字段名（字符串）

DateTimeField(DateField)
    - 日期+时间格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]

DateField(DateTimeCheckMixin, Field)
    - 日期格式      YYYY-MM-DD

TimeField(DateTimeCheckMixin, Field)
    - 时间格式      HH:MM[:ss[.uuuuuu]]

DurationField(Field)
    - 长整数，时间间隔，数据库中按照bigint存储，ORM中获取的值为datetime.timedelta类型

FloatField(Field)
    - 浮点型

DecimalField(Field)
    - 10进制小数
    - 参数：
        max_digits，小数总长度
        decimal_places，小数位长度

BinaryField(Field)
    - 二进制类型

# 2、Django admin级别生效
针对 dango_admin生效的参数（正则匹配）
blanke (是否为空)
editable=False 是否允许编辑
help_text="提示信息"提示信息
choices=choice 提供下拉框
error_messages="错误信息" 错误信息
validators  自定义错误验证（列表类型），从而定制想要的验证规则


# 3、Django class Meta
  1.abstract = True  #将这个类设置为抽象类，加入这个设置后，在迁移的时候不会创建表
                      这样设置是为了创建用于把字段继承给子类的类
  2.db_table = "name"  #设置当前表在数据库存储的表名
  3.verbase_name = "name"  #设置当前表在admin后台的显示名称
  4.ordering = ["fieldname"]  #告诉Django模型对象返回的记录结果集是按照哪个字段排序的
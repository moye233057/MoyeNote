一、基础概念
序列化。序列化器会把模型对象转换成字典，经过response以后变成json字符串
反序列化。把客户端发送过来的数据，经过resquest以后变成字典，序列化器可以把字典转换成模型
反序列化。完成数据校验功能。

二、导入序列化器
from rest_framework import serializers
Serializer      序列化器基类，drf中所有的序列化器类都必须继承于Serializer
ModelSerializer 模型序列化器基类，是序列化器基类的子类，在工作中，除了Serializer基类以外，最常用的序列化器类基类

三、序列化器的设计
模板:
class ModelNameSerializer(serializers.ModelSerializer):
    #针对用户名这种唯一值，字符串
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=Account.objects.all(), message='用户已经存在')])
    #时间数据，对存储的值格式转换，且只能读取，不能修改
    last_login_time = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    
    #手机验证码，设置最大长度及用专门的方法进行校验
    mobile = serializers.CharField(required=True, max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param mobile:
        :return:
        """
        # 手机是否注册
        if Account.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('手机号码已经注册')
        pattern = re.compile(r'^(13[0-9]|14[0|5|6|7|9]|15[0|1|2|3|5|6|7|8|9]|'
                             r'16[2|5|6|7]|17[0|1|2|3|5|6|7|8]|18[0-9]|'
                             r'19[1|3|5|6|7|8|9])\d{8}$')
        # 验证手机号码合法
        if not re.match(pattern, mobile):
            raise serializers.ValidationError('手机号码格式错误')

        # 验证码发送频率
        one_minute_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minute_age, mobile=mobile).count():
            raise serializers.ValidationError('请一分钟后再次发送')

        return mobile

    # 用方法对字段进行预处理
    casebrief = SerializerMethodField(read_only=True)
    def get_casebrief(self, obj):
        return obj.casebrief.replace('<p>', '').replace('</p>', '')

    # 外键属性的序列化方法
    secondpdftype = serializers.SerializerMethodField()
    def get_secondpdftype(self, obj):
        fd = obj.secondpdftype.all()  # obj是该模型的对象
        # 调用上边定义的外键序列化器序列化（相当于序列化了两次）
        jon = SecondPdfTypeSerializer(instance=fd, many=True)
        return jon.data

    class Meta:
        model = Account
        fields = '__all__'



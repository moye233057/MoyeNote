序列化。序列化器会把模型对象转换成字典，经过response以后变成json字符串
反序列化。把客户端发送过来的数据，经过resquest以后变成字典，序列化器可以把字典转换成模型
反序列化。完成数据校验功能。

导入序列化器
from rest_framework import serializers
Serializer      序列化器基类，drf中所有的序列化器类都必须继承于Serializer
ModelSerializer 模型序列化器基类，是序列化器基类的子类，在工作中，除了Serializer基类以外，最常用的序列化器类基类
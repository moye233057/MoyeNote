python:3.6.5
django 3.1.7

创建Django项目目录
pip uninstall django(d无论大小写，包都是全小写名字)
django-admin startproject mainproject
python manage.py startapp firstWEB(一定要在manage.py下的目录才能运行)

运行Django项目
python manage.py runserver

model注册创建
在setting中注册
创建迁移文件
python manage.py makemigrations
迁移到数据库
python manage.py migrate
创建超级管理员
在管理员页面中管理model
在funtion中把model导进来赋给变量
传到字典中
再到html中将字典显现出来
python:3.6.5
django 3.1.7

# 创建Django项目目录
pip uninstall django(d无论大小写，包都是全小写名字)
django-admin startproject mainproject
python manage.py startapp firstWEB(一定要在manage.py下的目录才能运行)

# 运行Django项目
python manage.py runserver

# 创建迁移文件
python manage.py makemigrations
# 迁移到数据库
python manage.py migrate
# 只记录变化，不提交数据库操作
python manage.py migrate --fake    
# 检查DB中已经创建完毕的表结构，生成model.py
python manage.py inspectdb > models.py 
# 创建超级管理员

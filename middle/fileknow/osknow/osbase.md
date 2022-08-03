# -*-encoding:utf-8-*-
import os
env = os.environ

## 目录相关
# os.mkdir('baseknow')  创建目录
# os.makedirs('./baseknow/osknow/')  递归创建
# os.rmdir('')  删除目录OS
## 文件路径相关
# os.chdir(path) 改变当前工作路径为指定工作路径
# os.path.abspath（path）取文件绝对路径的方法
# os.path.basename(abspath) 取文件名字
# os.path.dirname(abspath) 取文件上级路径
# os.pardir() 获取当前目录的父目录（上一级目录），以字符串形式显示目录名
# os.path.dirname(path) 去掉文件名，返回目录
## 文件相关
# 文件重命名
os.rename('', '') 
# 分离后缀名和文件名
print(os.path.splitext('hello.png'))
# 将目录名和文件名分离
print(os.path.split('/tmp/hello/python.jpg'))
# 查看文件状态
os.stat

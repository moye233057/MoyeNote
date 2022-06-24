# -*-encoding:utf-8-*-
import os

env = os.environ
print(env)
abspath = os.path.abspath('es.py')
print(abspath)
basename = os.path.basename(abspath)
dirname = os.path.dirname(abspath)
print('___')
print(basename)
print(dirname)
# 文件、目录相关
#   创建目录/删除目录
# os.mkdir('baseknow')  ##创建目录
# os.makedirs('./baseknow/osknow/')  ##递归创建
# os.rmdir('')  ##删除目录
# 文件重命名
# os.rename('', '')
# 分离后缀名和文件名
print(os.path.splitext('hello.png'))
# 将目录名和文件名分离
print(os.path.split('/tmp/hello/python.jpg'))


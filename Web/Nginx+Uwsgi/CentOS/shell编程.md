 # 一、脚本的执行方式
 # (1)第一种:采用bash或sh+脚本的相对路径或绝对路径(不用赋予脚本+x权限)
    1.sh+脚本的相对路径
    sh ./hellow.sh
    2.sh+脚本的绝对路径
    sh /home/user/hellow.sh
    3.bash+脚本的相对路径
    bash ./hellow.sh
    4.bash+脚本的绝对路径
    bash /home/user/hellow.sh
# (2)第二种：采用输入脚本的绝对路径或相对路径来执行脚本(必须具有可执行权限+x)
    1.赋予hellow.sh +x权限
    chmod +x hellow.sh
    2.相对路径
    cd /home/user
    ./hellow.sh
    3.绝对路径
    /home/user/hellow.sh
# (3)第三种：在脚本的路径前加上"."或者source
    1. source hellow.sh  source是shell里面的内置命令
    2. . hellow.sh   


# 二、如何在ubuntu(Linux)中设置一个自动化脚本
# (1)创建一个脚本文件.sh
# (2)写入脚本文件，以复制文件为例:
```shell
#!/bin/bash
#设置环境变量
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
#复制项目
sudo cp -r /home/trizhi2/zhangshiju/patentinfer /home/trizhi2/zhangshiju/oldproject/tuiliold/
#修改复制后的项目名称
sudo mv /home/trizhi2/zhangshiju/oldproject/tuiliold/patentinfer /home/trizhi2/zhangshiju/oldproject/tuiliold/patentinfernew
#判断是否备份成功        
if [ $? -ne 0 ];then
    echo “备份失败”
else
    echo "备份成功"
fi
```
#!/bin/bash为shell文件开头必填项，它**指定了shell脚本解释器的路径**，而且这个指定路径只能放在文件的第一行.第一行写错或者不写时，系统会有一个默认的解释器进行解释。
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin设置环境变量最好也不变
cp、mv这些主要运行命令前面加上sudo防止权限不够（Permission denied）
# (3)用crontab -e打开定时器设置，写入：
0 16 * * * sh /home/trizhi2/zhangshiju/copyfile.sh > /home/trizhi2/zhangshiju/copyfile.log
sh前面的五个位置具体作用见:https://blog.csdn.net/woshiyangyunlong/article/details/99944576
sh后面填要运行的脚本的路径
>后面代表要将运行结果写入哪个文件
整个命令的意思是：在每一天的16点运行一次copyfile.sh脚本，并把打印(echo)结果写在copyfile.log里面
# (4)查看正在定时运行的脚本crontab -l


# 三、归档文件
  要求: 实现每天对指定目录归档备份的脚本，输入一个目录名称（末尾不带/），将目录下所有文件按天归档保存，并将归档日期
  附加在归档文件名上
  用到归档命令: tar
  后面加上-c选项表示归档，加上-z选项表示同时进行压缩，得到的文件名后缀名为.tar.gz
  脚本:
  #! /bin/bash
  # 首先判断输入参数个数是否为1
  if [ $# -ne 1 ]
  then
      echo "参数个数错误！应该输入一个参数作为归档目录名"
  fi

  # 从参数中获取目录名称
  if [ -d $1 ]
  then
      echo
  else
      echo
      echo "目录不存在！"
      exit
  fi

  DIR_NAME=$[basename $1]
  DIR_PATH=$[cd $(dirname $1); pwd]

  # 获取当前日期
  DATE=$(date +%y%m%d)

  # 定义生成归档文件的名称
  FILE=archive_${DIR_NAME}_$DATE.tar.gz
  DEST=/root/archive/$FILE

  # 开始归档目录文件
  echo "开始归档"
  echo

  tar -czf $DEST $DIR_PATH/$DIR_NAME

  if [ $? -eq 0 ]
  then
     echo
     echo "归档成功"
     echo "归档文件为: $DEST"
     echo
  else
     echo "归档出现问题"
     echo
  fi
  
  exit


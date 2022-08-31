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

# 四、正则
  # (1)grep、sed、awk等文本处理工具都支持正则表达式
  # (2)常规匹配
  一串不包含特殊字符的表达式匹配它自己:
  cat /etc/passwd |grep root
  匹配所有包含root的行
  # (3)特殊匹配
  1、匹配一行的开头(^):
  cat /etc/passwd |grep ^a
  匹配所有以a开头的行
  2、匹配一行的结尾($):
  cat /etc/passwd |grep t$
  匹配所有以t结尾的行
  3、匹配空行
  cat /etc/passwd |grep ^$
  4、匹配任意字符(.)
  cat /etc/passwd |grep r..t
  匹配r和t之间有任意两个字符的行
  5、上一个字符出现0次或多次(*)，1次或多次(+)
  cat /etc/passwd |grep ro*t
  会匹配到rt、rot、root、rooot等情况
  因此 .* 就表示任意字符出现任意次
  6、匹配范围内的一个字符([])
  [6,8]       匹配6或8
  [0-9]       匹配0到9中的任意一个数字
  [0-9]*      匹配任意长度的数字字符串
  [a-c, e-f]  匹配a-c或者e-f之间的任意字符
  # (4)实例
  匹配手机号
  echo "15399876478" |grep -E ^1[34578][0-9]{9}$
  加了-E才能支持{9}的写法


# 五、文本处理工具
  # (1)cut  剪
  1、概念
    在文件中负责剪切数据。从文件中每一行剪切字节、字符和字段输出
  2、语法
    cut [选项] filename
  3、选项说明
    -f  列号，第几列
    -d  分隔符，按照指定的分隔符分割列，默认\t
    -c  按字符进行切割，后加数字表示第几列，例如 -c 1
  4、例子
  1.截取文档的第一列，以空格为分割符
  cut -d " " -f 1 cut.txt
  2.截取第二、三列
  cut -d " " -f 2,3 cut.txt
  3.截取passwd中有用信息
  cat /etc/passwd |grep bash$ | cut -d ":" -f 1,6,7
  4.提取ifconfig的ip(以ubuntu系统为例)
  ifconfig docker0 | grep Bcast | cut -d " " -f 12

  # (2)awk
  # 1.概念
  把文件逐行读入，以空格为默认分隔符将每行切片，切开的部分再进行分析处理
  # 2.语法
  awk [选项参数] '/pattern1/{action1} /pattern2/{action2}...' filename
  parttern: 表示awk在数据中查找的内容，就是匹配模式
  action: 在找到匹配内容时所执行的一些了命令
  # 3、选项参数说明
  -F  指定输入文件分隔符
  -v  赋值一个用户定义变量
  # 4、例子
  1.搜索passwd文件以root开头所有行，并输出该行的第7列
  awk -F ":" '/^root/ {print $7}'
  2.搜索passwd文件以root开头所有行，并输出该行的第1列和第7列，中间以“,”号分割
  awk -F ":"  '/^root/ {print $1","$7}'
  3.只显示/etc/passwd的第一列和第七列，以逗号分割，且在所有行前面添加列名user，shell在最后一行添加“abc”
  awk -F : 'BEGIN{print "user, shell"} {print $1","$7} END{print "abc"} passwd
  4.将passwd文件中的用户id增加1并输出
  awk -v i=1 -F ": '{print $3+i}'
  # 5、内置变量
  FILENAME  文件名
  NR        行号
  NF        切割后，列的个数
  1.统计passwd文件名、每行行号、每行列数
  awk -F : '{print "filename" FILENAME ",linenum" NR "col" NF}'
  2.输出ifconfig的行号
  ifconfig | awk '/^$/ {print NR}'


# 六、发送信息给另一个用户
 (1)查看用户是否登录
 login_user=$(who | grep -i -m 1 $1 | awk '{print $1}')
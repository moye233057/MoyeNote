# 一、反转字典
方法一:
for k,v in myinfor.items():
     infor[v]=k
方法二:
myinfor =  {"name":"qiwsir","site":"qiwsir.github.io","lang":"python"}
reverseDict = dict(zip(myinfor.values(),myinfor.keys()))



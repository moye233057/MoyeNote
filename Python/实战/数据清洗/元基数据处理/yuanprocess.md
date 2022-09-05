"""
目标：写一个处理通用基元库数据的脚本
数据分析：
一、通用基元库里面包含了基元的英文名和中文名，基元又分父基元和子基元，父子为上下级关系
二、目标文件第一列为ID（自增长），第二列留空，第三列为父ID，第四列为基元英文名，第五列为基元中文名
三、目标文件要有上下对应关系，体现为：
1、子基元的父ID为父基元在ID列中的数值，父基元的父ID另有数值
2、最终需要ID-父ID-子基元英文名-子基元中文名的对应关系
难点：
一、如何识别哪个是父基元？
观察到父基元的字体颜色不是黑色，文件中有空行，可以单独分隔取第一行为父基元
二、如何给子基元加上编号同时把父基元的ID放入父ID中？

"""

import xlrd
import pandas as pd


def getonerowlist(sorexcelpath,sheetname,col):
    """
    Args:
        sorexcelpath: 要插入的数据文件路径.xlsx
        sheetname: 工作簿名字
        col: 要提取的列数据
    Returns:一个包含单列所有数据的二维数组，数组中每个单元代表父基元(第一个)和它的所有子基元
    数据格式：空格（如果有效数据在第一列注释掉下面的del）-父基元-子基元-空格
    """
    wb = xlrd.open_workbook(sorexcelpath)
    sh = wb.sheet_by_name(sheetname)
    name = sh.col_values(col)
    del (name[0])  #删除第一行，若第一行有用注释掉
    everypoint = []
    onelist = []
    for index, en in enumerate(name):
        if len(en) > 0:
            onelist.append(en)
        elif len(en) == 0:
            everypoint.append(onelist)
            onelist = []
        if index == len(name) - 1:
            everypoint.append(onelist)
            onelist = []
    return everypoint



def getinsertdata(goalexcelpath,sheetname,enlist,zhlist,firstID):
    """
    Args:
        goalexcelpath: 要插入数据的文件路径
        sheetname: 工作薄名字
        enlist: getonerowlist中返回的英文名词列表
        zhlist: getonerowlist中返回的中文名词列表
        firstID: 插入数据插入的位置，同时也是数据的第一个ID
    Returns:要插入的数据，采用源数据拼接插入数据的形式
    """
    insertdata = []
    i = 0
    ID = firstID
    for type in enlist:
        j = 0
        parent_ID = firstID+1
        for name in type:
            ID += 1
            parent_enname = name
            parent_zhname = zhlist[i][j]
            j+=1
            row = [ID,'',parent_ID,parent_enname,parent_zhname]
            insertdata.append(row)
        firstID += len(type)
        i+=1
    df1 = pd.read_excel(goalexcelpath, sheet_name=sheetname)
    print(df1)
    df2 = pd.DataFrame(insertdata, columns=['ID', 'charall', 'parentid', 'chare', 'charc'])
    insertdata = df1.append(df2)

    return insertdata


if __name__ == '__main__':
    #要插入的数据文件路径，如通用基元参考库-1-示例test
    sorpath = 'data/通用基元参考库-1-示例test.xlsx'
    #目标数据文件路径，如whole-for input Tr
    respath = 'data/whole-for input Tr.xlsx'
    #要处理的excel文件的工作表名字
    sheetname = 'Sheet1'
    #英文元基列表，样例是取第0列数据
    enlist = getonerowlist(sorpath, sheetname, 0)
    #中文元基列表，样例是取第1列数据
    zhlist = getonerowlist(sorpath, sheetname, 1)
    # print(enlist)
    # print(zhlist)
    # 得到要插入的数据，type=DataFrame，firstID是代表数据插入第几行，同时作为ID
    insertdata = getinsertdata(respath,sheetname,enlist,zhlist,firstID=4999)
    # print(insertdata)
    # 插入数据
    insertdata.to_excel(respath,sheetname,index=False)


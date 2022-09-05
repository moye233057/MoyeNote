# 将biao.xls中的专利信息清洗后转换为前端需要的格式
import os
import re


def getFileData(request):
    titles = getInferTitles()
    filepath = os.path.join(BASE_DIR, 'media/biao.xls')
    if not os.path.exists(filepath):
        print('文件不存在')
    basename = os.path.basename(filepath)
    filename, ext = basename.split('.')
    returndata = []
    if ext == 'xls':
        # 工作表的名字
        xlsxsheetname = 'Sheet1'
        # 利用xlrd库打开xlsx后缀的excel表格
        wb = xlrd.open_workbook(filepath)
        # 按工作簿定位工作表
        sh = wb.sheet_by_name(xlsxsheetname)
        print(len(titles))
        for i in range(1, 20):
            data = sh.row_values(i)  # list
            json = {}
            nocount = -1
            for j, col in enumerate(titles):
                label = col['label']
                prop = col['prop']

                # 这四个字段是文件中没有的，因此取data中的数据是下标不能移动
                # 举例：如果当前col['label']为撤回原因，data[j - nocount]此时对应的是它下一个是否进入初审合格阶段的数据
                #      nocout这时候要-1，意思是这一次的取数不写入撤回原因，而应该写入下一个是否初审合格阶段
                if label in ['撤回原因', '申请缴费期限']:
                    nocount += 1
                    thisdata = ''
                else:
                    thisdata = data[j - nocount]
                if label in ['驳回时间', '是否视为撤回的时间']:
                    nocount += 1
                    continue
                # 是否驳回和是否视为撤回包含了它们下一个字段的内容，因此需要单独提取出来放到下一个字段中
                # 它们本身含有的括号中的内容对于它们也是多余的，要去除，prop是前端对应数据时需要的字段，作为键值
                if label == '是否驳回':
                    pat = re.compile('[(|（](.*?)[)|）]')
                    chtime = ''.join(re.findall(pat, thisdata))
                    # 如果是否驳回数据为是(2021/9/12)的形式
                    if len(chtime) > 0:
                        # 将括号里的时间作为驳回时间，添加到驳回时间列
                        thisdata = thisdata.replace(chtime, '')
                        thisdata = re.sub(u'[)|(|（|）]', '', thisdata)
                        json[prop] = thisdata
                        # 去除括号内容保留是否，放在是否驳回列
                        chtime = chtime.split('/')
                        if len(chtime[1]) < 2:
                            chtime[1] = '0' + chtime[1]
                        if len(chtime[2]) < 2:
                            chtime[2] = '0' + chtime[2]
                        chtime = ''.join(chtime)
                        json['time_bh'] = chtime
                        continue
                    elif '是' or '否' in thisdata:
                        json[prop] = thisdata
                        continue
                elif label == '是否视为撤回':
                    pat = re.compile('[(|（](.*?)[)|）]')
                    chtime = ''.join(re.findall(pat, thisdata))
                    # 如果是否驳回数据为是(2021/9/12)的形式
                    if len(chtime) > 0:
                        # 将括号里的时间作为驳回时间，添加到驳回时间列
                        thisdata = thisdata.replace(chtime, '')
                        thisdata = re.sub(u'[)|(|（|）]', '', thisdata)
                        json[prop] = thisdata
                        # 去除括号内容保留是否，放在是否驳回列
                        chtime = chtime.split('/')
                        if len(chtime[1]) < 2:
                            chtime[1] = '0' + chtime[1]
                        if len(chtime[2]) < 2:
                            chtime[2] = '0' + chtime[2]
                        chtime = ''.join(chtime)
                        json['time_if_ch'] = chtime
                        continue
                    elif '是' or '否' in thisdata:
                        json[prop] = thisdata
                        continue
                # 因为是否视为撤回的时间和驳回时间已经在上面的是否驳回和是否视为撤回代码中添加了
                # 所以轮到label为这两个的时候直接跳过，避免覆盖之前添加的内容
                if 'time_if_ch' in json.keys():
                    if label == '是否视为撤回的时间':
                        continue
                if 'time_bh' in json.keys():
                    if label == '驳回时间':
                        continue
                if label == '最后恢复时间':
                    if type(thisdata) == str:
                        if len(thisdata.strip()) > 0:
                            thisdata = thisdata.split('/')
                            if len(thisdata[1]) < 2:
                                thisdata[1] = '0' + thisdata[1]
                            if len(thisdata[2]) < 2:
                                thisdata[2] = '0' + thisdata[2]
                            thisdata = ''.join(thisdata)
                # 对于包含时间的数据，要进行格式转换，如果时间包含不规则数据，用另外的代码处理
                if '时间' in label:
                    try:
                        cdata = xlrd.xldate_as_tuple(thisdata, 0)
                        thisdata = datetime.datetime(cdata[0], cdata[1], cdata[2]).strftime('%Y%m%d')
                    except:
                        pass
                if type(thisdata) == str:
                    thisdata = thisdata.strip()
                    thisdata = re.sub(u'[(|（|【](.*?)[)|）|】]', '', thisdata)
                    thisdata = thisdata.replace('无', '')
                json[prop] = thisdata
            returndata.append(json)
    data = {
        'data': returndata,
        'msg': '获取数据成功',
    }
    return JsonResponse(data)
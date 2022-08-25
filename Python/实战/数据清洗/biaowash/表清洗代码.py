import os
import re
import csv
import xlrd
import datetime
import pandas as pd

titles = [
    {
        'value': '0',
        'label': '专利号',
        'prop': "hao"
    },
    {
        'value': '1',
        'label': '发明名称',
        'prop': "name"
    },
    {
        'value': '2',
        'label': '发明人',
        'prop': "people"
    },
    {
        'value': '3',
        'label': '申请人',
        'prop': "appli"
    },
    {
        'value': '4',
        'label': '发明类型',
        'prop': "type"
    },
    {
        'value': '5',
        'label': '申请时间',
        'prop': "time_apply"
    },
    {
        'value': '6',
        'label': '申请是否缴费',
        'prop': "if_apply_pay"
    },
    {
        'value': '7',
        'label': '申请缴费期限',
        'prop': "time_last_apply_pay"
    },
    {
        'value': '8',
        'label': '是否初审',
        'prop': "if_cs"
    },
    {
        'value': '9',
        'label': '是否实质审查',
        'prop': "if_sc"
    },
    {
        'value': '10',
        'label': '是否实质审查缴费',
        'prop': "if_sc_pay"
    },
    {
        'value': '11',
        'label': '第一次审核意见时间',
        'prop': "time_first_sh"
    },
    {
        'value': '12',
        'label': '第一次审核意见答复时间',
        'prop': "time_first_sh_df"
    },
    {
        'value': '13',
        'label': '第n次审核意见时间',
        'prop': "time_n_sh"
    },
    {
        'value': '14',
        'label': '第n次审核意见答复时间',
        'prop': "time_n_sh_df"
    },
    {
        'value': '15',
        'label': '撤回时间',
        'prop': "time_ch"
    },
    {
        'value': '16',
        'label': '撤回原因',
        'prop': "ch_reason"
    },
    {
        'value': '17',
        'label': '是否进入初审合格阶段',
        'prop': "if_cs_hege"
    },
    {
        'value': '18',
        'label': '是否驳回',
        'prop': "if_bh"
    },
    {
        'value': '19',
        'label': '驳回时间',
        'prop': "time_bh"
    },
    {
        'value': '20',
        'label': '是否视为撤回',
        'prop': "if_ch"
    },
    {
        'value': '21',
        'label': '是否视为撤回的时间',
        'prop': "time_if_ch"
    },
    {
        'value': '22',
        'label': '终止复审时间',
        'prop': "time_zz"
    },
    {
        'value': '23',
        'label': '是否授权',
        'prop': "if_sq"
    },
    {
        'value': '24',
        'label': '授权时间',
        'prop': "time_sq"
    },
    {
        'value': '25',
        'label': '授权最后缴费时间',
        'prop': "time_sq_pay"
    },
    {
        'value': '26',
        'label': '最后恢复时间',
        'prop': "time_rec"
    },
    {
        'value': '27',
        'label': '年费缴费最近一年',
        'prop': "time_pay_nf"
    },
    {
        'value': '28',
        'label': '年费缴费最近两年',
        'prop': "time_pay_nf_two"
    },
    {
        'value': '29',
        'label': '是否已经出售',
        'prop': "if_sale"
    },
    {
        'value': '30',
        'label': '出售金额',
        'prop': "sale_price"
    },
    {
        'value': '31',
        'label': '变更公司',
        'prop': "company"
    },
    {
        'value': '32',
        'label': '备注',
        'prop': "remarks"
    }
]


filepath = '../media/biao.xls'
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
    # print(len(titles))
    for i in range(1, sh.nrows):
        data = sh.row_values(i)  # list
        json = {}
        nocount = -1
        for j, col in enumerate(titles):
            label = col['label']
            prop = col['prop']
            if label in ['撤回原因', '申请缴费期限']:
                nocount += 1
                thisdata = ''
            else:
                thisdata = data[j - nocount]
            if label in ['驳回时间', '是否视为撤回的时间']:
                nocount += 1
                continue
            if label == '是否驳回':
                pat = re.compile('[(|（](.*?)[)|）]')
                chtime = ''.join(re.findall(pat, thisdata))
                # print('bhtime:', chtime)
                # 如果是否驳回数据为是(2021/9/12)的形式
                if len(chtime) > 0:
                    # 将括号里的时间作为驳回时间，添加到驳回时间列
                    thisdata = thisdata.replace(chtime, '')
                    thisdata = re.sub(u'[)|(|（|）]', '', thisdata)
                    json[label] = thisdata
                    # 去除括号内容保留是否，放在是否驳回列
                    chtime = chtime.split('/')
                    if len(chtime[1]) < 2:
                        chtime[1] = '0' + chtime[1]
                    if len(chtime[2]) < 2:
                        chtime[2] = '0' + chtime[2]
                    chtime = ''.join(chtime)
                    json['驳回时间'] = chtime
                    continue
                elif '是' or '否' in thisdata:
                    json[label] = thisdata
                    json['驳回时间'] = ''
                    continue
                else:
                    json['驳回时间'] = ''

            elif label == '是否视为撤回':
                pat = re.compile('[(|（](.*?)[)|）]')
                chtime = ''.join(re.findall(pat, thisdata))
                # print('chtime:', chtime)
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
                    json['是否视为撤回的时间'] = chtime
                    continue
                elif '是' or '否' in thisdata:
                    json[label] = thisdata
                    json['是否视为撤回的时间'] = ''
                    continue
                else:
                    json['是否视为撤回的时间'] = ''

            if '是否视为撤回的时间' in json.keys():
                if label == '是否视为撤回的时间':
                    continue
            if '驳回时间' in json.keys():
                if label == '驳回时间':
                    continue

            if type(thisdata) == str:
                thisdata = thisdata.strip()
                thisdata = re.sub(u'[(|（|【](.*?)[)|）|】]', '', thisdata)
                thisdata = thisdata.replace('无', '')
                thisdata = thisdata.replace('√', '')
                if label == '撤回时间':
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        try:
                            if len(thisdata[1]) < 2:
                                thisdata[1] = '0' + thisdata[1]
                            if len(thisdata[2]) < 2:
                                thisdata[2] = '0' + thisdata[2]
                        except:
                            thisdata = []
                        thisdata = ''.join(thisdata)
                elif label == '年费缴费最近一年':
                    print('___________________')
                    print('年缴一年')
                    print(thisdata)
                    print(type(thisdata))
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                    print(thisdata)
                    print(type(thisdata))
                    print('___________________')
                elif label == '第一次审核意见答复时间':
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                elif label == '第n次审核意见答复时间':
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                elif label == '授权最后缴费时间':
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                elif label == '终止复审时间':
                    if '/' in str(thisdata):
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                elif label == '是否实质审查缴费':
                    if thisdata == '':
                        thisdata = '否'
                    else:
                        thisdata = '是'
                elif '是否' in label:
                    if thisdata != '是':
                        thisdata = '否'

            if label == '最后恢复时间':
                if type(thisdata) == str:
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)

            if '时间' in label:
                try:
                    cdata = xlrd.xldate_as_tuple(thisdata, 0)
                    thisdata = datetime.datetime(cdata[0], cdata[1], cdata[2]).strftime('%Y%m%d')
                except:
                    pass
            json[label] = thisdata
        returndata.append(json)

keys = returndata[1].keys()
keys = list(keys)
print(len(keys))
# print(keys)
# print(type(keys))
# # values = returndata[11].values()
# for i in [4, 7, 11]:
#     for k, v in returndata[i].items():
#         print(k, v)
#     print('____________________')
data = []
for d in returndata:
    value = d.values()
    data.append(list(value))
print(len(data[0]))
print(data)
# df = pd.DataFrame(data, columns=keys)
# print(df.head())
csv_path = '../media/washbiao.csv'
with open(csv_path, "w", encoding='utf-8', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    writer.writerows(data)

# df.to_csv(csv_path, sep=',')
import os
import re
import csv
import xlrd
import datetime
import pandas as pd

titles = [
    {
        'value': '0',
        'label': 'ר����',
        'prop': "hao"
    },
    {
        'value': '1',
        'label': '��������',
        'prop': "name"
    },
    {
        'value': '2',
        'label': '������',
        'prop': "people"
    },
    {
        'value': '3',
        'label': '������',
        'prop': "appli"
    },
    {
        'value': '4',
        'label': '��������',
        'prop': "type"
    },
    {
        'value': '5',
        'label': '����ʱ��',
        'prop': "time_apply"
    },
    {
        'value': '6',
        'label': '�����Ƿ�ɷ�',
        'prop': "if_apply_pay"
    },
    {
        'value': '7',
        'label': '����ɷ�����',
        'prop': "time_last_apply_pay"
    },
    {
        'value': '8',
        'label': '�Ƿ����',
        'prop': "if_cs"
    },
    {
        'value': '9',
        'label': '�Ƿ�ʵ�����',
        'prop': "if_sc"
    },
    {
        'value': '10',
        'label': '�Ƿ�ʵ�����ɷ�',
        'prop': "if_sc_pay"
    },
    {
        'value': '11',
        'label': '��һ��������ʱ��',
        'prop': "time_first_sh"
    },
    {
        'value': '12',
        'label': '��һ����������ʱ��',
        'prop': "time_first_sh_df"
    },
    {
        'value': '13',
        'label': '��n��������ʱ��',
        'prop': "time_n_sh"
    },
    {
        'value': '14',
        'label': '��n����������ʱ��',
        'prop': "time_n_sh_df"
    },
    {
        'value': '15',
        'label': '����ʱ��',
        'prop': "time_ch"
    },
    {
        'value': '16',
        'label': '����ԭ��',
        'prop': "ch_reason"
    },
    {
        'value': '17',
        'label': '�Ƿ�������ϸ�׶�',
        'prop': "if_cs_hege"
    },
    {
        'value': '18',
        'label': '�Ƿ񲵻�',
        'prop': "if_bh"
    },
    {
        'value': '19',
        'label': '����ʱ��',
        'prop': "time_bh"
    },
    {
        'value': '20',
        'label': '�Ƿ���Ϊ����',
        'prop': "if_ch"
    },
    {
        'value': '21',
        'label': '�Ƿ���Ϊ���ص�ʱ��',
        'prop': "time_if_ch"
    },
    {
        'value': '22',
        'label': '��ֹ����ʱ��',
        'prop': "time_zz"
    },
    {
        'value': '23',
        'label': '�Ƿ���Ȩ',
        'prop': "if_sq"
    },
    {
        'value': '24',
        'label': '��Ȩʱ��',
        'prop': "time_sq"
    },
    {
        'value': '25',
        'label': '��Ȩ���ɷ�ʱ��',
        'prop': "time_sq_pay"
    },
    {
        'value': '26',
        'label': '���ָ�ʱ��',
        'prop': "time_rec"
    },
    {
        'value': '27',
        'label': '��ѽɷ����һ��',
        'prop': "time_pay_nf"
    },
    {
        'value': '28',
        'label': '��ѽɷ��������',
        'prop': "time_pay_nf_two"
    },
    {
        'value': '29',
        'label': '�Ƿ��Ѿ�����',
        'prop': "if_sale"
    },
    {
        'value': '30',
        'label': '���۽��',
        'prop': "sale_price"
    },
    {
        'value': '31',
        'label': '�����˾',
        'prop': "company"
    },
    {
        'value': '32',
        'label': '��ע',
        'prop': "remarks"
    }
]


filepath = '../media/biao.xls'
if not os.path.exists(filepath):
    print('�ļ�������')
basename = os.path.basename(filepath)
filename, ext = basename.split('.')
returndata = []
if ext == 'xls':
    # �����������
    xlsxsheetname = 'Sheet1'
    # ����xlrd���xlsx��׺��excel���
    wb = xlrd.open_workbook(filepath)
    # ����������λ������
    sh = wb.sheet_by_name(xlsxsheetname)
    # print(len(titles))
    for i in range(1, sh.nrows):
        data = sh.row_values(i)  # list
        json = {}
        nocount = -1
        for j, col in enumerate(titles):
            label = col['label']
            prop = col['prop']
            if label in ['����ԭ��', '����ɷ�����']:
                nocount += 1
                thisdata = ''
            else:
                thisdata = data[j - nocount]
            if label in ['����ʱ��', '�Ƿ���Ϊ���ص�ʱ��']:
                nocount += 1
                continue
            if label == '�Ƿ񲵻�':
                pat = re.compile('[(|��](.*?)[)|��]')
                chtime = ''.join(re.findall(pat, thisdata))
                # print('bhtime:', chtime)
                # ����Ƿ񲵻�����Ϊ��(2021/9/12)����ʽ
                if len(chtime) > 0:
                    # ���������ʱ����Ϊ����ʱ�䣬��ӵ�����ʱ����
                    thisdata = thisdata.replace(chtime, '')
                    thisdata = re.sub(u'[)|(|��|��]', '', thisdata)
                    json[label] = thisdata
                    # ȥ���������ݱ����Ƿ񣬷����Ƿ񲵻���
                    chtime = chtime.split('/')
                    if len(chtime[1]) < 2:
                        chtime[1] = '0' + chtime[1]
                    if len(chtime[2]) < 2:
                        chtime[2] = '0' + chtime[2]
                    chtime = ''.join(chtime)
                    json['����ʱ��'] = chtime
                    continue
                elif '��' or '��' in thisdata:
                    json[label] = thisdata
                    json['����ʱ��'] = ''
                    continue
                else:
                    json['����ʱ��'] = ''

            elif label == '�Ƿ���Ϊ����':
                pat = re.compile('[(|��](.*?)[)|��]')
                chtime = ''.join(re.findall(pat, thisdata))
                # print('chtime:', chtime)
                # ����Ƿ񲵻�����Ϊ��(2021/9/12)����ʽ
                if len(chtime) > 0:
                    # ���������ʱ����Ϊ����ʱ�䣬��ӵ�����ʱ����
                    thisdata = thisdata.replace(chtime, '')
                    thisdata = re.sub(u'[)|(|��|��]', '', thisdata)
                    json[prop] = thisdata
                    # ȥ���������ݱ����Ƿ񣬷����Ƿ񲵻���
                    chtime = chtime.split('/')
                    if len(chtime[1]) < 2:
                        chtime[1] = '0' + chtime[1]
                    if len(chtime[2]) < 2:
                        chtime[2] = '0' + chtime[2]
                    chtime = ''.join(chtime)
                    json['�Ƿ���Ϊ���ص�ʱ��'] = chtime
                    continue
                elif '��' or '��' in thisdata:
                    json[label] = thisdata
                    json['�Ƿ���Ϊ���ص�ʱ��'] = ''
                    continue
                else:
                    json['�Ƿ���Ϊ���ص�ʱ��'] = ''

            if '�Ƿ���Ϊ���ص�ʱ��' in json.keys():
                if label == '�Ƿ���Ϊ���ص�ʱ��':
                    continue
            if '����ʱ��' in json.keys():
                if label == '����ʱ��':
                    continue

            if type(thisdata) == str:
                thisdata = thisdata.strip()
                thisdata = re.sub(u'[(|��|��](.*?)[)|��|��]', '', thisdata)
                thisdata = thisdata.replace('��', '')
                thisdata = thisdata.replace('��', '')
                if label == '����ʱ��':
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
                elif label == '��ѽɷ����һ��':
                    print('___________________')
                    print('���һ��')
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
                elif label == '��һ����������ʱ��':
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                elif label == '��n����������ʱ��':
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                elif label == '��Ȩ���ɷ�ʱ��':
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                elif label == '��ֹ����ʱ��':
                    if '/' in str(thisdata):
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)
                elif label == '�Ƿ�ʵ�����ɷ�':
                    if thisdata == '':
                        thisdata = '��'
                    else:
                        thisdata = '��'
                elif '�Ƿ�' in label:
                    if thisdata != '��':
                        thisdata = '��'

            if label == '���ָ�ʱ��':
                if type(thisdata) == str:
                    if len(thisdata.strip()) > 0:
                        thisdata = thisdata.split('/')
                        if len(thisdata[1]) < 2:
                            thisdata[1] = '0' + thisdata[1]
                        if len(thisdata[2]) < 2:
                            thisdata[2] = '0' + thisdata[2]
                        thisdata = ''.join(thisdata)

            if 'ʱ��' in label:
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
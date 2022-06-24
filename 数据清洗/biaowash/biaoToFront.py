# ��biao.xls�е�ר����Ϣ��ϴ��ת��Ϊǰ����Ҫ�ĸ�ʽ
import os
import re


def getFileData(request):
    titles = getInferTitles()
    filepath = os.path.join(BASE_DIR, 'media/biao.xls')
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
        print(len(titles))
        for i in range(1, 20):
            data = sh.row_values(i)  # list
            json = {}
            nocount = -1
            for j, col in enumerate(titles):
                label = col['label']
                prop = col['prop']

                # ���ĸ��ֶ����ļ���û�еģ����ȡdata�е��������±겻���ƶ�
                # �����������ǰcol['label']Ϊ����ԭ��data[j - nocount]��ʱ��Ӧ��������һ���Ƿ�������ϸ�׶ε�����
                #      nocout��ʱ��Ҫ-1����˼����һ�ε�ȡ����д�볷��ԭ�򣬶�Ӧ��д����һ���Ƿ����ϸ�׶�
                if label in ['����ԭ��', '����ɷ�����']:
                    nocount += 1
                    thisdata = ''
                else:
                    thisdata = data[j - nocount]
                if label in ['����ʱ��', '�Ƿ���Ϊ���ص�ʱ��']:
                    nocount += 1
                    continue
                # �Ƿ񲵻غ��Ƿ���Ϊ���ذ�����������һ���ֶε����ݣ������Ҫ������ȡ�����ŵ���һ���ֶ���
                # ���Ǳ����е������е����ݶ�������Ҳ�Ƕ���ģ�Ҫȥ����prop��ǰ�˶�Ӧ����ʱ��Ҫ���ֶΣ���Ϊ��ֵ
                if label == '�Ƿ񲵻�':
                    pat = re.compile('[(|��](.*?)[)|��]')
                    chtime = ''.join(re.findall(pat, thisdata))
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
                        json['time_bh'] = chtime
                        continue
                    elif '��' or '��' in thisdata:
                        json[prop] = thisdata
                        continue
                elif label == '�Ƿ���Ϊ����':
                    pat = re.compile('[(|��](.*?)[)|��]')
                    chtime = ''.join(re.findall(pat, thisdata))
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
                        json['time_if_ch'] = chtime
                        continue
                    elif '��' or '��' in thisdata:
                        json[prop] = thisdata
                        continue
                # ��Ϊ�Ƿ���Ϊ���ص�ʱ��Ͳ���ʱ���Ѿ���������Ƿ񲵻غ��Ƿ���Ϊ���ش����������
                # �����ֵ�labelΪ��������ʱ��ֱ�����������⸲��֮ǰ��ӵ�����
                if 'time_if_ch' in json.keys():
                    if label == '�Ƿ���Ϊ���ص�ʱ��':
                        continue
                if 'time_bh' in json.keys():
                    if label == '����ʱ��':
                        continue
                if label == '���ָ�ʱ��':
                    if type(thisdata) == str:
                        if len(thisdata.strip()) > 0:
                            thisdata = thisdata.split('/')
                            if len(thisdata[1]) < 2:
                                thisdata[1] = '0' + thisdata[1]
                            if len(thisdata[2]) < 2:
                                thisdata[2] = '0' + thisdata[2]
                            thisdata = ''.join(thisdata)
                # ���ڰ���ʱ������ݣ�Ҫ���и�ʽת�������ʱ��������������ݣ�������Ĵ��봦��
                if 'ʱ��' in label:
                    try:
                        cdata = xlrd.xldate_as_tuple(thisdata, 0)
                        thisdata = datetime.datetime(cdata[0], cdata[1], cdata[2]).strftime('%Y%m%d')
                    except:
                        pass
                if type(thisdata) == str:
                    thisdata = thisdata.strip()
                    thisdata = re.sub(u'[(|��|��](.*?)[)|��|��]', '', thisdata)
                    thisdata = thisdata.replace('��', '')
                json[prop] = thisdata
            returndata.append(json)
    data = {
        'data': returndata,
        'msg': '��ȡ���ݳɹ�',
    }
    return JsonResponse(data)
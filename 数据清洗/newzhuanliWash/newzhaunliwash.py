# coding: utf-8
import re

path = 'newzhuanli.txt'
path1 = './data.txt'


def washNewzhuanliTxt():
    with open(path, 'r', encoding='utf_8_sig') as f:
        lines = f.readlines()
        print(len(lines), type(lines))
        washdata = []
        for index, line in enumerate(lines):
            washline = ''
            line = line.replace('\u2011', '').replace('\xa0', '').replace('\u2282', '').replace('\u230a', '') \
                .replace('\u230b', '').replace('\u2029', '').replace('\u2029', '').replace('\u03f5', '').replace('\xb5',
                                                                                                                 '') \
                .replace('\u2206', '').replace('\u03d1', '').replace('\xba', '').replace('\xb4', '').replace('\u2a02',
                                                                                                             '') \
                .replace('\u2022', '').replace('\u211d', '').replace('\u0108', '').replace('\u2212', '').replace(
                '\uff65', '') \
                .replace('\ufb02', '').replace('\u03d5', '').replace('\u2209', '')
            washdata.append(line)
        with open(path1, 'w', encoding='utf-8') as f1:
            for data in washdata:
                f1.write(data)


with open(path1, 'r', encoding='utf-8') as f3:
    lines = f3.readlines()
    for line in lines:
        line = re.split('==', line)
        last = line[-1]
        # for d in line:
        #     print(d)
        d = last.split('<<<--->>>')
        if len(d) > 4:
            quanurl = d[1]
            quancon = d[2]
            shuourl = d[3]
            shuocon = d[4]
            line.pop()
            line.pop(7)
            line.append(quanurl)
            line.append(quancon)
            line.append(shuourl)
            line.append(shuocon)
        else:
            other = line[-1]
            last2 = line[-2]
            d = last2.split('<<<--->>>')
            if len(d) > 4:
                quanurl = d[1]
                quancon = d[2]
                shuourl = d[3]
                shuocon = d[4]
                line.pop()
                line.pop(7)
                line.append(quanurl)
                line.append(quancon)
                line.append(shuourl)
                line.append(shuocon + other)
        print(line)

titles = ['公开号', '专利名称', '法律状态', '公开日', '申请号', '申请日', '申请人', '发明人', '代理机构',
          '分类号', '权利要求书地址', '权利要求', '说明书地址', '说明书']

engtitles = ['publicNumber', 'title', 'legalStatus', 'publicDay', 'appliNumber', 'appliDay', 'appliPeople', 'inventor'
             'agency', 'classificationNumber', 'quanUrl', 'quanCon', 'shuoUrl', 'shuoCon']
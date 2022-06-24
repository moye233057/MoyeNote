ids = []
titles = []
contents = []
values = []
pricemap = {'1': 0, '2': 35, '3': 50, '4': 70}
des = {'1': '不合格', '2': '看不太懂', '3': '思路清晰', '4': '有创造性'}
statistics = []
total = 0  # 总评估得分
effectcount = 0  # 符合主id与子id文本长度之和大于300的步骤个数
allcount = 0  # 主id段落数量
stepcount = 0  # 每个主id段落及其子id段落的文本长度
for i, v in enumerate(titles):
    # type1:当前id为主id，下一个id也为主id
    # type2:当前id为主id，下一个id为子id
    # type3:当前id为子id，下一个id为主id
    # type3:当前id为子id，下一个id为主id
    # type4:当前id为子id，下一个id为子id
    # type5:没有下一个id
    ifrun = 'type1'

    c = contents[i]
    value = values[i]
    d = des[value]
    thisprice = pricemap[value]
    thisstepword = len(v + c)
    if 100 <= thisstepword <= 300:
        thisprice = 10
    elif thisstepword < 100:
        thisprice = 0

    id = ids[i + 2]
    countthis = len(id.split('-'))
    try:
        # 判断下一个id是不是子id
        nextid = ids[i + 3]
        countnext = len(nextid.split('-'))
        if countthis < 2 and countnext < 2:  # type1
            allcount += 1
            stepcount = 0
            stepcount += thisstepword
        elif countthis < 2 and countnext >= 2:  # type2
            ifrun = 'type2'
            allcount += 1
            stepcount = 0
            stepcount += thisstepword
        elif countthis >= 2 and countnext < 2:  # type3
            ifrun = 'type3'
            allcount += 1
            stepcount += thisstepword
        elif countthis >= 2 and countnext >= 2:  # type4
            ifrun = 'type4'
            allcount += 1
            stepcount += thisstepword
    except:  # 如果没有下一个id
        ifrun = 'type5'
        allcount += 1

    # 如果没有下一个子id，开始统计该主id及其子id对应文本长度是否超过300
    print(ifrun)
    if ifrun == 'type1' or ifrun == 'type5':
        print('1')
        if stepcount >= 300:
            effectcount += 1
        elif 100 <= stepcount < 300:
            thisprice = 15
        else:
            thisprice = 0
        constatis = {
            'title': '步骤' + str(id) + '，' + v + '\n',
            'result': '字数:' + str(thisstepword) + '，审核结果:' + str(d) + '，得分:' + str(thisprice) + '分' + '\n\n',
            'price': thisprice
        }
    elif ifrun == 'type2' or ifrun == 'type4':
        print('2')
        constatis = {
            'title': '步骤' + str(id) + '，' + v + '\n',
            'result': '字数:' + str(thisstepword) + '，审核结果:' + str(d) + '\n',
            'price': 0
        }
    elif ifrun == 'type3':
        print('3')
        stepcountnum = 35
        if stepcount > 300:
            effectcount += 1
        if 100 <= stepcount < 300:
            stepcountnum = 15
        elif stepcount < 100:
            stepcountnum = 0
        constatis = {
            'title': '步骤' + str(id) + '，' + v + '\n',
            'result': '字数:' + str(thisstepword) + '，审核结果:' + str(d) + '\n'
                      + '该大步骤的总字数:' + str(stepcount) + '，得分：' + str(stepcountnum) + '分' + '\n\n',
            'price': stepcountnum
        }
    print('________________')

    statistics.append(constatis)


def valueevaluation(request):
    username = request.META.get('HTTP_USERNAME')
    title = request.POST.get('title')
    titles, contents, texts, jishubejing, youyixiaoguo, ids, values = getTitAndCon(request)
    inventframe = request.POST.get('inventframe')
    savetext = frameextraction(inventframe, titles, contents, jishubejing, youyixiaoguo, ids)

    par1 = r'^.{%s}$' % (len(savetext))
    print(par1, title)
    aid = -1
    sid = -1
    try:
        ADdraft = AuditDraft.objects.filter(title=title, content__iregex=par1)
        print(ADdraft)
        if len(ADdraft) > 0:
            aid = list(ADdraft)[-1].id
    except:
        print('管理员表找不到')
    try:
        SDread = SubmitDraft.objects.filter(title=title, content__iregex=par1)
        print(SDread)
        if len(SDread) > 0:
            sid = list(SDread)[-1].uid
    except:
        print('用户表找不到')
    print('最终id', aid, sid)

    reportpath, file_name = pricecalcul(titles, contents, jishubejing, youyixiaoguo, ids, username, values, title)
    thisdraftpath = reportpath.replace('\\', '/')
    pattern = re.compile('(?<=/patentinfer).*$')
    path = re.findall(pattern, thisdraftpath)
    url = gethost(request) + path[0]
    if sid != -1:
        try:
            PFM, created = PriceFileMapping.objects.get_or_create(mapAid=aid, mapSid=sid)
            PriceFileMapping.changepriceurl(PFM, url, file_name)
        except:
            pass

    return responseJson(200, url, '价值报告生成成功')
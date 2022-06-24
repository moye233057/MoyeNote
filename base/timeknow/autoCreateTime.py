import datetime
import re

from base.timeknow.timeCompute import datetimeAndStrEachChange


def jsonCreate(i, v, request):
    json = {}
    v = v.strip()
    # 如果循环到time_apply(申请时间),且时间长度为8位
    # if_apply_pay是否缴费为否或空时,才更新last_time_pay最后缴费期限
    if all([i == 'time_apply', request.POST.get('if_apply_pay') in ['均未交', '申请费已交，实审费未交']]):
        days = 0
        if request.POST.get('if_apply_pay') == '均未交':
            days = 60
        elif request.POST.get('if_apply_pay') == '申请费已交，实审费未交':
            days = 365 * 3
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('更新last_time_pay')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=days)
            recdate_t = date_t + datetime.timedelta(days=60)
            str_t = datetimeAndStrEachChange(date_t)
            json['last_time_pay'] = str_t
            print('last_time_pay:', str_t)
            # 最后恢复时间对于第一次答复时间要加4个月，其他加两个月，这里是原来已经加了两个月，因此再加两个月
            str_t = datetimeAndStrEachChange(recdate_t)
            json['time_rec'] = str_t
            print('time_rec', str_t)
        else:
            json['last_time_pay'] = ''
            json['time_rec'] = ''
    # 如果循环到time_correction(补正通知书时间),且时间长度为8
    # reply_correction答复补正通知书为未补正或空时,才自动更新time_reply_correction补正通知书答复时间
    elif all([i == 'time_correction', request.POST.get('reply_correction') == '未补正']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('更新time_reply_correction')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=120)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_reply_correction'] = str_t
            print('time_reply_correction:', str_t)
        else:
            json['time_reply_correction'] = ''
    # 如果循环到time_sh(审核意见时间),且时间长度为8
    # if_sh_df是否审核意见答复为否或空时,才自动更新time_sh_df审核意见答复时间
    elif all([i == 'time_sh', request.POST.get('if_sh_df') == '否']):
        if request.POST.get('num_sh') == '1':
            days = 120
        elif request.POST.get('num_sh') in ['2', '3', '4', '5', '6']:
            days = 60
        else:
            return json
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('更新time_sh_df')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=days)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_sh_df'] = str_t
        else:
            json['time_sh_df'] = ''
    # 如果循环到time_bh(驳回时间),且时间长度为8
    # if_bh是否驳回为否或空时,才自动更新time_claim_for_review复审请求书提交期限
    elif all([i == 'time_bh', request.POST.get('if_bh') == '是']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('更新time_claim_for_review')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=90)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_claim_for_review'] = str_t
            print('time_claim_for_review', str_t)
        else:
            json['time_claim_for_review'] = ''
    # 如果循环到withdraw_no_response(未答复/未办理导致撤回时间),且时间长度为8
    # claim_for_rights_recover恢复权利请求书为未提交或空时,才自动更新time_rec最后恢复时间
    elif all([i == 'withdraw_no_response', request.POST.get('claim_for_rights_recover') == '未提交']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('更新time_rec')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=60)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_rec'] = str_t
            print('time_rec', str_t)
        else:
            json['time_last_recover'] = ''
    # 如果循环到rightNotice_giveUp(放弃取得专利权通知书),且时间长度为8
    # right_recover恢复权利请求书为未提交或空时,才自动更新time_last_recover最后恢复时间
    elif all([i == 'rightNotice_giveUp', request.POST.get('right_recover') == '未提交']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('更新time_last_recover')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=60)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_last_recover'] = str_t
            print('time_last_recover', str_t)
        else:
            json['time_last_recover'] = ''
    # 如果循环到的字段为deadline_pay_nf(年费缴费期限), 且是否按期年费缴纳为否或空
    # 需要进行特殊生成，公式为:年费缴费最近一年+一年的年份与申请时间+一个月的月日部分的组合
    elif all([i == 'deadline_pay_nf', request.POST.get('annualfee_pay_on_schedule') == '否']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            time_pay_nf = request.POST.get('time_pay_nf')
            time_apply = request.POST.get('time_apply')
            # 如果年费缴费最近一年和申请时间都符合格式,计算年费缴费期限
            if all([len(time_apply) == 8, len(time_pay_nf) == 8, time_apply is not None, time_pay_nf is not None]):
                time_pay_nf = datetimeAndStrEachChange(time_pay_nf)
                time_pay_nf = time_pay_nf + datetime.timedelta(days=365)
                str_time_pay_nf = datetimeAndStrEachChange(time_pay_nf)
                time_apply = datetimeAndStrEachChange(time_apply)
                time_apply = time_apply + datetime.timedelta(days=30)
                str_time_apply = datetimeAndStrEachChange(time_apply)
                deadline_pay_nf = str_time_pay_nf[0:4] + str_time_apply[4:8]
                # print('deadline_pay_nf', deadline_pay_nf)
                json.update({'deadline_pay_nf': deadline_pay_nf})
                # 计算滞纳金缴纳期限
                deadline_pay_latefees = datetimeAndStrEachChange(deadline_pay_nf)
                deadline_pay_latefees = deadline_pay_latefees + datetime.timedelta(days=150)
                deadline_pay_latefees = datetimeAndStrEachChange(deadline_pay_latefees)
                json.update({'deadline_pay_latefees': deadline_pay_latefees})
                # print('deadline_pay_latefees', deadline_pay_latefees)
                # print(json)
                # 特殊的，年费缴费期限是经过计算得到的，不是原本前端传来的
                # 因此需要将计算后的结果与滞纳金一起写入json直接返回，不能进入下面的json，否则会被前端传的覆盖掉
                return json
        else:
            json.update({'deadline_pay_nf': ''})
            json.update({'deadline_pay_latefees': ''})
            return json
    # 如果循环到的字段为time_sq(授权时间), 且
    # situation_sq授权情况为已授权或空时,才自动更新time_sq_pay授权最后缴费时间
    elif all([i == 'time_sq', request.POST.get('situation_sq') == '已授权']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('更新time_sq_pay')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=60)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_sq_pay'] = str_t
            print('time_sq_pay', str_t)
        else:
            json['time_last_recover'] = ''
    # 如果是其他普通字段，直接将前端传来的数据写入json即可
    json[i] = v
    return json


def notAutoJudge(request):
    for i, v in request.POST.items():
        # id和tiemJudge不属于可修改内容，跳过
        if i in ['id']:
            continue
        elif 'timeJudge' in i:
            continue
        elif 'file' in i:
            continue
        # 如果自动生成字段在修改专利信息时不为空，根据他们的自动生成触发字段判断要不要将参数对应的值直接存入对应的专利中
        # 如果触发字段判断结果为不写入，忽略参数对应的值
        elif i in ['last_time_pay', 'time_rec', 'time_reply_correction', 'time_sh_df',
                   'time_claim_for_review', 'deadline_pay_latefees', 'time_last_recover', 'time_sq_pay']:
            if all([i == 'last_time_pay', request.POST.get('if_apply_pay') in ['全交', '']]):
                json = {i: v}
            elif all([i == 'time_rec', request.POST.get('if_apply_pay') in ['全交', '']]):
                json = {i: v}
            elif all([i == 'time_reply_correction', request.POST.get('reply_correction') in ['已补正', '']]):
                json = {i: v}
            elif all([i == 'time_sh_df', request.POST.get('if_sh_df') in ['是', '']]):
                json = {i: v}
            elif all([i == 'time_claim_for_review', request.POST.get('if_bh') in ['否', '']]):
                json = {i: v}
            elif all([i == 'deadline_pay_nf', request.POST.get('annualfee_pay_on_schedule') in ['是', '']]):
                json = {i: v}
            elif all([i == 'deadline_pay_latefees', request.POST.get('annualfee_pay_on_schedule') in ['是', '']]):
                json = {i: v}
            elif all([i == 'time_last_recover', request.POST.get('right_recover') in ['已提交', '']]):
                json = {i: v}
            else:
                continue
        # 如果当前循环参数名不是可能手动生成的字段，进入自动生成判断分支
        else:
            json = jsonCreate(i, v, request)
        # print(json)
        kwargs.update(json)


    # 如果要生成的字段为deadline_pay_nf(年费缴费期限)
    # 根据rightNotice_giveUp(放弃取得专利权通知书)、right_recover(恢复权利请求书)来生成

    if i == 'deadline_pay_nf':
        deadline_pay_nf = request.POST.get('deadline_pay_nf')
        if len(re.findall(r'^(\d{8})$', deadline_pay_nf)) != 0:
            if request.POST.get('annualfee_pay_on_schedule') == '否':
                time_pay_nf = request.POST.get('time_pay_nf')
                time_apply = request.POST.get('time_apply')
                # 年费缴费期限=(年费缴费最近一年+一年)后取年与(申请时间+一个月)取月日的组合
                if all([len(time_apply) == 8, len(time_pay_nf) == 8, time_apply is not None, time_pay_nf is not None]):
                    time_pay_nf = datetimeAndStrEachChange(time_pay_nf)
                    time_pay_nf = time_pay_nf + datetime.timedelta(days=365)
                    str_time_pay_nf = datetimeAndStrEachChange(time_pay_nf)
                    time_apply = datetimeAndStrEachChange(time_apply)
                    time_apply = time_apply + datetime.timedelta(days=30)
                    str_time_apply = datetimeAndStrEachChange(time_apply)
                    deadline_pay_nf = str_time_pay_nf[0:4] + str_time_apply[4:8]
                    # print('deadline_pay_nf', deadline_pay_nf)
                    json.update({'deadline_pay_nf': deadline_pay_nf})
                    # 计算滞纳金缴纳期限 = 年费缴费期限 + 五个月
                    deadline_pay_latefees = datetimeAndStrEachChange(deadline_pay_nf)
                    deadline_pay_latefees = deadline_pay_latefees + datetime.timedelta(days=150)
                    deadline_pay_latefees = datetimeAndStrEachChange(deadline_pay_latefees)
                    json.update({'deadline_pay_latefees': deadline_pay_latefees})
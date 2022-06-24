import datetime
import re

from base.timeknow.timeCompute import datetimeAndStrEachChange


def jsonCreate(i, v, request):
    json = {}
    v = v.strip()
    # ���ѭ����time_apply(����ʱ��),��ʱ�䳤��Ϊ8λ
    # if_apply_pay�Ƿ�ɷ�Ϊ����ʱ,�Ÿ���last_time_pay���ɷ�����
    if all([i == 'time_apply', request.POST.get('if_apply_pay') in ['��δ��', '������ѽ���ʵ���δ��']]):
        days = 0
        if request.POST.get('if_apply_pay') == '��δ��':
            days = 60
        elif request.POST.get('if_apply_pay') == '������ѽ���ʵ���δ��':
            days = 365 * 3
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('����last_time_pay')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=days)
            recdate_t = date_t + datetime.timedelta(days=60)
            str_t = datetimeAndStrEachChange(date_t)
            json['last_time_pay'] = str_t
            print('last_time_pay:', str_t)
            # ���ָ�ʱ����ڵ�һ�δ�ʱ��Ҫ��4���£������������£�������ԭ���Ѿ����������£�����ټ�������
            str_t = datetimeAndStrEachChange(recdate_t)
            json['time_rec'] = str_t
            print('time_rec', str_t)
        else:
            json['last_time_pay'] = ''
            json['time_rec'] = ''
    # ���ѭ����time_correction(����֪ͨ��ʱ��),��ʱ�䳤��Ϊ8
    # reply_correction�𸴲���֪ͨ��Ϊδ�������ʱ,���Զ�����time_reply_correction����֪ͨ���ʱ��
    elif all([i == 'time_correction', request.POST.get('reply_correction') == 'δ����']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('����time_reply_correction')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=120)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_reply_correction'] = str_t
            print('time_reply_correction:', str_t)
        else:
            json['time_reply_correction'] = ''
    # ���ѭ����time_sh(������ʱ��),��ʱ�䳤��Ϊ8
    # if_sh_df�Ƿ���������Ϊ����ʱ,���Զ�����time_sh_df��������ʱ��
    elif all([i == 'time_sh', request.POST.get('if_sh_df') == '��']):
        if request.POST.get('num_sh') == '1':
            days = 120
        elif request.POST.get('num_sh') in ['2', '3', '4', '5', '6']:
            days = 60
        else:
            return json
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('����time_sh_df')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=days)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_sh_df'] = str_t
        else:
            json['time_sh_df'] = ''
    # ���ѭ����time_bh(����ʱ��),��ʱ�䳤��Ϊ8
    # if_bh�Ƿ񲵻�Ϊ����ʱ,���Զ�����time_claim_for_review�����������ύ����
    elif all([i == 'time_bh', request.POST.get('if_bh') == '��']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('����time_claim_for_review')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=90)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_claim_for_review'] = str_t
            print('time_claim_for_review', str_t)
        else:
            json['time_claim_for_review'] = ''
    # ���ѭ����withdraw_no_response(δ��/δ�����³���ʱ��),��ʱ�䳤��Ϊ8
    # claim_for_rights_recover�ָ�Ȩ��������Ϊδ�ύ���ʱ,���Զ�����time_rec���ָ�ʱ��
    elif all([i == 'withdraw_no_response', request.POST.get('claim_for_rights_recover') == 'δ�ύ']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('����time_rec')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=60)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_rec'] = str_t
            print('time_rec', str_t)
        else:
            json['time_last_recover'] = ''
    # ���ѭ����rightNotice_giveUp(����ȡ��ר��Ȩ֪ͨ��),��ʱ�䳤��Ϊ8
    # right_recover�ָ�Ȩ��������Ϊδ�ύ���ʱ,���Զ�����time_last_recover���ָ�ʱ��
    elif all([i == 'rightNotice_giveUp', request.POST.get('right_recover') == 'δ�ύ']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('����time_last_recover')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=60)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_last_recover'] = str_t
            print('time_last_recover', str_t)
        else:
            json['time_last_recover'] = ''
    # ���ѭ�������ֶ�Ϊdeadline_pay_nf(��ѽɷ�����), ���Ƿ�����ѽ���Ϊ����
    # ��Ҫ�����������ɣ���ʽΪ:��ѽɷ����һ��+һ������������ʱ��+һ���µ����ղ��ֵ����
    elif all([i == 'deadline_pay_nf', request.POST.get('annualfee_pay_on_schedule') == '��']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            time_pay_nf = request.POST.get('time_pay_nf')
            time_apply = request.POST.get('time_apply')
            # �����ѽɷ����һ�������ʱ�䶼���ϸ�ʽ,������ѽɷ�����
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
                # �������ɽ��������
                deadline_pay_latefees = datetimeAndStrEachChange(deadline_pay_nf)
                deadline_pay_latefees = deadline_pay_latefees + datetime.timedelta(days=150)
                deadline_pay_latefees = datetimeAndStrEachChange(deadline_pay_latefees)
                json.update({'deadline_pay_latefees': deadline_pay_latefees})
                # print('deadline_pay_latefees', deadline_pay_latefees)
                # print(json)
                # ����ģ���ѽɷ������Ǿ�������õ��ģ�����ԭ��ǰ�˴�����
                # �����Ҫ�������Ľ�������ɽ�һ��д��jsonֱ�ӷ��أ����ܽ��������json������ᱻǰ�˴��ĸ��ǵ�
                return json
        else:
            json.update({'deadline_pay_nf': ''})
            json.update({'deadline_pay_latefees': ''})
            return json
    # ���ѭ�������ֶ�Ϊtime_sq(��Ȩʱ��), ��
    # situation_sq��Ȩ���Ϊ����Ȩ���ʱ,���Զ�����time_sq_pay��Ȩ���ɷ�ʱ��
    elif all([i == 'time_sq', request.POST.get('situation_sq') == '����Ȩ']):
        if len(re.findall(r'^(\d{8})$', v)) != 0:
            print('����time_sq_pay')
            date_t = datetimeAndStrEachChange(v)
            date_t = date_t + datetime.timedelta(days=60)
            str_t = datetimeAndStrEachChange(date_t)
            json['time_sq_pay'] = str_t
            print('time_sq_pay', str_t)
        else:
            json['time_last_recover'] = ''
    # �����������ͨ�ֶΣ�ֱ�ӽ�ǰ�˴���������д��json����
    json[i] = v
    return json


def notAutoJudge(request):
    for i, v in request.POST.items():
        # id��tiemJudge�����ڿ��޸����ݣ�����
        if i in ['id']:
            continue
        elif 'timeJudge' in i:
            continue
        elif 'file' in i:
            continue
        # ����Զ������ֶ����޸�ר����Ϣʱ��Ϊ�գ��������ǵ��Զ����ɴ����ֶ��ж�Ҫ��Ҫ��������Ӧ��ֱֵ�Ӵ����Ӧ��ר����
        # ��������ֶ��жϽ��Ϊ��д�룬���Բ�����Ӧ��ֵ
        elif i in ['last_time_pay', 'time_rec', 'time_reply_correction', 'time_sh_df',
                   'time_claim_for_review', 'deadline_pay_latefees', 'time_last_recover', 'time_sq_pay']:
            if all([i == 'last_time_pay', request.POST.get('if_apply_pay') in ['ȫ��', '']]):
                json = {i: v}
            elif all([i == 'time_rec', request.POST.get('if_apply_pay') in ['ȫ��', '']]):
                json = {i: v}
            elif all([i == 'time_reply_correction', request.POST.get('reply_correction') in ['�Ѳ���', '']]):
                json = {i: v}
            elif all([i == 'time_sh_df', request.POST.get('if_sh_df') in ['��', '']]):
                json = {i: v}
            elif all([i == 'time_claim_for_review', request.POST.get('if_bh') in ['��', '']]):
                json = {i: v}
            elif all([i == 'deadline_pay_nf', request.POST.get('annualfee_pay_on_schedule') in ['��', '']]):
                json = {i: v}
            elif all([i == 'deadline_pay_latefees', request.POST.get('annualfee_pay_on_schedule') in ['��', '']]):
                json = {i: v}
            elif all([i == 'time_last_recover', request.POST.get('right_recover') in ['���ύ', '']]):
                json = {i: v}
            else:
                continue
        # �����ǰѭ�����������ǿ����ֶ����ɵ��ֶΣ������Զ������жϷ�֧
        else:
            json = jsonCreate(i, v, request)
        # print(json)
        kwargs.update(json)


    # ���Ҫ���ɵ��ֶ�Ϊdeadline_pay_nf(��ѽɷ�����)
    # ����rightNotice_giveUp(����ȡ��ר��Ȩ֪ͨ��)��right_recover(�ָ�Ȩ��������)������

    if i == 'deadline_pay_nf':
        deadline_pay_nf = request.POST.get('deadline_pay_nf')
        if len(re.findall(r'^(\d{8})$', deadline_pay_nf)) != 0:
            if request.POST.get('annualfee_pay_on_schedule') == '��':
                time_pay_nf = request.POST.get('time_pay_nf')
                time_apply = request.POST.get('time_apply')
                # ��ѽɷ�����=(��ѽɷ����һ��+һ��)��ȡ����(����ʱ��+һ����)ȡ���յ����
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
                    # �������ɽ�������� = ��ѽɷ����� + �����
                    deadline_pay_latefees = datetimeAndStrEachChange(deadline_pay_nf)
                    deadline_pay_latefees = deadline_pay_latefees + datetime.timedelta(days=150)
                    deadline_pay_latefees = datetimeAndStrEachChange(deadline_pay_latefees)
                    json.update({'deadline_pay_latefees': deadline_pay_latefees})
# һ��django�ı���ȷ���Ȳ�ѯ
# ģ��(��)�洢���ı�̫��ʱ�����ֱ����=���в�ѯ����ʹƥ���ı������ݡ����͡����ȶ�һ�����ǻ��ѯ������
# ���磺ADdraft = AuditDraft.objects.filter(title=title, content=content)
# ��ʹtitle��content��ȷ�϶�Ӧ���ˣ����ؽ������Ϊ��
# ����취��content�������ݸ�Ϊ�����ݳ��Ƚ���ƥ�䣬title��Ϊ��һ��ѯ������С��Χ
# ���յõ�: ADdraft = AuditDraft.objects.filter(title=title, content__iregex=par1)
# iregex����Сд�����е��жϵ��ж�ĳ�ֶε�ֵ�Ƿ�����������ʽ��������par1 = r'^.{%s}$' % (len(savetext)) {}����Ҫƥ����ı�����

# �������������ѯ
#

# -*-encoding:utf-8-*-

import string

# ���д�д+СдӢ����ĸ,str
s1 = string.ascii_letters
print(s1)
print(type(s1))
# ����СдӢ����ĸ
s2 = string.ascii_lowercase
print(s2)
print(type(s2))
# ���д�дӢ����ĸ
s3 = string.ascii_uppercase
print(s3)
# 0-9
s4 = string.digits
# ������
s5 = string.punctuation
print(s5)
# 0-9a-fA-F(ʮ�������ַ�)
s6 = string.hexdigits
print(s6)
# 0-9a-zA-Z������(���пɴ�ӡ�ַ�)
s7 = string.printable
print(s7)
# ��ȡ���еİ˽��ƽ��������ַ�
s8 = string.octdigits
print(s8)


# ����ĳ��λ��
# .insert(λ��int������Ķ���str)
# .strip()����ȥ���ַ����еĿո�
# .join() �������ڽ������е�Ԫ����ָ�����ַ���������һ���µ��ַ�����
#
# title() �����ַ����ı���汾������������ĸ��д������ĸСд
# upper() �����ַ���ȫ����д�İ汾
# lower() �����ַ�����ȫ��Сд�汾
# swapcase() �����ַ�����Сд������İ汾
# isalnum() ��������ַ��Ƿ�ֻ����ĸ������
# isalpha() ����ַ���֮���Ƿ�ֻ����ĸ
# ǰ���is���Ա�Ϊ�жϷ���
#
# find() �ܰ������ҵ���һ��ƥ������ַ�����û���ҵ��򷵻� -1
#
# z = s[::-1] #��������ַ���s ���е������γ��µ��ַ���z
#
# ��ʽ����������
# * %s �ַ������� str() ���������ַ���ת����
# * %r �ַ������� repr() ���������ַ���ת����
# * %d ʮ��������
# * %f ������
# * %% �ַ� %



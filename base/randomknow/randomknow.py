# -*-encoding:utf-8-*-
import string
import random

# ����1~255֮�������һ������
r1 = random.randint(1, 255)
# print(r1)
# �ӿɵ����������������ȡָ��������
l1 = string.hexdigits
l2 = [1, 2, 3, 4, 5]
r2 = random.sample(l2, 5)
# print(r2)
# ����0~1֮������������
r3 = random.random()
# print(r3)
# ����ָ����Χ�ĸ�����
r4 = random.uniform(0.1, 0.5)
# print(r4)
# ���������е����Ԫ��
l3 = [1, 2, 3, 4]
r5 = random.choice(l3)
# print(r5)
# ��һ�������е�Ԫ�أ��������
random.shuffle(l3)
# print(l3)
# ��ָ����Χ��,��ָ�����������ļ�����,��ȡһ�������.
# �൱�ڴ�[10, 12, 14, 16, ... 96, 98]�����л�ȡһ�������
r6 = random.randrange(10, 100, 2)
print(r6)
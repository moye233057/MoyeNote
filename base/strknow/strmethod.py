def JudgePalindrome(string):
    # �ж�һ���ַ����ǲ��ǻ��Ĵ�
    z = string[::-1]  # ��������ַ���s ���е������γ��µ��ַ���z
    if string == z:
        print("Yes")
    else:
        print("No")


def Judgeimportword():
    # һ����������СдӢ���ַ����ַ��������ַ������ܲ��ǻ��Ĵ���
    # �������ַ���β���������������������ַ���ʹ���ַ�����ɻ��Ĵ���
    # ��������Եõ�����̻��Ĵ���
    n = int(input())
    wc = dict()
    for _ in range(n):
        word = input().strip()
        if word not in wc:
            wc[word] = 1
        else:
            wc[word] += 1
    count = 0
    for w in wc:
        if wc[w] / n >= 0.01:
            count += 1
    print(count)


def createleastrome(s):
    # ���ұ߽�
    l, r = 0, len(s) - 1
    # mark��¼���Ĳ��ֵĿ�ʼλ��
    mark = -1
    while l <= r:
        # �����˿�ʼ��飬������˵��ַ���ȣ���lָ�������ƶ���rָ�������ƶ�
        if s[l] == s[r]:
            mark = l if mark == -1 else mark
            l += 1
            r -= 1
            continue
        # ����ԭʼ�ַ������ǻ��Ĵ�
        if mark != -1:
            l = mark + 1
            mark = -1
            r = len(s) - 1
        else:
            l += 1
    # ���mark��0����ʾԭ�����ַ������ǻ��Ĵ�(���Ĵ�������0��ʼ)
    if mark >= 0:
        # mark����0��ʱ���Ҫ��0~mark-1�Ĳ��ַ�ת��ƴ����ԭʼ�ַ�������
        s += s[:mark][::-1]
    else:
        # ���mark��-1�����ʾԭʼ�ַ�����ȫû�л��ĵĲ��֣�ֱ�ӽ�ԭʼ�ַ�����תƴ���ں���
        s += s[:-1][::-1]
    return s


def insertstring(s, n):
    """
    Args:
        s: ��������ַ���,str
        n: Ҫ�����λ��,int
    Returns:out,�������ݺ���ַ���
    """
    li = list(s)
    length = len(s)
    out = ""
    if n > length:
        out = s
        out += "-"
    else:
        li.insert(n, '-')
        for l in li:
            out += l
    return out


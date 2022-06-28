# coding: utf-8

def JudgePalindrome(string):
    # 判断一个字符串是不是回文串
    z = string[::-1]  # 把输入的字符串s 进行倒序处理形成新的字符串z
    if string == z:
        print("Yes")
    else:
        print("No")


def Judgeimportword():
    # 一个仅包含大小写英文字符的字符串，该字符串可能不是回文串。
    # 可以在字符串尾部加入任意数量的任意字符，使其字符串变成回文串。
    # 计算出可以得到的最短回文串。
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


# 将一个字符串复制为回文字符串
def createleastrome(s):
    # 左右边界
    l, r = 0, len(s) - 1
    # mark记录回文部分的开始位置
    mark = -1
    while l <= r:
        # 从两端开始检查，如果两端的字符相等，则l指针向右移动，r指针向左移动
        if s[l] == s[r]:
            mark = l if mark == -1 else mark
            l += 1
            r -= 1
            continue
        # 否则原始字符串不是回文串
        if mark != -1:
            l = mark + 1
            mark = -1
            r = len(s) - 1
        else:
            l += 1
    # 如果mark是0，表示原来的字符串就是回文串(回文串从索引0开始)
    if mark >= 0:
        # mark大于0的时候就要将0~mark-1的部分反转后拼接在原始字符串后面
        s += s[:mark][::-1]
    else:
        # 如果mark是-1，则表示原始字符串完全没有回文的部分，直接将原始字符串反转拼接在后面
        s += s[:-1][::-1]
    return s


def insertstring(s, n):
    """
    Args:
        s: 被插入的字符串,str
        n: 要插入的位置,int
    Returns:out,插入数据后的字符串
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


if __name__ == '__main__':
    s = 'aaaaabbbbb'
    res = createleastrome(s)
    print(res)

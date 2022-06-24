import socket
import getpass

user_name = getpass.getuser()  # 获取当前用户名
hostname = socket.gethostname()  # 获取当前主机名
print(type(user_name))
print('C:\\Users\\' + user_name + '\\AppData\Local\Temp\\')
print(hostname)
print(user_name)


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


# from ltp import LTP
# # 1、名词（nouns）n
# # 2、代词（pronoun）pron
# # 3、数词（numeral）Num
# # 4、形容词（adjective）adj
# # 5、副词（adverb）adv
# # 6、动词 (verb)v
# # 7、感叹词(interjection)int
# # 8、
# ltp = LTP()
# sentence ="申报“发明专利产品年销售收入达到300万元以上”奖励项目的14家企业，共14个项目"
# place = []
# seg, hidden = ltp.seg([sentence])
# print(seg)
# s = seg[0]
# #获取文本中的词性关系
# pos = ltp.pos(hidden)
# #提取ns即文本中代表的地点的词
# p = pos[0]
# for index,p2 in enumerate(p):
#     if p2 == 'ns':
#         place.append(s[index])
# print(pos)
# print(place)
#
# # ner = ltp.ner(hidden)
# # print(ner)
#
# #语义角色分析
# srl = ltp.srl(hidden)
# print(srl)
# L = srl[0]
# timeindex = []
# #ARGM-EXT能够提取有关时间的内容
# for l1 in L:
#     for l2 in l1:
#         if 'ARGM-EXT' in l2:
#            timeindex.append(l2)
# print(timeindex)
# if len(timeindex)>1:
#     time = ""
#     for tsplit in s[timeindex[0][1]:timeindex[0][2]+1]:
#        time += tsplit
#     print(time)
#
# # dep = ltp.dep(hidden)
# # print(dep)
#
# #语义依存分析
# sdp = ltp.sdp(hidden)
# sdp = sdp[0]
# print(sdp)
# # moneyindex = []
# # for s in sdp:
# #     print(s)
#     # if 'MEAS' or 'mDEPD' in s :
#     #     moneyindex.append(s)
# # print(moneyindex)


if __name__ == '__main__':
    print(get_host_ip())

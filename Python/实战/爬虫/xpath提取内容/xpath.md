一、从本地html文件中提取一级和二级分类
`ˋ`
from lxml import etree
import pprint
# 本地提取用etree.parse
tree = etree.parse('热点聚焦 - 未来智库.html')
listdiv = tree.xpath('//body/div[2]/div/div')
bigType = []
for i, div in enumerate(listdiv[1:]):
    firstTit = div.xpath('./span/text()')
    # print("大标题:", firstTit)
    uls = div.xpath('./ul')
    for ul in uls:
        secondTit = ul.xpath('./span/text()')
        # print("二级标题:", secondTit)
        lis = ul.xpath('./li/a/text()')
        # print("分类:", lis)
        dictTit = {
            "firstTit": ''.join(secondTit),
            "secondTit": lis
        }
        bigType.append(dictTit)

pprint.pprint(bigType)
`ˋ`
import re
import mammoth


def gettezheng(path):
    tezheng = []
    with open(path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value  # The generated HTML
        t1 = html.replace('<strong>', '').replace('</strong>', '')
        t2 = re.sub('<a(.*?)</a>', '', t1)
        pat = re.compile('<p>((\w|\W)*?)</p>')
        texts = re.findall(pat, t2)
        for index, value in enumerate(texts):
            texts[index] = value[0]
            if value[0].startswith("特征A") and value[0] not in tezheng:
                tezheng.append(value[0])
        docx_file.close()
        return tezheng


if __name__ == '__main__':
    docxpath = "./trizhian.docx"
    tezheng = gettezheng(docxpath)
    for te in tezheng:
        print(te)

# documemnt.element方法提取docx
# from docx import Document
# children = document.element.body.iter()
# child_iters = []
# tezheng = []
# for child in children:
#     # 通过类型判断目录
#     for ci in child.iter():
#         if ci.text == None:
#             continue
#         if ci.text and ci.text.strip():
#             text = ci.text.strip()
#             if "特征A" in text and text not in tezheng:
#                 tezheng.append(text)
#             if text not in child_iters:
#                 child_iters.append(text)
# print(tezheng)
# print(child_iters)

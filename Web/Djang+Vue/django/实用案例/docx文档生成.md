# 包含向下流程图、五书、草稿文件、审核文件的生成
`ˋ`
# coding: utf-8
import os
import re
import string
from datetime import datetime
import random
from infer.usemethod.staticData import getLastSentence
from infer.usemethod.svg_turtle import SvgTurtle
from patentinfer.settings import BASE_DIR
from docx import Document
from docx.shared import Pt, Cm, Mm, RGBColor, Inches
from docx.oxml.ns import qn
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import cairosvg
import svgwrite
from turtle import *


# 保存前端传来的文件
def savefile(file, save_path):
    f = open(save_path, 'wb')
    for chunk in file.chunks():
        f.write(chunk)
    f.close()


# 读取docx
def readdocx(docxpath):
    wordfile = Document(docxpath)  # 读入文件
    paragraphs = wordfile.paragraphs
    # 输出每一段的内容
    content = []
    for index, paragraph in enumerate(paragraphs):
        content.append(paragraph.text.replace(' ', '').replace('\n', ''))
    return content


# 五书图片生成类
class WritePicture:
    def __init__(self, filename, quans, ids, canvasx="720px", canvasy="2160px"):
        self.filename = filename  # 文件名
        self.quans = quans  # 权利要求列表
        self.ids = ids  # id列表
        self.cx = canvasx  # 画布宽度
        self.cy = canvasy  # 画布长度

    # 向矩形内填充文字
    @staticmethod
    def writesquareword(quan, cutnum, startwordx, startwordy, align):
        quan = quan.strip('；')
        # print(quan)
        if cutnum > 0:
            for i in range(cutnum + 1):
                penup()  # 提笔移动
                goto(startwordx, startwordy)  # 画笔移动到该位置
                pendown()  # 笔降落
                l = 25 * i
                r = 25 * (i + 1)
                # print(l, r)
                q1 = quan[l:r]
                write(q1, move=False, align=align, font=('SimHei', 22, 'normal'))
                startwordy = startwordy - 50
        else:
            penup()  # 提笔移动
            goto(startwordx, startwordy)  # 画笔移动到该位置
            pendown()  # 笔降落
            write(quan, move=False, align=align, font=("SimHei", 22, 'normal'))

    # startwordx字的起始x坐标；startwordy字的起始y坐标；startjux矩形的起始x坐标；
    # startjuy矩形的起始y坐标；juxlength矩形长度；juylength矩形宽度
    def SquareTreeWrite(self, align, startwordx, startwordy, startjux=-500, startjuy=950, juxlength=1000):
        thistime = datetime.now().strftime('%Y%m%d%H%M%S%f')  # 获取当前时间戳
        midfilename = 'media/png/' + self.filename + str(thistime)  # 拼接相对文件路径
        drawing = svgwrite.Drawing(midfilename, size=(self.cx, self.cy))  # 新建一张画布并设置其大小
        drawing.add(drawing.rect(fill='white', size=("100%", "100%")))  # 添加一个矩形在画布上
        t = SvgTurtle(drawing)  # 设置海龟做图模型
        Turtle._screen = t.screen
        Turtle._pen = t

        speed(8)  # 设置画笔移速度
        pensize(5)  # 设置画笔第大小
        color("black", 'white')
        # print('-'*10)
        # print(self.quans)
        # 书写每一个矩形中的内容，一个权利要求对于一个矩形
        for index, quan in enumerate(self.quans):
            juylength = 50  # !!!对每一个文字输入框都要重置它的宽
            home()  # 画笔移动初始位置
            length = len(quan)
            # print("文本长度：", length)
            # 一行放25个字
            cutnum = int(length / 25)
            # print("切割份数：", cutnum)
            # print('起始位置：', pos())

            begin_fill()  # 开始绘制
            penup()  # 提笔
            goto(startjux, startjuy)  # 移动到开始位置
            pendown()  # 落笔
            # 画矩形，如果cutnum==0，说明当前标题只需要一行放置，初始长度为50即可
            # 如果cutnum>0，说明当前标题大于25个字，要进行换行，cutnum可以认为是多出来的行数，每多一行矩形y轴长多50
            if cutnum > 0:
                juylength = juylength + cutnum * 50
            else:
                juylength = 50
            for x in range(1, 5):
                if x % 2 == 1:
                    n = juxlength
                else:
                    n = juylength
                forward(n)
                right(90)
            end_fill()
            # 画矩形中的的字
            self.writesquareword(quan, cutnum, startwordx, startwordy, align)
            # 画向下箭头的直线部分
            penup()
            liney = startjuy - juylength
            goto(0, liney)
            # print("直线起点位置：", pos())
            # 画向下箭头的箭头部分
            if index != len(self.quans) - 1:
                pensize(3)
                pendown()
                right(90)
                begin_fill()  # 开始填充
                forward(100)
                goto(-15, liney - 80)
                penup()
                goto(0, liney - 100)
                pendown()
                goto(15, liney - 80)
                penup()
                pensize(5)
                end_fill()
            # 设置下一个矩形的起始坐标
            startjuy = startjuy - juylength - 100
            startwordy = startwordy - juylength - 100
            drawing.save()

        # 将生成的初始图像文件转化为png格式
        pngpath = os.path.join(BASE_DIR, 'media/png/', self.filename + thistime + '.png')
        cy1 = 600  # 输出图片宽度
        cx1 = 325  # 输出图片高度
        cairosvg.svg2png(url=midfilename, write_to=pngpath, output_width=cx1, output_height=cy1)
        # cairosvg.svg2png(url=filename, write_to=pngpath, output_width=473, output_height=622)

        return pngpath, midfilename


class FiveBook:
    def __init__(self, ids, tits, cons, title='报告', username='nouser'):
        self.title = title
        self.username = username
        self.lastflag = 0  # 根据最后一段判断是否要进行说明书附图书写的标志位(模块...用于句型)
        self.ids = ids
        self.tits = tits
        self.cons = cons

        # 判断最后一段正文中模块和用于两个词的个数，如果都大于三，说明需要进行说明书附图书写
        # 当lastflag==1的时候证明需要书写说明书附图，且权利要求书最后一段要进行系统处理
        try:
            lastcon = cons[-1]
            mokuainum = lastcon.count('模块')
            yongyunum = lastcon.count('用于')
            if mokuainum > 3 and yongyunum > 3:
                self.lastflag = 1
            self.lastcon = lastcon
        except:
            print('可能没有生成对应图片或者没有正文')

        # 权利要求一写入文本预处理
        quan1 = []  # 权1标题，包含每个文本框标题，特殊处理文本，用于写入权利要求书
        quanpic = []  # 权1标题，包含每个文本框标题，末尾为分号，用于生成附图

        # 由于ids中还包含了背景和有益的id,因此ids的索引比标题列表应该多两位
        for i, tit in enumerate(tits):
            id = ids[i + 2]
            countthis = len(id.split('-'))
            # 对标题为空和模块用于权要不进行处理
            if len(tit) < 1:
                continue
            if self.lastflag == 1 and i == len(tits) - 1:
                continue
            t = tit.strip('。').strip(',')
            # quanpic保存主id+；
            if countthis < 2:
                quanpic.append(t + '；')
            # 权1特殊文本处理
            try:
                # 判断当前id的下一个id类型
                nextid = ids[i + 3]
                countnext = len(nextid.split('-'))
                # 如果当前id为主id，下一个id为子id，需要在主id标题后面添加所述字段
                if countthis < 2 and countnext >= 2:
                    try:
                        nnid = ids[i + 4]
                        t = t + '，'
                        try:
                            # 如果主id后面有多个子id，加上所述+主id标题+具体包括
                            if len(nnid.split('-')) >= 2:
                                t += '所述' + t + '具体包括：'
                            # 如果主id后面只有一个子id，只加上具体包括
                            else:
                                t += '具体包括：'
                        except:
                            pass
                    except:
                        t = t + '，包括：'
                # 如果当前id为子id，下一个id也为子id，标题后接逗号
                if countthis >= 2 and countnext >= 2:
                    t = t + '，'
                # 如果下一个id为主id，标题后接分号
                if countnext < 2:
                    t = t + '；'
            except:
                # 如果后面没有id，标题后接句号
                t = t + '。'
            quan1.append(t)

        self.quan1 = quan1
        self.quanpic = quanpic

    # 设置间距和缩进，放在文档开头
    @staticmethod
    def setparaformat(para):
        # 设置行前后间距,行间距
        para.paragraph_format.space_before = Pt(0)
        para.paragraph_format.space_after = Pt(0)
        para.paragraph_format.line_spacing = Pt(24)
        # 设置首行缩进
        para.first_line_indent = para.style.font.size * 2

    # 设置纸张格式，放在文档结尾
    @staticmethod
    def setsectionformat(doc):
        for sec in doc.sections:
            # 设置页面边距(左上25毫米，右下15毫米)
            sec.top_margin = Cm(2.5)
            sec.left_margin = Cm(2.5)
            sec.right_margin = Cm(1.5)
            sec.bottom_margin = Cm(1.5)
            # 设置纸张大小(A4)
            sec.page_height = Mm(297)
            sec.page_width = Mm(210)
            # 设置页眉页脚距离
            sec.header_distance = Cm(1.5)
            sec.footer_distance = Cm(0.2)

    # 字符串结尾标点检测
    @staticmethod
    def checklastmark(titorcon, mark):
        """
        :param titorcon:标题或者正文的字符串文本。str
        :param mark: 对字符串最后替换或加上的标点符号。str
        :return: 末尾替换为指定标点符号的字符串文本。str
        1、判断字符串的最后一位是不是中文
        2、如果是直接在后面加上指定标点符号
        3、如果不是，先截取字符串，范围为开头到倒数第二位字符，再在后面加上指定字符
        """
        if len(titorcon) > 0:
            # if '\u4ee0' <= titorcon[-1] <= '\u9fa5':
            #     titorcon += str(mark)
            # el
            if titorcon[-1].isalpha():
                titorcon += str(mark)
            else:
                titorcon = titorcon[:-1]
                titorcon += str(mark)
            # 若出现两个标点连一起的情况，去除其中一个
            titorcon.replace(mark + mark, mark)
        else:
            titorcon.replace(mark + mark, mark)
        return titorcon

    # 是否要插入图片判断
    @staticmethod
    def pictureJudge(para, doc, uid, title, line):
        """
        :param para: 段落对象
        :param doc: 文档对象
        :param uid: 专利id
        :param title: 标题列表
        :param line: 要插入图片的文本
        :return: para: 最后创建的para对象
        """
        # print('进入图片判断:', 'pic' in line)
        # 说明书的标题会多出"一种"和"方法"两个词，存储图片的文件名不带有一种、方法，需要除去
        title = title.replace('方法', '').replace('一种', '')
        # 构建图片标签正则。图片标签格式是：{pic}图片名{/pic}
        part = re.compile(r'\{pic\}(.*?)\{/pic\}')
        # 判断图片标签在不在正文中，在的话要根据标签寻找插入位置，不在则直接写入整个文本
        if 'pic' in line:
            # 首行缩进
            para.add_run(u'    ')
            # 找到所有标签中的图片名称
            res = re.findall(part, line)
            # print('有图片：', res)
            for index, name in enumerate(res):
                # 根据标签切开文本
                picline = line.split('{pic}' + name + '{/pic}')
                # 构建获取图片的路径
                filepath = 'media/insertimages/{}/{}'.format(uid + title, name)
                # 写入插入图片前的文本
                para = doc.add_paragraph()
                if index == 0:
                    para.add_run('    ' + picline[0])
                else:
                    para.add_run(picline[0])
                # print('插入文本：', picline[0])
                # 写入图片，并将图片设置为居中
                try:
                    # print('插入图片：', filepath)
                    paragraph = doc.add_paragraph()
                    # 图片居中设置
                    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                    run = paragraph.add_run("")
                    run.add_picture(filepath, width=Inches(2))
                    line = picline[1]
                    # print('插入成功')
                except Exception as e:
                    print(e)
            # # 如果图片都写入完了，可能还剩最后一个图片后面的文本没写入，最后写入
            # lastline = line.split('{pic}' + res[-1] + '{/pic}')[-1]
            para = doc.add_paragraph()
            para.add_run(line)
        else:
            # 如果没有pic标签，直接写入文本
            line = line.strip()
            para = doc.add_paragraph()
            para.add_run(u'    ' + line)
        return para

    # 正文换行检测
    @staticmethod
    def checkchangeline(con, doc, uid, title, para):
        """
        :param con:字符串文本。str
        :param para: docx库段落元素。
        1、对输入的文本统计其换行符的个数
        2、如果换行符个数大于0,对文本以换行符进行切割
        3、对切割后的数组进行遍历，每一个切割文本单独加上缩进写入段落中
        4、如果没有换行符，判断有没有图片标签，有的话插入图片
        5、没有图片标签直接加上缩进写入段落中
        """
        if len(con) > 0:
            linenum = con.count('\n')
            lines = []
            if linenum > 0:
                lines = con.split('\n')
            if len(lines) > 1:
                for i, line in enumerate(lines):
                    para = FiveBook.pictureJudge(para, doc, uid, title, line)
            else:
                para = doc.add_paragraph()
                if 'pic' in con:
                    para = FiveBook.pictureJudge(para, doc, uid, title, con)
                else:
                    para.add_run('    ' + con + '')
        return para

    # 正文手动换行检测
    @staticmethod
    def checkintidline(con, para, ids, uid, title, doc):
        """
        :param con: 正文列表
        :param para: 段落对象
        :param ids: id列表
        :param uid: 专利id
        :param title: 正文标题列表
        :param doc: 文档对象
        :return: para 最后创建的para对象
        """
        # 判断正文有没有手动换行，有的话拆分并对被换行正文加缩进
        if len(con) > 0:
            linenum = con.count('\n')
            lines = []
            if linenum > 0:
                lines = con.split('\n')
            if len(lines) > 1:
                for i, line in enumerate(lines):
                    para = FiveBook.pictureJudge(para, doc, uid, title, line)
            else:
                try:
                    para = FiveBook.pictureJudge(para, doc, uid, title, con)
                except:
                    # 对含有特殊字符的段落进行清洗，去除无效字符
                    def str_to_int(s, default, base=10):
                        if int(s, base) < 0x10000:
                            return chr(int(s, base))
                        return default

                    html = re.sub(u"&#(\d+);?", lambda c: str_to_int(c.group(1), c.group(0)), con)
                    html = re.sub(u"&#[xX]([0-9a-fA-F]+);?", lambda c: str_to_int(c.group(1), c.group(0), base=16),
                                  html)
                    html = re.sub(u"[\x00-\x08\x0b\x0e-\x1f\x7f]", "", html)
                    para = FiveBook.pictureJudge(para, doc, uid, title, html)
            try:
                nextid = ids[i + 3]
                countnext = len(nextid.split('-'))
                if countnext < 2:
                    para.add_run('')
            except:
                # print('没有下一个id')
                pass
        return para

    # 提取放在主id正文后面的子id标题
    @staticmethod
    def fenziinclude(ids, tits, i, doc, para, con='zhanwei'):
        """
        :param ids: id列表。list。
        :param tits: 标题列表。list。
        :param i: 五书权利要求书和说明书中对标题循环的位置。int。
        1、ids的结构为[1,1-1,1-2,2,2-1,3,4，...]
        2、进入该函数时默认循环运行到了整数id，即1、2、3...，目的是找到所有分支id的标题
        3、若有分支id，利用异常捕获，当获取不到分支id时跳出(若开头id为整数如1，调用一次，该函数只会判断到1-2，直到整数2才会再次进入该函数)
        4、对分支id判断'-'的个数，若个数大于等于2，则将其对应标题写入behindtits，最后循环写入para
        """
        idslen = len(ids)
        behindtits = []
        for j in range(idslen - i - 2):
            try:
                nextid = ids[i + 3 + j]
            except:
                break
            countnext = len(nextid.split('-'))
            if countnext >= 2:
                nexttit = tits[i + 1 + j].strip('。').strip()
                behindtits.append(nexttit)
            else:
                # print('没有子序号')
                break
        if len(behindtits) > 0:
            # para = doc.add_paragraph()
            if len(con) > 0:
                para.add_run('；包括：')
            for tit in behindtits:
                para.add_run(tit + '；')
        elif len(con) > 0:
            para.add_run('。')
        return para

    # 设置字体和标题
    @staticmethod
    def docxinitial(doc, name):
        """
        :param doc: 文档对象
        :param name:  专利名称
        """
        # 设置正文字体类型、大小
        doc.styles["Normal"].font.name = u'宋体'
        doc.styles["Normal"].font.size = Pt(12)
        doc.styles["Normal"]._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
        # 设置页眉
        header = doc.sections[0].header
        pheader = header.paragraphs[0]  # 获取页眉的第一个段落
        ph = pheader.add_run(name)
        ph.font.name = u'黑体'  # 设置页眉字体样式
        ph._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体')
        ph.font.size = Pt(16)  # 设置页眉字体大小
        ph.bold = True  # 页眉字体加粗
        pheader.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 页眉对齐方式设为居中

    # 写权利要求书
    def claims(self, doc, uid):
        """
        :param doc: 文档对象
        :param uid:  专利id
        """
        title = self.title
        ids = self.ids
        tits = self.tits
        cons = self.cons
        # 初始化五书格式
        self.docxinitial(doc, '权利要求书')
        # 创建段落
        para = doc.add_paragraph()
        # 设置段落基本属性
        self.setparaformat(para)
        # 开始正文内容输入
        # 输入权利要求段落
        para.add_run('    1. ').bold = True
        para.add_run(str(self.title).replace('与系统', '') + '，其特征在于，所述方法包括：')
        para = doc.add_paragraph()
        para.add_run(u'    ' + ''.join(self.quan1) + '')
        # 按根据当前id是主id还是子id对每个输入框进行书写
        for i, tit in enumerate(tits):
            id = ids[i + 2]
            count = len(id.split('-'))
            # 清洗标题，去除句号和空格
            t = tit.strip('。').strip()
            # 如果用'-'切开得到的列表长度小于2，说明当前id为主id
            if count < 2:
                if len(t) > 0:
                    # 如果当前索引是最后一段，进入系统:模块段落判断，根据五书初始化结果确定最后一段的标题写入格式
                    if i == len(tits) - 1:
                        if self.lastflag == 1:
                            para = doc.add_paragraph()
                            para.add_run(u'    {}. '.format(str(int(id) + 1))).bold = True
                            para.add_run(self.title.replace('方法与', '') + '，其特征在于，所述系统包括:')
                        else:
                            para = doc.add_paragraph()
                            para.add_run(u'    {}. '.format(str(int(id) + 1))).bold = True
                            para.add_run(u'根据权利要求1所述的方法，其中，所述' + t + '，包括:')
                    # 不是最后一段，按以下格式写入当前标题
                    else:
                        para = doc.add_paragraph()
                        para.add_run(u'    {}. '.format(str(int(id) + 1))).bold = True
                        para.add_run(u'根据权利要求1所述的方法，其中，所述' + t + '，包括:')
                # 写入当前标题对应的正文
                if len(cons[i]) > 0:
                    con = cons[i]  # 获取当前索引对应的正文
                    con = re.sub('例如.*', '', con)  # 去掉例如部分
                    con = con.strip()  # 去掉左右空格
                    con = re.sub('。', '；', con)  # 将句号全部替换为分号
                    con = re.sub(r'\s+', '', con)  # 去除中间多余空格
                    con = self.checklastmark(con, '')  # 结尾标点处理
                    # para = doc.add_paragraph()
                    para = self.checkintidline(con, para, ids, uid, title, doc)  # 手动换行处理
                    para = self.fenziinclude(ids, tits, i, doc, para, con)  # 主id提取子id标题，放在正文后。包括：子id标题1，子id标题2...
            else:
                # 如果当前id为子id，直接写入正文
                con = cons[i]
                con = re.sub('例如.*', '', con)
                con = con.strip()
                con = re.sub('。', '；', con)
                try:
                    nextid = ids[i + 3]
                    countnext = len(nextid.split('-'))
                    # 如果子id的下一个id是主id，这个子id对应的正文结尾才可以是句号，否则是分号
                    if countnext < 2:
                        con = self.checklastmark(con, '。')
                    else:
                        con = self.checklastmark(con, '；')  # 结尾标点处理，默认为分号
                except:
                    con = self.checklastmark(con, '。')
                para = doc.add_paragraph()
                para.add_run('    所述' + t + '，具体包括:')
                para = doc.add_paragraph()
                # 手动换行判断，检测到有换行符进行切分并将切分后的段落加上两格缩进
                linenum = con.count('\n')
                lines = []
                if linenum > 0:
                    lines = con.split('\n')
                if len(lines) > 1:
                    for i, line in enumerate(lines):
                        line = line.strip()
                        para = FiveBook.pictureJudge(para, doc, uid, title, line)
                else:
                    if 'pic' in con:
                        para = FiveBook.pictureJudge(para, doc, uid, title, con)
                    else:
                        para.add_run('    ' + con + '')
        self.setsectionformat(doc)

    # 写说明书
    def instruction(self, doc, jishu, youyi, exas, uid):
        """
        :param doc: 文档对象
        :param jishu: 技术背景
        :param youyi: 有益条件
        :param exas: 例子
        :param uid: 专利的id
        """
        ids = self.ids
        title = self.title.replace('与系统', '')
        tits = self.tits
        cons = self.cons
        # 传入说明书方法的列子列表包含了背景和有益的例子，需要去掉
        if len(exas) > 2:
            exas = exas[2:]
        # 初始化五书格式
        self.docxinitial(doc, '说明书')
        # 写标题
        ti = doc.add_paragraph()
        ti.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 居中
        ti1 = ti.add_run(title)
        ti1.font.size = Pt(16)  # 字体大小
        ti1.bold = True  # 加粗

        para = doc.add_paragraph()
        self.setparaformat(para)
        para = doc.add_paragraph()
        para.add_run(u'技术领域').bold = True
        para = doc.add_paragraph()
        para.add_run(u'    本发明涉及信息技术领域，尤其涉及')
        para.add_run(title + u'。')
        para = doc.add_paragraph()
        para.add_run(u'背景技术').bold = True
        jishu = "".join(jishu)
        para = self.checkchangeline(jishu, doc, uid, title, para)
        para = doc.add_paragraph()
        para.add_run(u'发明内容').bold = True
        para = doc.add_paragraph()
        para.add_run(u'    本发明提供了' + title + u'，主要包括：')
        para = doc.add_paragraph()
        para.add_run('    ' + "".join(self.quan1) + '')

        try:
            for i in range(len(tits)):
                id = ids[i + 2]
                count = len(id.split('-'))
                # 去除标题中的标点符号
                t = tits[i].strip(string.punctuation)
                # 对主id
                if count < 2:
                    # 当索引为最后一段时
                    if i == len(tits) - 1:
                        para = doc.add_paragraph()
                        para.add_run(u'    ' + title + '其特征在于，所述系统包括：')
                    # 当索引不是最后一段时
                    elif len(tits[i]) > 0:
                        para = doc.add_paragraph()
                        para.add_run(u'    进一步可选地，所述' + t + '包括：')
                    if len(cons[i]) > 0:
                        con = cons[i]
                        con = con.strip()
                        con = re.sub('。', '；', con)
                        con = re.sub('\s+', '', con)
                        con = self.checklastmark(con, '')  # 结尾标点检测
                        # para = doc.add_paragraph()
                        para = self.checkintidline(con, para, ids, uid, title, doc)  # 手动换行检测
                        para = self.fenziinclude(ids, tits, i, doc, para, con)  # 主id提取子id标题，放在正文后。包括：子id标题1，子id标题2...
                # 对子id
                else:
                    para = doc.add_paragraph()
                    para.add_run('    所述' + t + '，具体包括：')
                    con = cons[i]
                    con = con.strip()
                    con = self.checklastmark(con, '。')
                    para = self.checkchangeline(con, doc, uid, title, para)
        except Exception as e:
            print(e)

        para = doc.add_paragraph()
        para.add_run(u'    本发明实施例提供的技术方案可以包括以下有益效果：')
        para = doc.add_paragraph()
        para.add_run(u'    ' + "".join(youyi) + '')
        para = doc.add_paragraph()
        para.add_run(u'附图说明')
        para = doc.add_paragraph()
        para.add_run(u'    图1为本发明的')
        para.add_run(title)
        para.add_run(u'的流程图。')
        para = doc.add_paragraph()
        para.add_run(u'具体实施方式')
        para = doc.add_paragraph()
        para.add_run(u'    为了使本发明的目的、技术方案和优点更加清楚，下面结合附图和具体实施例对本发明进行详细描述。')
        para = doc.add_paragraph()
        para.add_run(u'    图1为本发明的' + title + u'流程图。如图1所示，本实施例' + title + u'具体可以包括：')
        # 说明书步骤内容
        try:
            for i in range(len(tits)):
                id = ids[i + 2]  # 步骤用的是有益条件下id1开始的标题、正文等，因此要取ids第三位开始的id
                count = len(id.split('-'))  # 统计当前id中'-'的个数
                t = tits[i].strip(string.punctuation)  # 去除标点符号
                if count < 2:
                    if len(tits[i]) > 0:
                        t = t.strip()
                        t = self.checklastmark(t, '。')
                        para = doc.add_paragraph()
                        para.add_run('    步骤10{}，'.format(str(id)) + t + '')
                    # 步骤的具体内容需要同时包含正文和例子
                    if len(cons[i]) > 0:
                        con = cons[i]
                        con = con.strip()
                        exa = exas[i]
                        exa = exa.strip()
                        con = con + exa
                        con = self.checklastmark(con, '。')
                        para = self.checkchangeline(con, doc, uid, title, para)
                else:
                    # 步骤的具体内容需要同时包含正文和例子
                    t = t.strip()
                    t = self.checklastmark(t, '。')
                    con = cons[i]
                    con = con.strip()
                    exa = exas[i]
                    exa = exa.strip()
                    con = con + exa
                    con = self.checklastmark(con, '。')
                    para = doc.add_paragraph()
                    para.add_run('    ' + t + '')
                    para = self.checkchangeline(con, doc, uid, title, para)
        except Exception as e:
            print(e)

        sentences = getLastSentence()
        para = doc.add_paragraph()
        para.add_run('    ' + random.choice(sentences))
        #         u'''    以上所述仅为本发明的实施例，并非因此限制本发明的专利范围，凡是利用本发明说明书及附图内容所作的等效结构或等效流程变换，或直接或间接运用在其它相关的技术领域，均同理包括在本发明的专利保护范围内。
        # 用于实现本发明进行信息控制的程序，可以以一种或多种程序设计语言或其组合来编写用于执行本发明操作的计算机程序代码，所述程序设计语言包括面向对象的程序设计语言—诸如Java、python、C++，还包括常规的过程式程序设计语言—诸如C语言或类似的程序设计语言。
        # 程序代码可以完全地在用户计算机上执行、部分地在用户计算机上执行、作为一个独立的软件包执行、部分在用户计算机上部分在远程计算机上执行、或者完全在远程计算机或服务器上执行。在涉及远程计算机的情形中，远程计算机可以通过任意种类的网络——包括局域网(LAN)或广域网(WAN)—连接到用户计算机，或者，可以连接到外部计算机（例如利用因特网服务提供商来通过因特网连接）。
        # 在本发明所提供的几个实施例中，应该理解到，所揭露的系统，装置和方法，可以通过其它的方式实现。例如，以上所描述的装置实施例仅仅是示意性的，例如，所述单元的划分，仅仅为一种逻辑功能划分，实际实现时可以有另外的划分方式。
        # 所述作为分离部件说明的单元可以是或者也可以不是物理上分开的，作为单元显示的部件可以是或者也可以不是物理单元，即可以位于一个地方，或者也可以分布到多个网络单元上。可以根据实际的需要选择其中的部分或者全部单元来实现本实施例方案的目的。
        # 另外，在本发明各个实施例中的各功能单元可以集成在一个处理单元中，也可以是各个单元单独物理存在，也可以两个或两个以上单元集成在一个单元中。上述集成的单元既可以采用硬件的形式实现，也可以采用硬件加软件功能单元的形式实现。
        # 上述以软件功能单元的形式实现的集成的单元，可以存储在一个计算机可读取存储介质中。上述软件功能单元存储在一个存储介质中，包括若干指令用以使得一台计算机设备（可以是个人计算机，服务器，或者网络设备等）或处理器（processor）执行本发明各个实施例所述方法的部分步骤。
        # 而前述的存储介质包括：U盘、移动硬盘、只读存储器（Read-Only Memory，ROM）、随机存取存储器（Random Access Memory，RAM）、磁碟或者光盘等各种可以存储程序代码的介质。''')
        # 设置纸张和页眉格式
        self.setsectionformat(doc)

    # 写说明书摘要
    def instructionabs(self, doc):
        self.docxinitial(doc, '说明书摘要')
        para = doc.add_paragraph()
        self.setparaformat(para)
        # 等同于权利要求书标题和权一总结部分
        text = ''.join(self.quan1)
        # 如果初始权利要求文本大于300字，进行一次清洗，去除所述...具体包括内容
        if len(text) > 300:
            parn1 = re.compile(r'所述(.*?)具体包括：')
            text = re.sub(parn1, '具体包括:', text)
            # 如果一次清洗后摘要文本仍大于300字，只保留主id标题的部分
            if len(text) > 300:
                parn2 = re.compile(r'，具体包括(.*?)；')
                text = re.sub(parn2, '；', text)
        # 判断组合文本是否大于300字，若大于，逐个去除权利要求中最长的标题，直到整个摘要文本字数小于300字
        protext = '本申请提供' + str(self.title) + u'，包括：' + text
        if len(protext) > 300:
            deletelist = text.split('；')  # 以'；'切割出每个权利要求
            for i in range(len(deletelist) - 1):
                # 找到权利要求中最长的一个
                maxlongstr = max(deletelist, key=len, default='')
                # 从列表中去除
                deletelist.remove(maxlongstr)
                # 再次组成摘要文本判断长度，如果小于300字就写入说明书摘要文档中
                quan1 = '；'.join(deletelist)
                text = '本申请提供' + str(self.title) + u'，包括：' + quan1
                if len(text) < 300:
                    break
            para = doc.add_paragraph()
            para.add_run(text + '')
        else:
            para = doc.add_paragraph()
            para.add_run(protext + '')
        self.setsectionformat(doc)

    # 写摘要附图
    def abspicture(self, doc):
        quan1 = self.quanpic
        ids = self.ids
        # 创建附图本体
        WP1 = WritePicture(self.title, quan1, ids)
        try:
            pngpath, midfilename = WP1.SquareTreeWrite('left', -450, 900)
        except:
            return
        # 将附图写入文件
        doc.add_picture(pngpath)
        # 划定下标“图一”的区域
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        para = doc.add_paragraph()
        para.add_run('                                      图1').bold = True
        self.setsectionformat(doc)
        # removefile(midfilename)

    # 写说明书附图
    def instrupicture(self, doc):
        self.docxinitial(doc, '说明书附图')
        # 只有lastflag为1的时候能够创建说明书附图
        if self.lastflag == 1:
            writetxts = []
            lastcon = self.lastcon
            # 根据各种格式的分号对正文进行切割
            cutcon = re.split(':|;|：|；', lastcon)
            # 查找切割后的文本中包含模块的文本
            for con in cutcon:
                txts = re.findall(r"(.*?)模块[，|,]", con)
                if len(txts) > 0:
                    writetxts.append(txts)
            for txt in writetxts:
                txt[0] = txt[0] + '模块'
            # 创建索引列表作为写文本的顺序
            ids2 = ['0', '0']
            for i in range(len(writetxts)):
                ids2.append(str(i + 1))
            WP2 = WritePicture(self.title + 'model', writetxts, ids2, canvasy='1440px')
            try:
                png2path, midfilename = WP2.SquareTreeWrite('center', 0, 500, -300, 550, 600)
            except:
                print('没有权利要求无法生成图片')
                return
            # 插入图片并居中
            doc.add_picture(png2path)
            last_paragraph = doc.paragraphs[-1]
            last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            # 加入下标图1
            para = doc.add_paragraph()
            para.add_run('                                      图2').bold = True

            self.setsectionformat(doc)
            # removefile(midfilename)


# Docx文档书写类
class SaveDocxDemo(object):
    def __init__(self, tits, cons, username='nouser', title='报告'):
        self.tits = tits
        self.cons = cons
        self.username = str(username)
        self.title = title

    # 创建可导入草稿文件
    def get_caninput_docx(self, ids, inventframe, values, errors, marks, annotates, examples, oar, oaRa):
        """
        :param ids: id列表
        :param inventframe: 框架
        :param values: 评价列表
        :param errors: 错误列表
        :param marks: 分数列表
        :param annotates: 批注列表
        :param examples: 例子列表
        :param oar: 审核认定授权概率
        :param oaRa: 审核总体评价
        :return: thisdraftpath: 文件路径
                 file_name: 文件名称
        """
        # 1、查看有没有该用户的可导入草稿文件夹
        user_file_path = os.path.join(BASE_DIR, 'media/caninputdraft/', self.username)
        if not os.path.exists(user_file_path):
            os.mkdir(user_file_path)
        # 2、查看有没有demo文件，没有则在caninputdratf里面创建一个demo.docx
        demo_path = os.path.join(BASE_DIR, user_file_path, 'demo.docx')
        if not os.path.exists(demo_path):
            document = Document()
            # document.add_paragraph(' ')# 如果再报错试试先写入内容
            document.save(demo_path)
        # 3、打开demo文件开始写入用户草稿内容
        doc = Document(demo_path)
        # 4、写入框架、审核认定授权率、审核总体评价编码内容
        para = doc.add_paragraph('***kj' + inventframe + '|||')
        para.add_run('***oar' + oar + '|||')
        para.add_run('***oaRa' + oaRa + '|||')
        # 5、循环写入id、标题、正文、评价、批注、分数、错误、例子的编码内容
        idslength = len(ids)
        if idslength > 0:
            for i in range(len(ids)):
                para.add_run('***id' + ids[i] + '|||')
                para.add_run('***tit' + self.tits[i] + '|||')
                para.add_run('***con' + self.cons[i] + '|||')
                para.add_run('***val' + values[i] + '|||')
                para.add_run('***ann' + annotates[i] + '|||')
                para.add_run('***mar' + marks[i] + '|||')
                para.add_run('***err' + '&'.join(errors[i]) + '|||')
                para.add_run('***exa' + examples[i] + '|||')
        # 6、获取年月日的时间戳，用作文件不重复名称设置
        thisday = datetime.now().strftime('%Y%m%d')
        # 7、组合文件存储的上级路径
        save_path = user_file_path + '/' + str(thisday)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        # 8、拼接文件的名字，格式为标题+年月日小时分钟秒时间戳+.docx
        thistime = datetime.now().strftime('%Y%m%d%H%M%S%f')
        thisdraftpath = save_path + '/' + self.title + thistime + '.docx'
        # 9、获取文件名
        file_name = thisdraftpath.split('/')[-1]
        # 10、保存文件
        doc.save(thisdraftpath)
        return thisdraftpath, file_name

    # 创建五书文件
    def getfivebook(self, ids, examples, uid, ifPicture):
        """
        :param ids: id列表
        :param examples: 例子列表
        :param uid: 专利id
        :param ifPicture: 是否生成图片标志
        :return: zippath: 五书路径
                 file_name: 文件名称
        """
        # 1、查看有没有该用户的五书存放文件夹，没有则创建
        user_file_path = os.path.join(BASE_DIR, 'media/userdraft/', self.username)
        if not os.path.exists(user_file_path):
            os.mkdir(user_file_path)
        # 2、查看有没有demo文件，没有则在userdraft里面创建一个demo.docx
        demo_path = os.path.join(BASE_DIR, user_file_path, 'demo.docx')
        if not os.path.exists(demo_path):
            document = Document()
            # document.add_paragraph(' ')# 如果再报错试试先写入内容
            document.save(demo_path)
        # 3、打开demo文件作为五书的五个docx文档的基础空白文档
        doc1 = Document(demo_path)
        # 4、创建五书类
        # 五书各文件的标题，['10001权利要求书', '10002说明书', '10003说明书附图', '10004说明书摘要', '10005摘要附图']
        FB = FiveBook(ids, self.tits[2:], self.cons[2:], self.title, self.username)
        # 5、将文件存储在对应用户文件夹下，按日期存储，文件命名也用时间戳来区分
        thistime = datetime.now().strftime('%Y%m%d%H%M%S%f')
        save_path = user_file_path + '/' + str(thistime)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        # 6、写权利要求书docx
        FB.claims(doc1, uid)
        claimspath = save_path + '/10001权利要求书.docx'
        doc1.save(claimspath)
        # 7、写说明书docx
        doc2 = Document(demo_path)
        jishu = self.cons[0]
        youyi = self.cons[1]
        FB.instruction(doc2, jishu, youyi, examples, uid)
        instructionpath = save_path + '/10002说明书.docx'
        doc2.save(instructionpath)
        # 8、写说明书附图docx
        doc3 = Document(demo_path)
        if ifPicture == "true":
            FB.abspicture(doc3)
            FB.instrupicture(doc3)
        abspicturepath = save_path + '/10003说明书附图.docx'
        doc3.save(abspicturepath)
        # 9、写说明书摘要docx
        doc4 = Document(demo_path)
        FB.instructionabs(doc4)
        instructionabspath = save_path + '/10004说明书摘要.docx'
        doc4.save(instructionabspath)
        # 10、写摘要附图docx
        doc5 = Document(demo_path)
        if ifPicture == "true":
            FB.abspicture(doc5)
        instrupicturepath = save_path + '/10005摘要附图.docx'
        doc5.save(instrupicturepath)
        # 11、将包含五书的五个文档的文件夹进行打包
        import zipfile
        file_name = self.title + str(thistime) + '.zip'
        zippath = user_file_path + '/' + file_name
        z = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
        startdir = save_path
        for dirpath, dirnames, filenames in os.walk(startdir):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                z.write(filepath, arcname=filename)
        z.close()
        return zippath, file_name

    # 创建价值评估报告文件
    def getpricecalcul(self, statistics, total, effectcount, allcount, totalwords, jsyymsg):
        """
        :param statistics: 每一段的分析结果
        :param total: 总分
        :param effectcount: 有效段落数
        :param allcount: 总段落数
        :param totalwords: 总字数
        :param jsyymsg: 背景和有益分析结果
        :return: thisdraftpath: 文件路径
                 file_name: 文件名
                 total: 总分
        """
        # 1、查看有没有价值评估报告的文件夹，没有则创建
        price_file_path = os.path.join(BASE_DIR, 'media/price/', self.username)
        if not os.path.exists(price_file_path):
            os.mkdir(price_file_path)
        # 2、查看有没有demo文件，没有则在price里面创建一个demo.docx
        demo_path = os.path.join(BASE_DIR, price_file_path, 'demo.docx')
        if not os.path.exists(demo_path):
            document = Document()
            # document.add_paragraph(' ')# 如果再报错试试先写入内容
            document.save(demo_path)
        # 3、打开demo文件开始写入价值评估内容
        # 设置基本格式
        doc = Document(demo_path)
        doc.styles["Normal"].font.name = u'宋体'
        doc.styles["Normal"].font.size = Pt(12)
        doc.styles["Normal"]._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
        # 写标题
        ti = doc.add_paragraph()
        ti.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        ti1 = ti.add_run(self.title + '-审核结果')
        ti1.font.size = Pt(16)  # 添加页面内容
        ti1.bold = True
        # 写价值评估结果，放在文档前面
        para = doc.add_paragraph()
        para.add_run('\n总字数:' + str(totalwords) + '个').bold = True
        para.add_run('\n总共段落个数:' + str(allcount) + '个').bold = True
        para.add_run('\n满足要求字数的段落个数:' + str(effectcount) + '个').bold = True
        pr1 = para.add_run('\n综合价值度得分:' + str(total) + '分' + '\n')
        pr1.font.size = Pt(16)
        pr1.bold = True
        # 写技术背景和有益效果的分析结果，要注意有的专利没有背景和有益
        # 没有背景和有益的设置字数为0
        if len(self.cons) > 1:
            jslen = len(self.cons[0])
            yylen = len(self.cons[1])
        else:
            jslen, yylen = 0, 0
        para.add_run('细节如下：\n').bold = True
        para.add_run('技术背景:\n')
        para.add_run('字数:' + str(jslen) + '\n').bold = True
        para = doc.add_paragraph()
        para.add_run('有益效果:')
        para.add_run('字数:' + str(yylen) + '\n').bold = True
        para = doc.add_paragraph()
        para.add_run(jsyymsg + '').bold = True
        para = doc.add_paragraph()
        # 写每一个步骤的标题、字数、审核结果、得分
        for res in statistics:
            para.add_run(res['title'])
            # 敏感词文本判断，若敏感词个数大于0，分析结果不合格且进行想应文本说明
            words = res['riskwork']
            if len(words) > 0:
                thisprice = str(res['price'])
                thisresult = '不合格'
                para.add_run(
                    res['number'] + '，审核结果:' + thisresult + '，得分:' + str(thisprice) + '分' + '\n').bold = True
                words = '，'.join(words).lstrip('，')
                para = doc.add_paragraph()
                para.add_run('权利要求书部分出现违规字词：' + words + '、')
            else:
                para.add_run(
                    res['number'] + '，审核结果:' + res['result'] + '，得分:' + str(res['price']) + '分' + '\n').bold = True
            # 每一段与已写专利的相似度比较结果
            ifsim = res.get('similar')
            if ifsim:
                for sim in res['similar']:
                    for k, v in sim.items():
                        para.add_run('相似专利标题:{}，相似段落id:{}\n'.format(k, '，'.join(v)))
            # 每一段与全库专利的比较结果
            ifred = res.get('color')
            if ifred == 'red':
                run = para.add_run("相似度比较有问题,相似度为{}".format(res.get('esScore')))
                run.font.color.rgb = RGBColor(255, 0, 0)
            # 书写每一段的分析文本结果
            writejson = res['writejson']
            for json in writejson:
                para.add_run('该段落进行创造性分析的结果为：、\n').bold = True
                para.add_run('源段落：').bold = True
                para.add_run(json['value'] + '/\n')
                para.add_run('结论：').bold = True
                try:
                    int(json['rejectpatentnumber'][:4])
                    run = para.add_run('授权概率低。' + '、\n')
                    run.font.color.rgb = RGBColor(255, 0, 0)
                    run.bold = True
                except:
                    run = para.add_run(json['rejectpatentnumber'] + '、\n')
                    run.font.color.rgb = RGBColor(255, 0, 0)
                    run.bold = True
                if len(json['rejectpatentname']) > 0:
                    para.add_run('对比段落：')
                    para.add_run(json['rejectpatentnumber'] + json['rejectpatentname'] + '、\n')
                    para.add_run(json['rejectsection'] + '、\n')
            para.add_run('\n')

        # 保存价值评估报告文件
        thisday = datetime.now().strftime('%Y%m%d')
        save_path = price_file_path + '/' + str(thisday)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        thistime = datetime.now().strftime('%Y%m%d%H%M%S%f')
        # 报告文件名要加上审核-
        thisdraftpath = save_path + '/' + '审核-' + self.title + '-' + thistime + '.docx'
        file_name = thisdraftpath.split('/')[-1]
        doc.save(thisdraftpath)
        return thisdraftpath, file_name, total
`ˋ`
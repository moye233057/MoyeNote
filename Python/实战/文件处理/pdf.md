# 一、pdf转成一张张图片
python 3.6
pip install pdf2image
# 安装PyMuPDF必须指定版本，否则会报错
pip install PyMuPDF==1.18.0

`ˋ`
import sys, fitz
import os
import datetime


def pyMuPDF_fitz(pdfPath, imagePath):
    """
    pdfPath: 一份pdf文件的路径
    imagePath: 存放生成图片的文件夹路径，例如./image\2022年中国视频云服务行业研究报告，会以2022年中国视频云服务行业研究报告作为图片文件夹的名称
    """

    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.writePNG(imagePath + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


if __name__ == "__main__":
    pdfPath = './pdf/2020社交零售白皮书-腾讯+BCG-2020.1-63页.pdf'
    imagePath = './image'
    pyMuPDF_fitz(pdfPath, imagePath)
`ˋ`


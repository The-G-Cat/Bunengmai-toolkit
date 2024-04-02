

# -*- coding: utf-8 -*-
"""
1、安装库
    pip install pymupdf
    pip install pillow
2、修改main方法参数
3、运行
"""
import os
import sys
import fitz
from PIL import Image
 
 
def pdf_to_images(pdf_path, img_path):
    #  打开PDF文件，生成一个对象
    doc = fitz.open(pdf_path)
    print(doc.page_count)
    for pg in range(doc.page_count):
        page = doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        try:
            os.mkdir(img_path)
        except FileExistsError:
            pass
        pm.save(f'{img_path}/%s.png' % pg)
 
 
def join(png1, png2, size):
    img1, img2 = Image.open(png1), Image.open(png2)
    size1, size2 = img1.size, img2.size  # 获取两张图片的大小
    joint = Image.new('RGB', (size1[0], size1[1] + size2[1] - size))
    # 新建一张新的图片
    # 因为拼接的图片的宽都是一样，所以宽为固定值
    # 高为两张图片的高相加再减去需要缩进的部分
    loc1, loc2 = (0, 0), (0, size1[1] - size)
    # 两张图片的位置
    # a-------------
    # |            |
    # |            |
    # |            |
    # |            |
    # |            |
    # b------------|
    # |            |
    # |            |
    # |            |
    # |            |
    # |------------|
 
    # 位置都是以该图片的左上角的坐标决定
    # 第一张图片的左上角为a点，a的坐标为(0,0)
    # 第二张图片的左上角为b点，a的横坐标为0，纵坐标为第一张图片的纵坐标减去第二张图片上移的size: (0, size[1]-size)
 
    joint.paste(img2, loc2)
    joint.paste(img1, loc1)
    # 因为需要让第一张图片放置在图层的最上面,所以让第一张图片最后最后附着上图片上
    joint.save(result)
 
 
def start(items, size, first_path=None):
    # 当first为None时,默认将第一张图片设置为图片列表的第一张图片,第二张图片设置为图片列表的第二张
    # 当这两张图片合成后，将图片列表的已经合成的图片元素移除
    # 然后将合成的图片设置为第一张图片,将剩余的没有合成的图片列表继续操作
    # 当first_path不为None,将第一张图片设置为first_path，第二张图片设置为传进来的列表的第一个元素
    # 合成之后，将刚刚使用的列表的元素删除
    # 最后递归函数，知道列表为空
    try:
        if not first_path:
            path1, path2 = items[0], items[1]
            join(path1, path2, size)
            items.remove(path1)
            items.remove(path2)
            return start(items, size, first_path=result)
        else:
            path2 = items[0]
            join(first_path, path2, size)
            items.remove(path2)
            return start(items, size, first_path=result)
    except:
        pass
 
 
def getAllImg(path):
    result = []
    filelist = os.listdir(path)
    i = 0
    for file in filelist:
        if str(file).split(".")[0].isdigit():
            result.append(os.path.join(path, f"{str(i)}.png"))
        i += 1
    return result
 
 
if __name__ == '__main__':
    # 图片保存路径：
    if not os.path.exists('./png'):
        os.makedirs('./png')
    path = './png'
    pdf_to_images('./XXX.pdf', path)
    result = f"{path}/XXX.png"
    s = getAllImg(path)
    start(s, 100)
    print('最后图片尺寸--->', Image.open(result).size)
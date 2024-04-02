import os
from PIL import Image
from PIL import ImageFile
 
 
# 压缩图片文件
def compress_image(outfile, kb=2048, quality=100, k=0.9):  # 通常你只需要修改kb大小
    """不改变图片尺寸压缩到指定大小
    :param outfile: 压缩文件保存地址
    :param kb: 压缩目标，KB
    :param k: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
 
    o_size = os.path.getsize(outfile) // 1024  # 函数返回为字节，除1024转为kb（1kb = 1024 bit）
    print('before_size:{} after_size:{}'.format(o_size, kb))
    if o_size <= kb:
        return outfile
 
    ImageFile.LOAD_TRUNCATED_IMAGES = True  # 防止图像被截断而报错
 
    while o_size > kb:
        im = Image.open(outfile)
        x, y = im.size
        out = im.resize((int(x * k), int(y * k)), Image.LANCZOS)  # 最后一个参数设置可以提高图片转换后的质量
        try:
            out.save(outfile, quality=quality)  # quality为保存的质量，从1（最差）到95（最好），此时为85
        except Exception as e:
            print(e)
            break
        o_size = os.path.getsize(outfile) // 1024
    return outfile
 
# 压缩单张图片(注意不会保存源文件)
outfile = "./XXX.png" # 单张图片地址
compress_image(outfile,kb=2048)
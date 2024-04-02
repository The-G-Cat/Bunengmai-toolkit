from PIL import Image

img = Image.open("C:/Users/谷冬宇/Desktop/QQ图片20240212180758.jpg")
# 此时返回一个新的image对象，转换图片模式
image = img.convert('RGB')
# 调用save()保存
image.save('E:/Python脚本/编译使用/图标.ico')
import img2pdf
import os,re
img_path = "./"
imgs = []
for f in os.listdir(img_path):
	if not f.endswith((".jpg",".png")): #检测文件类型，否则跳过
		continue
	path = os.path.join(img_path, f) #完整文件路径
	if os.path.isdir(path): ##检测是否为文件，否则跳过
		continue;
	 #将文件完整路径添加到列表存储
	imgs.insert((int(re.search(r'\d+',path).group())-1),path)
with open("./PHOTO.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))
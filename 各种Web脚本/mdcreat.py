'''Python Markdown操作模块

@author:什么都不能卖
@version：1.0.0
'''

class md():
	def __init__(self):
		self.md=[]
		self.re=""
		self.commands={
		"None":"",
		"line":"\n",
		"t1":r"# 文本",
		"t2":r"## 文本",
		"t3":r"### 文本",
		"t4":r"#### 文本",
		"t5":r"##### 文本",
		"rw":r'<font color="E62817">文本</font>',
		"bw":r'<font color="1B9AEE">文本</font>',
		"gw":r'<font color="2FBDB3">文本</font>',
		"url":r"[文本](文本)",
		"img":r"![Alt|文本x文本](文本)",
		"quote":r"> 文本"
		}

	def add(self,Type="None",*text):#加内容
		if Type in self.commands:
			temp=self.commands[Type]
			temp2=0
			while temp.find("文本")!= -1:
				idx=temp.find("文本")
				temp=temp[:idx]+text[temp2]+temp[idx+2:]
				temp2+=1
			self.md.append(temp)
		else:
			self.md.append(Type)
	
	def new(self):
		self.md=[]

	def delete(self,*num):
		y=0
		for x in num:
			del self.md[x-y]
			y+=1

	def edit(self,*pair):
		for x in pair:
			self.md[x[0]]=x[1]

	def listout(self):
		y=0
		for x in self.md:
			print("["+str(y)+r"]:   "+x)
			y+=1
		return self.re

	def check(self,*num):
		for x in num:
			print("["+str(x)+r"]:   "+self.md[x])

	def out(self):
		self.re=""
		for x in self.md:
			self.re+=x
		return self.re


		
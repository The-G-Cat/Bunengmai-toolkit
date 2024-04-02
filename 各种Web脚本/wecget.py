'''WeChat公众号文章获取模块

@author:什么都不能卖
@version:v1.1.5
'''


import requests
import time,json,ssl

def take(word="Check!!!!",ifpausee=False,**kwargs):
	#啊没错，这玩意是个查错用的小工具
	if not kwargs:
		print(word)
	else:
		for key, value in kwargs.items(): 
			print ("%s = %s" %(key, value)) 
	if ifpause:
		input()


class wechat():
	"""公众号爬取函数类"""
	def __init__(self,much,token,cookie):
		requests.packages.urllib3.disable_warnings()#关掉该死的warning，吵死
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
			'Cookie': cookie
		}#头！
		self.ids={
            "MzA3NTE5MzQzMA%3D%3D": "共青团中央"#这是个例子
		}#ID表
		self.much=much
		self.fdata={}#一级结构
		self.timestamp=self.gettime()#昨天零点时间戳
		self.temp2 = []#用于每个来源文章在不同循环间的信息共通
		self.begin = 0#用于每个来源文章在不同循环间文章获取开始位的共通
		self.token = str(token)

	def gettime(self):
		#获取某天时间戳
		current_timestamp = int(time.time())

		current_time = time.localtime(current_timestamp)

		year = current_time.tm_year
		mon = current_time.tm_mon
		day = current_time.tm_mday
		hour = current_time.tm_hour
		minute = current_time.tm_min
		second = current_time.tm_sec

		current_time = (year, mon, day+self.much, 0, 0, 0, 0, 0, 0)

		timestamp = int(time.mktime(current_time))
		return timestamp#获得某天零点时间戳

	def checktime(self,timestamp):
		#确认一下文章发表时间是不是在某天之前
		return (timestamp<=self.timestamp)

	def dealdata(self,temp1):
		#数据录入和处理
		for x in range(len(temp1)):
			if self.checktime(temp1[x]["update_time"]):
				self.begin = 0
				return False

			y=x+self.begin
			a=[]
			self.temp2.append(a)
			self.temp2[y].append(temp1[x]["title"])
			self.temp2[y].append(time.strftime("%Y-%m-%d",time.gmtime(temp1[x]["create_time"])))
			self.temp2[y].append(time.strftime("%Y-%m-%d",time.gmtime(temp1[x]["update_time"])))
			self.temp2[y].append(temp1[x]["link"])
			self.temp2[y].append(temp1[x]["digest"])
			self.temp2[y].append(temp1[x]["author_name"])
			self.temp2[y].append(temp1[x]["cover"])

			if (self.checktime(temp1[x]["update_time"])==False and x == (len(temp1)-1)):
				self.begin+=len(temp1)
				break
		return True

	def getdata(self):
		#主函数，获得各来源文章列表及相应信息
		for fakeid in self.ids.keys():#遍历各来源
			self.temp2 = []#初始化
			temp1=""
			while self.dealdata(temp1)==True:
				time.sleep(10)
				begin=str(self.begin)
				url = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&fakeid="+fakeid+"&query=&begin="+begin+"&count=10&type=9&need_author_name=1&token="+self.token+"&lang=zh_CN&f=json&ajax=1%20HTTP/1.1"
				response = requests.get(url,headers = self.headers,verify=False) #发送网络请求
				response = response.content.decode('utf-8')
				response = json.loads(response)
				temp1 = response["app_msg_list"]
			self.fdata[self.ids[fakeid]]=self.temp2
		pass

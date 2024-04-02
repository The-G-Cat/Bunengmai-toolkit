from seleniumwire import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class debug(object):

	def __init__(self,URL,MODE="headless"):
		#各种各样的反检测设置

		options = Options()
		#无头
		options.add_argument(MODE)
		#设置默认编码为utf-8，也就是中文
		options.add_argument('lang=zh_CN.UTF-8')

		
		#模拟浏览器
		options.add_argument(
		'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"')

		

		#禁止硬件gpu加速，谷歌文档提到需要加上这个属性来规避bug
		options.add_argument('--disable-gpu')

		#取消沙盒模式,        # “–no-sandbox”参数是让Chrome在root权限下跑
		options.add_argument('--no-sandbox')

		#禁止弹窗广告
		options.add_argument('--disable-popup-blocking')

		#不加载图片, 提升速度
		options.add_argument('blink-settings=imagesEnabled=false') 

		#隐藏滚动条, 应对一些特殊页面
		options.add_argument('--hide-scrollbars') 

		#设置最大界面
		options.add_argument('--window-size=1920,1080')

		#去掉自动控制标志
		options.add_experimental_option('excludeSwitches',['enable-automation'])

		#此方法针对V78版本及以上有效，同时可以解决部分网站白屏的问题。
		options.add_experimental_option('useAutomationExtension',False)

		#忽略证书错误（实操后感觉没什么用）
		options.add_argument('--ignore-certificate-errors')


		#启动浏览器
		self.driver = webdriver.Edge(options=options,service=EdgeService(EdgeChromiumDriverManager().install()))

		#将window.navigator.webdriver属性变为undefined 防止检测
		self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
		  "source": """
		    Object.defineProperty(navigator, 'webdriver', {
		      get: () => undefined
		    })
		  """
		})		

		#访问链接
		self.driver.get(URL)



		self.url = []
		self.res = []
		self.req = []

		self.re=""

	def get_cookie(self):
		#获取cookie
		cookies = self.driver.get_cookies()
		cookie = [item["name"] + "=" + item["value"] for item in cookies]
		cookiestr = ';'.join(item for item in cookie)
		self.cookie = cookiestr
		return self.cookie

	def get_headers(self,Type=""):
		#获取headers及不同部分
		if not Type:
			return self.driver.requests
		elif Type == "url":
			self.url = []
			for request in self.driver.requests:
				self.url.append(request.url)
			return self.url
		elif Type == "req":
			self.req=[]
			for request in self.driver.requests:
				self.req.append(request.headers)
			return self.req
		elif Type == "res":
			self.res=[]
			for request in self.driver.requests:
				self.res.append(request.response.headers)
			return self.res

	def get_all(self):
		return self.driver.page_source

	def Xpath(self,Xpath='/http'):
		#Xpath元素检索
		self.re=self.driver.find_element(by = By.XPATH, value = Xpath)
		return self.re

	def clsname(self,classname=""):
		#classname 元素检索
		self.re=self.driver.find_element(By.CLASS_NAME, classname)
		return self.re
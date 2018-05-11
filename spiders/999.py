# !/usr/bin/env/python
# _*_coding:utf-8_*_


import requests
from lxml import etree
import os
import gevent
from gevent import monkey
import threading

monkey.patch_all()

road = "/home/python/Desktop/ligang/"

DIR_LAND = road

class QianBaiLu:

	def __init__(self):
		self.start_url = "https://www.999av.vip/html/tupian/toupai/index.html"
		self.headers = {"User-Agent": "MMozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

	def parse_url(self,url):
		print(url)
		try:
			response = requests.get(url,headers=self.headers)
		except Exception as e:
			print(e)
			response = None
			return
		return response.content.decode()

	def get_content_list(self,html_str):# 3. 提取数据
		html = etree.HTML(html_str)
		li_list = html.xpath("//div[@class='art']/ul/li") #返回li的列表
		print(li_list)
		content_list = []
		for li in li_list:
			item = {}
			item["href"] = "https://www.999av.vip"+li.xpath("./a/@href")[0]
			item["title"] = li.xpath("./a/text()")[0]
			item["img_list"] = self.get_img_list(item["href"])
			content_list.append(item)
		return content_list


	def get_img_list(self,detail_url):
		# 获取详情页的图片地址
		#1.发送请求
		detail_html_str = self.parse_url(detail_url)
		#2. 提取数据
		html = etree.HTML(detail_html_str)
		img_list = []
		img_temp_url_list = html.xpath("//p/img/@src")[1:]
		for img_temp_url in img_temp_url_list:
			img_url = "https:" + img_temp_url
			img_list.append(img_url)
		# print(img_list)
		return img_list

	def save_content_list(self,content_lsit):#保存数据
		for content in content_lsit:
			filename = content["title"]
			for img_url in content["img_list"]:
				name = img_url.split("/")[-1]
				self.dowload_img(img_url,filename,name)

	def dowload_img(self,url,filename,name):
		data = requests.get(url)
		try:
			file = open(DIR_LAND + filename + "/" + name, 'wb')
			file.write(data.content)
			file.close()
		except Exception as e:
			print(e, data.status_code)

	def run(self): #实现主要逻辑
		url = self.start_url
		num = 1
		while True:
			# 1. 准备url，start_url
			#2. 发送请求，获取响应
			html_str = self.parse_url(url)
			# 3. 提取数据
			content_list = self.get_content_list(html_str)
			#4. 保存
			self.save_content_list(content_list)
			num +=1
			url = "https://www.999av.vip/html/tupian/toupai/index_" + str(num) +".html"
			if num > 362:
				break


if __name__ == '__main__':
	spider = QianBaiLu()
	spider.run()

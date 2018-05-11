# -*- coding: utf-8 -*-
import scrapy


class ItSpider(scrapy.Spider):
    name = 'it'  #爬虫名
    allowed_domains = ['itcast.cn']  #允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  #start_url 最开始爬虫会抓取的地址

    def parse(self, response):  #parse函数处理startur对饮的响应
        # ret = response.xpath("//div[@class='tea_con']/div/ul/li//h3/text()").extract()
        # print(ret)
        li_list = response.xpath("//div[@class='tea_con']/div/ul/li")
        for li in li_list:
            item = {}
            item["name"]=li.xpath(".//h3/text()").extract_first()
            item["title"]=li.xpath(".//h4/text()").extract_first()
            item["desc"]=li.xpath(".//p/text()").extract_first()
            # item_list.append(item)
            # print(item)
            yield item  # Request, BaseItem, dict or None

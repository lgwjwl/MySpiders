# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from pymongo import
import json
from pymongo import MongoClient

client = MongoClient(host='127.0.0.1',port=27017)
collection = client['load']['zhaopin']

class TencentZhaopinPipeline(object):
    def process_item(self, item, spider):
        with open('temp.txt','a') as f:
            json.dump(item,f,ensure_ascii=False,indent=2)

        return item


class TencentZhaopinPipeline2(object):
    def process_item(self, item, spider):
        collection.insert(item)

        return item

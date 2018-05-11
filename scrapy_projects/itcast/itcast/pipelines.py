# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItcastPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "it":
            item["come_from"]="itcast"
            print(item)

        return item


class ItcastPipeline1(object):
    def process_item(self, item, spider):
        if spider.name == "it1":
            print(item)
        return item


# coding:utf-8
import json
import requests


class Douban_Spider(object):
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start=54&count=18&loc_id=108288"
        self.headers = {
            "Referer": "https: // m.douban.com / tv / american",
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"
        }

    def parse_url(self):
        resp_json = requests.get(self.temp_url,headers = self.headers)
        print(resp_json)
        print(resp_json.content.decode())
        return resp_json.content.decode()

    def get_data(self,data_json):
        data_dict = json.loads(data_json)
        content_list = data_dict["subject_collection_items"]
        return content_list

    def save_content(self,data_list):
        with open("douban_my.txt","a",encoding="utf-8") as f:
            for data in data_list:
                f.write(json.dumps(data,ensure_ascii=False))
                f.write("\n")

    def run(self):
        # 准备url地址
        # 解析url，获取响应
        resp = self.parse_url()
        # 提取数据
        data_list = self.get_data(resp)
        # 保存数据
        self.save_content(data_list)

if __name__ == '__main__':
    spider = Douban_Spider()
    spider.run()

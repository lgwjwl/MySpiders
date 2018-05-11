# coding=utf-8
import requests
import json

class Douban:

    def __init__(self):
        # https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?start=0&count=18&loc_id=108288
        # self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start={}&count=18&loc_id=108288"

        self.temp_url_list = [
            {
                "temp_url":"https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start={}&count=18&loc_id=108288",
                "referer": "https://m.douban.com/tv/american"
            },
            {
                "temp_url":"https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?start={}&count=18&loc_id=108288",
                "referer": "https://m.douban.com/tv/chinese"
            }
        ]

        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}

    def parse_url(self,url,referer):
        self.headers.update({"Referer":referer})
        print(url)
        resposne = requests.get(url,headers=self.headers)
        return resposne.content.decode()

    def get_content_list(self,json_str):
        temp_dict = json.loads(json_str)
        content_list = temp_dict["subject_collection_items"]
        return content_list

    def save_content_list(self,content_lsit):#保存
        with open("douban.txt","a",encoding="utf-8") as f:
            for content in content_lsit:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self): #实现主要逻辑
        for temp_url in self.temp_url_list:
            #1. start_url
            num = 0
            while True:
                next_url =temp_url["temp_url"].format(num)
                # 2. 发送请求，获取响应
                json_str = self.parse_url(next_url,temp_url["referer"])
                # 3. 提取数据
                content_lsit = self.get_content_list(json_str)
                # 4. 保存
                self.save_content_list(content_lsit)
                # 5. 获取下一页的url地址，循环2-5步
                num+=18
                # 6. 程序终止的条件
                if len(content_lsit)<18:
                    break

if __name__ == '__main__':
    douban = Douban()
    douban.run()
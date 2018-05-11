#
import json,sys
import requests

class TranslateTool(object):
    """
    自动翻译
    """
    def __init__(self,query_string):
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        self.url = "http://fanyi.baidu.com/basetrans"
        self.query_string = query_string
        self.data = self.send_data()

    def send_data(self):
        data = {
            "query": self.query_string,
            "from": "zh",
            "to": "en"
        }
        return data

    def parse_url(self):
        resp = requests.post(self.url,headers = self.headers,data=self.data)
        return resp.content.decode('utf-8')

    def save_data(self,data_str):
        data_dict = json.loads(data_str)
        result = data_dict["trans"][0]["dst"]
        print("{}的翻译结果是:{}".format(self.query_string,result))

    def run(self):
        # 1. 准备url地址,准备请求体
        # 2. 发送请求，获取响应
        result_str = self.parse_url()
        # 3.提取数据
        self.save_data(result_str)


if __name__ == '__main__':
    query_str = sys.argv[1]
    # query_str = "好好学习，天天向上"
    print(query_str)
    translatetool = TranslateTool(query_str)
    translatetool.run()
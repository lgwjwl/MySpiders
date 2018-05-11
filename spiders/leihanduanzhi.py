# coding:utf-8
import re
import requests

Pattern = r'''    <div class="j-r-list-c-desc">
        <a href="/detail-\d*.html">(.*?)</a>
    </div>'''

class Leihanduanzhi_Speder(object):
    def __init__(self):
        self.url = "http://www.budejie.com/"
        self.headers = {
            "Referer":"http://www.budejie.com/text/2",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }

    def parse_url(self,url,header):
        resp = requests.get(url,headers = header)
        # print(resp.content.decode())
        return resp.content.decode()

    def get_data(self,html_str):
        p = re.compile(Pattern)
        data_list = p.findall(html_str)
        print(data_list)
        return data_list

    def save_data(self,data_list):
        with open("leihanduanzhi.txt","w",encoding="utf-8") as f:
            num = 1
            for data in data_list:
                f.write(str(num) + ".")
                f.write(data)
                f.write("\n")
                num += 1

    def run(self):
        resp = self.parse_url(self.url,self.headers)
        data_list = self.get_data(resp)
        self.save_data(data_list)

if __name__ == '__main__':
    spider = Leihanduanzhi_Speder()
    spider.run()
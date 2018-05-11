import time
from selenium import webdriver


class DouYu:
    def __init__(self):
        self.start_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
        contents_list = []
        for li in li_list:
            item = {}
            item['title'] = li.find_element_by_xpath('./a').get_attribute('title')
            item['anchor'] = li.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text
            item['watch_count'] = li.find_element_by_class_name('dy-num fr').text
            contents_list.append(item)
        next_url_list = self.driver.find_elements_by_class_name('dy-num fr')
        next_url = next_url_list[0] if len(next_url_list)>0 else None
        return contents_list,next_url

    def save_content(self,contents_list):
        with open('douyu.html','a',encoding='utf-8') as f:
            num = 1
            for item in contents_list:
                f.write(str(num) + '.')
                f.write(item['anchor'] + ':' +item['title'] +'-----' + item['watch_count'])
                f.write('\n')
                num += 1

    def run(self):
        self.driver.get(self.start_url)
        content_list ,next_url= self.get_content_list()
        self.save_content(content_list)
        while next_url is not None:
            next_url.click()
            time.sleep(5)
            content_list ,next_url = self.get_content_list()
            self.save_content(content_list)


if __name__ == '__main__':
    spider = DouYu()
    spider.run()




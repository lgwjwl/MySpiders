import time
from selenium import webdriver

url = 'https://www.douban.com/'

driver = webdriver.Chrome()
driver.get(url)

ret1 = driver.find_element_by_id("anony-nav")
print(ret1)

ret2 = driver.find_elements_by_id("anony-nav")
print(ret2)

ret3 = driver.find_elements_by_xpath("//*[@id='anony-nav']/h1/a")
print(len(ret3))

ret4 = driver.find_elements_by_tag_name("h1")
print(len(ret4))

ret5 = driver.find_element_by_link_text("下载豆瓣 App")
print(ret5.get_attribute('href'))

ret6 = driver.find_elements_by_partial_link_text("豆瓣")
print(len(ret6))

driver.quit()
from selenium import webdriver
import time

driver = webdriver.Chrome()
ret = driver.get('http://www.baidu.com')
print(ret)
time.sleep(1)

driver.save_screenshot('baidu.png')
driver.close()

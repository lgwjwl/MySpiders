# _*_coding:utf-8_*_
import selenium
import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected

User_Id = 'xxxx '
User_Password = 'jjjjjj'
url = "https://login.tmall.com/?"

driver = Chrome()
driver.get(url)
driver.switch_to.frame("J_loginIframe")
wait = WebDriverWait(driver, timeout=60)
wait.until(expected.visibility_of_element_located((By.ID, 'J_Quick2Static'))).click()
# driver.find_element_by_id('J_Quick2Static').click()
driver.find_element_by_id('TPL_username_1').send_keys(User_Id)

driver.find_element_by_id('TPL_password_1').send_keys(User_Password)
driver.find_element_by_id('J_SubmitStatic').click()
# 滑动滑条
time.sleep(2)
# try:
count = 0
sleep = 3
while count <= 5:

    btn = driver.find_element_by_id('nc_1_n1z')
    driver.find_element_by_id('J_SubmitStatic').click()

    driver.find_element_by_id('TPL_password_1').send_keys(User_Password)
    time.sleep(sleep)
    actions = ActionChains(driver)
    actions.click_and_hold(btn).perform()
    for x in [10,20,30,50,148]:
        actions.move_by_offset(x, 0).perform()
        actions.perform()
    actions.release()

    driver.find_element_by_id('J_SubmitStatic').click()
    count +=1
    sleep +=1

# except Exception as e:
#     print(e)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# driver.find_element(By.ID, 'kw').send_keys("水滴租房")
# driver.find_element(By.CLASS_NAME, 'bg s_btn').click()
time.sleep(5)
# driver.find_element(By.NAME,'?')
# driver.find_element(By.TAG_NAME,'a').click()
a = locate_with(By.ID, 'kw').above({By.ID: "kw"})
driver.find_element(By.XPATH, "")
print("1111111")
time.sleep(3)
driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.get("https://centre.creative-apartment.com.cn/")
driver.maximize_window()
# element = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/label/input[@id = 'username']")
# element = driver.find_element(By.XPATH, "//input[@class = 'xsd-input']")
element = driver.find_element(By.XPATH, "//input[@placeholder = '请输入手机号或者员工帐号']")
element.send_keys("15621113820")
driver.find_element(By.CSS_SELECTOR, "#psd").send_keys("666666")
driver.find_element(By.CSS_SELECTOR, ".xsd-btn").click()
time.sleep(14)
driver.quit()
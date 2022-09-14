from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://10.99.131.78/")

# action = ActionChains(driver)
driver.implicitly_wait(5)#隐式等待
WebDriverWait(driver, 5, 0.5).until(lambda x:x.find_element(By.CSS_SELECTOR, "#username")).send_keys("15621113820")
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys("15621113820")
driver.find_element(By.CSS_SELECTOR, "#psd").send_keys("123456")
print("11111")
driver.find_element(By.CSS_SELECTOR, ".xsd-btn").click()
print("2222")
time.sleep(7)
driver.find_element(By.LINK_TEXT, "知道了").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[href='/workbench/work-order']").click()#工单按钮
driver.find_element(By.LINK_TEXT, "新增工单").click()#新增工单按钮
time.sleep(2)
list_01 = driver.find_elements(By.CSS_SELECTOR, "[type = 'radio']"and"[name = 'ticket_source']")
print(list_01)
if list_01[0].is_selected() is True:#判断是不是首个按钮勾选，要是首个按钮勾选则点击第二个按钮：用来选择租客、内部
    list_01[1].click()
# list_02 = driver.find_elements(By.CSS_SELECTOR, "[type = 'radio']"and"[name = 'ticket_type']")
# print(list_02)
# if list_02[0].is_selected() is True:#判断是不是首个按钮勾选，要是首个按钮勾选则点击第二个按钮：用来选择维修、投诉
#     list_02[1].click()
# alert = driver.switch_to.alert#获取警告框
driver.find_element(By.CSS_SELECTOR, ".xsd-input" and "[placeholder='选择类型']").click()
time.sleep(2)
a = driver.find_elements(By.XPATH, "//div[@class='xsd-input-group']/ul[@class='display']/li")
print(a)
a[1].click()
time.sleep(2)
b = driver.find_element(By.XPATH, "//div[@class='dropdown-menu']/ul[@class='level2 ']/li").click()
print(b)
# b[0].click()
driver.find_element(By.CSS_SELECTOR, "[placeholder='请输入租客姓名']").send_keys("测试姓名")
driver.find_element(By.CSS_SELECTOR, "#order_customer_phone").send_keys("13222222272")
driver.find_element(By.CSS_SELECTOR, "#rental_room_id").click()

time.sleep(4)
driver.quit()
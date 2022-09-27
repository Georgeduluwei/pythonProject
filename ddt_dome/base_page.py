from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
     def open_browser(self):

         self.driver = webdriver.Chrome()

         global driver
         driver = self.driver
     def get(self,url):
         self.driver.get(url)

     def login(self):
         self.open_browser()
         self.get("https://centre.shuidiguanjia.com/")
         self.driver.find_element(By.ID, "username").send_keys("15621113820")
         self.driver.find_element(By.ID, "psd").send_keys("liuzhiwei123")
         self.driver.find_element(By.CLASS_NAME,"xsd-btn").click()

     def location_element(self,*args):
         return self.driver.find_element(*args)
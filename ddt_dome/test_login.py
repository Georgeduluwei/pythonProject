import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from ddt_dome.base_page import BasePage


class TsetLogin(unittest.TestCase):
    def test_01_login(self):
        bp = BasePage()
        bp.login()
        time.sleep(3)
        bp.location_element(By.XPATH,"/html/body/div[6]/div[3]/div[1]/ul/li[3]/a/span").click()

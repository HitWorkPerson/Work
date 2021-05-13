from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from io import BytesIO
from PIL import Image


class Selenium:

    def __init__(self):
        self.url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def start(self):
        # 打开网页
        self.driver.get(self.url)
        # 最大化
        self.driver.maximize_window()
        # 点击账户登录
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//li[@class="login-hd-account"]'))).click()
        # 获取第一个输入框，输入账户
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="J-userName"]'))).send_keys('1735429225@qq.com')
        # 获取第二个输入框，输入密码
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="J-password"]'))).send_keys(
            'qwer1234')



if __name__ == '__main__':
    s = Selenium()
    s.start()




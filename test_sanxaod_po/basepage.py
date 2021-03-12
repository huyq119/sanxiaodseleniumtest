import configparser
import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'isanxiaod.ini'))
        return config

    def __init__(self, _base_driver=None):
        _config = self.get_config()
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')
        _chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            _chrome_options.add_argument("--headless")
            _chrome_options.add_argument("--disable-extensions")
            _chrome_options.add_argument("--display-gpu")
            _chrome_options.add_argument("--no-sandbox")
        _base_driver: WebDriver
        if _base_driver is None:

            _chrome_options.add_experimental_option("w3c", False)
            self._driver = webdriver.Chrome(executable_path=_config.get('driver', 'chrome_driver'), options=_chrome_options)
            self._driver.maximize_window()
            self._driver.implicitly_wait(4)
            # self._get_cookies_sanxiaod()
            self._cookie_login()
        else:
            self._driver = _base_driver

    def _get_cookies_sanxiaod(self):

        self._driver.get("https://www.sanxiaod.com")
        self._driver.find_element(By.CSS_SELECTOR, ".header .w .r.hand").click()
        self._driver.find_element(By.CSS_SELECTOR, ".wx .iconweixin").click()
        sleep(8)
        _cookies = self._driver.get_cookies()
        with open("../test_sanxaod_po/cookies.json", "w") as f:
            json.dump(_cookies, f)

    def _cookie_login(self):
        self._driver.get("https://www.sanxiaod.com")
        self._driver.find_element(By.CSS_SELECTOR, ".header .w .r.hand").click()
        self._driver.find_element(By.CSS_SELECTOR, ".wx .iconweixin").click()
        with open(f"../test_sanxaod_po/cookies.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get("https://www.sanxiaod.com/")
        sleep(3)

    def find(self, by, value):
        return self._driver.find_element(by=by, value=value)

    def quit_page(self):
        self._driver.quit()

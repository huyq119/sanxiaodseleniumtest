from time import sleep

from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

from test_sanxaod_po.basepage import BasePage


class PrintListAva(BasePage):

    def page_scroll(self):
        _element = self.find(By.CSS_SELECTOR, ".container .type7")
        _actions = TouchActions(self._driver)
        _actions.scroll_from_element(_element, 0, 3000).scroll(0,-3000).perform()
        _text = self.find(By.CSS_SELECTOR, ".l .on").text
        return _text




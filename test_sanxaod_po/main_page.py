from selenium.webdriver.common.by import By

from test_sanxaod_po.basepage import BasePage
from test_sanxaod_po.print_list_ava import PrintListAva


class MainPage(BasePage):

    def goto_print_list_ava(self):
        self.find(By.CSS_SELECTOR, ".l a[href='/3_album?type=7']").click()
        return PrintListAva(self._driver)



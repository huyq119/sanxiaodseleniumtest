import allure
from test_sanxaod_po.main_page import MainPage


@allure.feature('测试三小D登录浏览可打印模型列表')
class TestSignIn():

    def setup(self):
        self.main = MainPage()

    @allure.story('Test key word 登录查看')
    def test_login(self):
        result = self.main.goto_print_list_ava().page_scroll()

        assert result == "3D打印"

    def teardown(self):
        self.main.quit_page()

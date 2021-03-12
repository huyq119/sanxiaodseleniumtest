from test_sanxaod_po.main_page import MainPage


class TestSignIn():

    def setup(self):
        self.main = MainPage()

    def test_login(self):
        result = self.main.goto_print_list_ava().page_scroll()

        assert result == "3D打印"

    def teardown(self):
        self.main.quit_page()

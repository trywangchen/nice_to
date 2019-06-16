import time
import pytest
from base.base_analyze import analyze_file

from base.base_driver import init_driver
from page.page import Page

class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(6)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self,args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        self.page.home_page.click_me_button()
        self.page.register_page.click_login()
        self.page.login_page.login_input_name(username)
        self.page.login_page.login_input_password(password)
        self.page.login_page.login_me_button()

        if toast is None:
            assert self.page.me_page.get_nick_text() == username
        else:
            assert self.page.login_page.is_toast_exist(toast)# 部分内容断言
            assert self.page.login_page.get_toast(toast) # 获取全部文本断言



import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(6)
        self.driver.quit()
    def test_login(self):
        self.page.home_page.click_me_button()
        self.page.register_page.click_login()
        self.page.login_page.login_input_name("13136137289")
        self.page.login_page.login_input_password("wangchen361")
        self.page.login_page.login_me_button()
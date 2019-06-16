from page.home_page import HomePage
from page.login_page import Login
from page.me_page import MePage
from page.register_page import Register


class Page:
    def __init__(self,driver):
        self.driver = driver
    @property
    def home_page(self):
        return HomePage(self.driver)
    @property
    def register_page(self):
        return Register(self.driver)
    @property
    def login_page(self):
        return Login(self.driver)
    @property
    def me_page(self):
        return MePage(self.driver)

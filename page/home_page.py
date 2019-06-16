from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class HomePage(BaseAction):
    me_button = By.ID,"com.yunmall.lc:id/tab_me"

    def click_me_button(self):
       self.click(self.me_button)


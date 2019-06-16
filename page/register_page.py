from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class Register(BaseAction):
    register_button = By.ID,"com.yunmall.lc:id/textView1"

    def click_login(self):
        self.click(self.register_button)
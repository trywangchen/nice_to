from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class MePage(BaseAction):
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    def get_nick_text(self):
        return self.find_element(self.nick_name_text_view).text
from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class Login(BaseAction):
   login_name =  By.CLASS_NAME,"android.widget.EditText"
   login_password = By.ID,"com.yunmall.lc:id/logon_password_textview"
   login_button = By.CLASS_NAME,"android.widget.Button"

   def login_input_name(self,text):
       self.input(self.login_name,text)

   def login_input_password(self,text):
       self.input(self.login_password,text)

   def login_me_button(self):
       self.click(self.login_button)
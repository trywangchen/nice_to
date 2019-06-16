from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        """
        根据特征，找元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    def find_elements(self, feature, timeout=10, poll=1.0):
        """
        根据特征，找多个符合条件的元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
        return element

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        self.find_element(feature).clear()

    def is_toast_exist(self,message):
        message_xpath = By.XPATH,"//*[contains(@text,'%s')]" % message
        try: # 根据本分文本断言  有返回True 然则返回False
            self.find_element(message_xpath,5,0.1)   #  较少超时长 增加频率 更快获取到
            return True
        except TimeoutException:
            return False

    def get_toast(self,message): # 根据部分文本获取全部文本 如上获取文本 重新定位元素获取文本
        if self.is_toast_exist(message):#  若 返回False 主动跑出异常
            message_xpath = By.XPATH,"//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast不存在")



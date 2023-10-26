"""
    表现层代码
    存放测试数据以及需要定位的元素
    管理登陆页面所有的元素，
    以及操作这些元素所用的方法。
"""
from common.base import Base
from selenium.webdriver.common.by import By
import time


class Login_baidu(Base):
    # 编写定位器和页面属性
    baidu_input_locator = (By.ID, "kw")
    baidu_click_locator = (By.ID, "su")
    csdn_click_locator = (By.XPATH, "//*[@id='1']/div/div[1]/h3/a[1]")
    url = 'https://www.baidu.com'
    search_text = 'csdn'
    before_login_locator = (By.XPATH, "//*[@id='csdn-toolbar']/div/div/div[3]/div/div[1]/a")
    after_login_locator = (By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[1]/a/img")
    pass_login_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/span[4]')
    phone_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/input')
    passwd_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/input')
    agree_button_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/p/div/i')
    login_button_locator = (By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[4]/button')
    after_name_locator = (By.XPATH, '//*[@id="userSkin"]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div['
                                    '1]')
    private_name_locator = (By.XPATH, '//*[@id="userSkin"]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[1]')
    assert_text = ['登录', '彭湃0623', '用户名或密码错误']
    wrong_text_locator = (By.CLASS_NAME, 'login-form-error')
    login_page_iframe_name = 'passport_iframe'

    # """封装元素操作"""

    # 输入框输入'csdn'
    def input_csdn(self):
        self.send_keys(self.baidu_input_locator, self.search_text)

    # 点击百度一下
    def click_baiduyixia(self):
        self.click(self.baidu_click_locator)

    # 点击CSDN链接
    def click_csdn_link(self):
        self.click(self.csdn_click_locator)

    def switch_new_window(self):
        self.switch_window(-1)

    # 切换iframe窗口
    def switch_login_iframe(self):
        time.sleep(1)
        self.switch_iframe(self.login_page_iframe_name)

    # 断言
    def asset_before_login_locator_text(self):
        if self.find_element_text(self.before_login_locator) == self.assert_text[0]:
            print("登入CSDN首页成功")
        else:  # pragma:no cover
            print("登入CSDN首页失败")  # pragma:no cover

    def assert_after_name_locator_text(self):
        if self.find_element_text(self.private_name_locator) == self.assert_text[1]:
            print("CSDN登录成功，成功进入个人主页")
        else:  # pragma:no cover
            print("CSDN登录失败")  # pragma:no cover

    def assert_wrong_passwd_text(self):
        time.sleep(1)
        if self.find_element_text(self.wrong_text_locator) == self.assert_text[2]:
            print("错误提示准确")
        else:  # pragma:no cover
            print("无法定位错误信息")  # pragma:no cover

    # 点击未登录前“登录”框
    def click_before_login(self):
        self.click(self.before_login_locator)

    # 点击密码登录
    def click_passwd_login(self):
        self.click(self.pass_login_locator)

    # 输入账号
    def input_phone(self, phone):
        self.send_keys(self.phone_locator, phone)

    # 输出密码
    def input_passwd(self, passwd):
        self.send_keys(self.passwd_locator, passwd)

    def clear_wrong_text(self):
        self.clear_text(self.passwd_locator)

    # 点击我已阅读
    def click_agree(self):
        self.click(self.agree_button_locator)

    # 点击登录
    def click_login_button(self):
        self.click(self.login_button_locator)

    # 点击登录后“登录”框
    def click_after_login(self):
        self.click(self.after_login_locator)


if __name__ == '__main__':
    base = Base()
    base.open_url(url=Login_baidu.url)

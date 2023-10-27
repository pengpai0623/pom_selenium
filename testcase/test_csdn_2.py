"""
存放测试用例，包括测试步骤和断言
"""
import pytest


@pytest.fixture(scope='class')
def setup3():
    print("夹具顺序验证-3")
    yield
    print("夹具顺序验证-6")
# 控输出1 - 2 - 3 - 6 -5 -4


# 定义测试类
class TestCaseLogin(object):
    @pytest.mark.parametrize("phone,passwd", [('18883245086', 'eb1019EBD11')])
    def test_correct_login(self, setup1, phone, passwd):
        """
        正确帐密登陆测试用例
        :param setup1: fixture
        :return: 无返回值
        """
        self.driver = setup1
        # 断言
        self.driver.asset_before_login_locator_text()
        self.driver.click_before_login()
        self.driver.switch_login_iframe()
        self.driver.click_passwd_login()
        # 输入正确帐密登录
        self.driver.input_phone(phone)
        self.driver.input_passwd(passwd)
        self.driver.click_agree()
        self.driver.click_login_button()
        self.driver.switch_new_window()
        self.driver.click_after_login()
        # 断言
        self.driver.assert_after_name_locator_text()
        # self.driver.close()

    @pytest.mark.parametrize("phone,passwd",
                             [('18883245086', 'eb1019EBD1'), ('18883245086', 'eb1019EBD')])
    def test_wrong_login(self, setup1, phone, passwd):
        """
        通过参数化的方式实现错误帐密登录
        :param setup1: fixture
        :return: 无返回值
        """
        self.driver = setup1
        # 断言
        self.driver.asset_before_login_locator_text()
        self.driver.click_before_login()
        self.driver.switch_login_iframe()
        self.driver.click_passwd_login()
        self.driver.input_phone(phone)
        # 输入错误密码，尝试登录，断言错误提示
        self.driver.input_passwd(passwd)
        self.driver.click_agree()
        self.driver.click_login_button()
        self.driver.assert_wrong_passwd_text()
        # self.driver.close()


if __name__ == '__main__':
    pytest.main(['-q', '-s', 'test_csdn_2.py'])

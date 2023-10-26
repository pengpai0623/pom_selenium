# """
# 存放测试用例，包括测试步骤和断言
# """
#
#
# # 定义测试类
# class TestCaseLogin(object):
#     def test_Login(self, setup):
#         """登陆测试用例"""
#         self.driver = setup
#         # 断言
#         self.driver.asset_before_login_locator_text()
#         self.driver.click_before_login()
#         self.driver.switch_login_iframe()
#         self.driver.click_passwd_login()
#         self.driver.input_phone()
#         # 输入错误密码，尝试登录，断言错误提示
#         self.driver.input_wrong_passwd()
#         self.driver.click_agree()
#         self.driver.click_login_button()
#         self.driver.assert_wrong_passwd_text()
#         self.driver.clear_wrong_text()
#         # 输入正确帐密登录
#         self.driver.input_correct_passwd()
#         self.driver.click_login_button()
#         self.driver.switch_new_window()
#         self.driver.click_after_login()
#         # 断言
#         self.driver.assert_after_name_locator_text()
#         self.driver.close()
#         self.driver.close()
#
#

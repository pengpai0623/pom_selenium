"""
对元素的操作方式，比如点击 输入等
"""
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base(object):
    def __init__(self, browser='chrome'):
        """
        初始化driver
        :param browser: 浏览器
        """
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':  # pragma:no cover
            self.driver = webdriver.Firefox()  # pragma:no cover
        elif browser == 'ie':  # pragma:no cover
            self.driver = webdriver.Ie()  # pragma:no cover
        else:  # pragma:no cover
            raise ValueError("请选择正确的浏览器，例如'chrome,firefox,ie'")  # pragma:no cover

    def open_url(self, url):
        """
        open链接地址
        :return:
        """
        self.driver.get(url)
        time.sleep(1)

    def find_element(self, locator, timeout=10, poll_frequency=0.5):
        """
        定位单个元素
        :param poll_frequency:
        :param locator:定位器，例如('id','id属性值')
        :param timeout:
        :return:元素本身
        """
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator))
            return element
        except:  # pragma:no cover
            print(f"{locator}无法定位到元素")  # pragma:no cover
            return False  # pragma:no cover

    def find_element_text(self, locator):
        """
        定位元素text值
        :return: text值
        """
        try:
            element = self.find_element(locator)
            return element.text
        except:  # pragma:no cover
            print(f"{locator}无法定位到元素")  # pragma:no cover
            return False  # pragma:no cover

    def clear_text(self, locator):
        element = self.find_element(locator)
        element.clear()

    def click(self, locator):
        """
        点击元素
        :param locator:
        :return:
        """
        try:
            element = self.find_element(locator)
            element.click()
        except:  # pragma:no cover
            print(f"{locator}无法点击，请查找原因")  # pragma:no cover

    def send_keys(self, locator, text):
        """
        元素输入
        :param text:
        :param locator:
        :return:
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        """
        关闭浏览器
        :return:
        """
        time.sleep(2)  # pragma:no cover
        self.driver.quit()  # pragma:no cover

    def max_window(self):
        self.driver.maximize_window()

    # 切换窗口方法，需要传入窗口对应索引值
    def switch_window(self, index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    # 切换iframe
    def switch_iframe(self, iframe_name):
        self.driver.switch_to.frame(iframe_name)


if __name__ == '__main__':
    base = Base()
    base.open_url("https://www.baidu.com")
    base.close()

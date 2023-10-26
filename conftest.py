import pytest
from pages.baidu_page import Login_baidu


@pytest.fixture(scope='class')
def setup1():
    print("夹具顺序验证-1")
    driver = Login_baidu()
    driver.open_url(driver.url)
    driver.max_window()
    driver.input_csdn()
    driver.click_baiduyixia()
    driver.click_csdn_link()
    driver.switch_new_window()
    yield driver
    print("夹具顺序验证-4")
    driver.close()




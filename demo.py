import pytest


@pytest.fixture(scope='class')
def setup():
    print("开始执行")
    yield
    print("结束执行")


class Test_login:
    def test_1(self):
        assert 1 == 1
        print('test_1执行完毕')

    def test_2(self, setup):
        assert 2 == 2
        print('test_2执行完毕')
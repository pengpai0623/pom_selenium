import pytest

@pytest.fixture()
def setup2():
    print("夹具顺序验证-2")
    yield
    print("夹具顺序验证-5")
import pytest
import os

if __name__ == '__main__':
    # pytest.main(['-q', '-s'])
    pytest.main(['-s', '-q', '--clean-alluredir'])
    os.system(r"allure serve report")

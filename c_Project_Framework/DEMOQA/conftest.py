from selenium import webdriver
import pytest
import time
import logging
from TestData.userpass import LoginData

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")      # tst bedanya klo ga pake ini
def setup(request):
    browsers = request.config.getoption("browser")

    if browsers == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #utk chrome
        options.add_argument("--disable-notifications")                        #utk chrome
        #options.headless = True
        drv = webdriver.Chrome(options=options)
    elif browsers == "firefox":
        options = webdriver.FirefoxOptions()
        #options.headless = True
        drv = webdriver.Firefox(options=options)   

    drv.maximize_window()               
    drv.get('https://demoqa.com/login')
    drv.implicitly_wait(15)
    request.cls.drv = drv           
    yield                             
    #time.sleep(2)
    drv.quit()

#userpass berhasil
@pytest.fixture(params=LoginData.login_valid)
def loginvalid(request):
    yield request.param


#userpass salah
@pytest.fixture(params=LoginData.login_invalid)              # user salah, pass salah - 6
def login_invalid(request):
    yield request.param


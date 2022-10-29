from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def setup():
    options = webdriver.FirefoxOptions()
    options.headless = True
    drv = webdriver.Firefox(options=options)
    drv.get('https://rahulshettyacademy.com/dropdownsPractise/')
    #drv.minimize_window()
    drv.implicitly_wait(15)
    yield drv
    #drv.minimize_window()

@pytest.mark.testautosuggestcombobox
def test_autoSuggestiveComboBox(setup):
    setup.find_element(By.ID, 'autosuggest').send_keys('in')
    time.sleep(2)
    negara = setup.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
    print(len(negara))
    print(type(negara))

    for iter in negara:
        if iter.text == 'Indonesia':
            iter.click()
            break
    a = setup.find_element(By.ID, 'autosuggest').get_attribute('value')
    assert a == 'Indonesia'

import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def wb():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
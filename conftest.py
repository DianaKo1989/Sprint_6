import pytest
from selenium import webdriver
from test_data import url

@pytest.fixture(scope='function')
def wb():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()
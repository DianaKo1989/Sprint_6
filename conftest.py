import pytest
from selenium import webdriver

@pytest.fixture
def wb():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
from selenium import webdriver
from locators.base_page_locators import yndx, main, cookie_btn

class BasePage:
    def __init__(self) -> None:
        self.url = 'https://qa-scooter.praktikum-services.ru'
        self.wb = webdriver.Chrome()

    def open_browser(self):
        self.wb.get(self.url)
        self.wb.find_element(*cookie_btn).click()

    def close_browser(self):
        self.wb.quit()

    def click_logo_scooter(self):
        self.wb.find_element(*main).click()

    def click_logo_yndx(self):
        self.wb.find_element(*yndx).click()
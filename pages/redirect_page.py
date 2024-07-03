from pages.base_page import BasePage
from locators.base_page_locators import main, yndx
import allure

class RedirectPage(BasePage):

    def __init__(self):
        super().__init__()
        self.open_browser()

    @allure.step('Нажимаем на логотип «Самоката»')
    def click_logo_scooter(self):
        self.click_to_element(*main)

    @allure.step('Нажимаем на логотип Яндекса')
    def click_logo_yndx(self):
        self.click_to_element(*yndx)
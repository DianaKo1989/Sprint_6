from locators.base_page_locators import yndx, main, cookie_btn
import allure

class BasePage:

    def __init__(self, wb) -> None:
        self.url = 'https://qa-scooter.praktikum-services.ru'
        self.wb = wb

    allure.step('Открываем браузер')
    def open_browser(self):
        self.wb.get(self.url)
        self.wb.find_element(*cookie_btn).click()

    allure.step('Закрываем браузер')
    def close_browser(self):
        self.wb.quit()

    allure.step('Нажимаем на логотип «Самоката»')
    def click_logo_scooter(self):
        self.wb.find_element(*main).click()

    allure.step('Нажимаем на логотип Яндекса')
    def click_logo_yndx(self):
        self.wb.find_element(*yndx).click()

    
    def find_element(self):
        pass

    def find_elements(self):
        pass    

    def send_keys(self):
        pass

    def click(self):
        pass    
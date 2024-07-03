from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import cookie_btn
import allure

class BasePage:

    def __init__(self, wb) -> None:
        self.url = 'https://qa-scooter.praktikum-services.ru'
        self.wb = wb

    allure.step('Открываем браузер')
    def open_browser(self):
        self.wb.get(self.url)
        self.accept_cookies()

    allure.step('Закрываем браузер')
    def close_browser(self):
        self.wb.quit()

    @allure.step('Находим элемент')
    def find_element_with_wait(self, locator, index=0, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)[index]

    @allure.step('Кликаем по элементу')
    def click_to_element(self, locator, index=0):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                locator))
        self.driver.find_element(*locator)[index].click()

    @allure.step('Вводим текст')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)

    @allure.step('Кликаем на кнопку принятия cookies')
    def accept_cookies(self):
        self.click_to_element(*cookie_btn)

    @allure.step('Переключаемся на вкладку')
    def change_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])
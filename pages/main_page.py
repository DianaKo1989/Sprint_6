from pages.base_page import BasePage
from locators.base_page_locators import cookie_btn, xpath_text_template
from selenium.webdriver.common.by import By 
import allure

class MainPage(BasePage):
    
    def __init__(self):
        super().__init__()
        self.open_browser()

    @allure.step('Нажимаем на вопрос')
    def click_question(self, question: str):
        question_loc = xpath_text_template % question
        self.wb.find_element(By.XPATH, question_loc).click()

    @allure.step('Получаем ответ')
    def get_answer(self, answer: str):
        answer_loc = xpath_text_template % answer
        a_block = self.wb.find_element(By.XPATH, answer_loc)
        return a_block
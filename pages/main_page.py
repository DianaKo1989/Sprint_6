from pages.base_page import BasePage
from locators.base_page_locators import xpath_text_template
import allure

class MainPage(BasePage):
    
    def __init__(self):
        super().__init__()
        self.open_browser()

    @allure.step('Нажимаем на вопрос')
    def click_question(self, question: str):
        question_loc = self.format_locator(xpath_text_template, question)
        self.click_to_element(question_loc)

    @allure.step('Получаем ответ')
    def get_answer(self, answer: str):
        answer_loc = self.format_locator(xpath_text_template, answer)
        return self.find_element_with_wait(answer_loc)
   
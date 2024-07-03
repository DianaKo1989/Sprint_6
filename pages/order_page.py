from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import allure
from locators.order_page_locators import (
    order_btn, 
    approve_btn, 
    name_fld,
    lname_fld,
    subway_fld,
    address_fld,
    phone_fld,
    next_btn,
    date_field,
    selector,
    selector_option,
    choice_box,
    comment_fld

)

class OrderPage(BasePage):
    def __init__(self):
        super().__init__()
        self.open_browser()

    @allure.step('Нажимаем на кнопку "Заказать (верхнюю)"')
    def click_top_order_button(self):
        self.wb.find_elements(*order_btn)[0].click()

    @allure.step('Нажимаем на кнопку "Заказать (нижнюю)"')
    def click_bottom_order_button(self):
        self.wb.find_elements(*order_btn)[1].click()

    @allure.step('Закрываем модальное окно')
    def close_modal(self):
        self.click_to_element(*approve_btn)

    @allure.step('Заполняем поля для заказа')
    def fill_the_order(self, data):
        self.add_text_to_element(*name_fld, data[0])
        self.add_text_to_element(*lname_fld, data[1])
        sub_fld = self.find_element_with_wait(*subway_fld)
        self.click_to_element(sub_fld)
        self.add_text_to_element(sub_fld, data[2])
        sub_fld.send_keys(Keys.ARROW_DOWN)
        sub_fld.send_keys(Keys.ENTER)
        self.add_text_to_element(*address_fld, data[3])
        self.add_text_to_element(*phone_fld, data[4])
        self.wb.find_element(*next_btn).click()
        self.add_text_to_element(*date_field, data[5])
        self.click_to_element(*selector, -1)
        self.click_to_element(*selector_option, data[6])
        self.click_to_element(*choice_box)
        self.add_text_to_element(*comment_fld, data[7])
        self.click_to_element(*order_btn, -1)
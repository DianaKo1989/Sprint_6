from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
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

    def click_top_order_button(self):
        self.wb.find_elements(*order_btn)[0].click()

    def click_bottom_order_button(self):
        self.wb.find_elements(*order_btn)[1].click()

    def close_modal(self):
        self.wb.find_element(*approve_btn).click()

    def fill_the_order(self, data):
        self.wb.find_element(*name_fld).send_keys(data[0])
        self.wb.find_element(*lname_fld).send_keys(data[1])
        sub_fld = self.wb.find_element(*subway_fld)
        sub_fld.click()
        sub_fld.send_keys(data[2])
        sub_fld.send_keys(Keys.ARROW_DOWN)
        sub_fld.send_keys(Keys.ENTER)
        self.wb.find_element(*address_fld).send_keys(data[3])
        self.wb.find_element(*phone_fld).send_keys(data[4])
        self.wb.find_element(*next_btn).click()
        self.wb.find_element(*date_field).send_keys(data[5])
        self.wb.find_elements(*selector)[-1].click()
        self.wb.find_elements(*selector_option)[data[6]].click()
        self.wb.find_element(*choice_box).click()
        self.wb.find_element(*comment_fld).send_keys(data[7])
        self.wb.find_elements(*order_btn)[-1].click()

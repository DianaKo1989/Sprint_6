from selenium.webdriver.common.by import By
from locators.base_page_locators import xpath_text_template

xpath_ph_template = "//input[@placeholder='%s']"
name_fld = [By.XPATH, xpath_ph_template % '* Имя']
lname_fld = [By.XPATH, xpath_ph_template % '* Фамилия']
subway_fld = [By.XPATH, xpath_ph_template % '* Станция метро']
address_fld = [By.XPATH, xpath_ph_template % '* Адрес: куда привезти заказ']
phone_fld = [By.XPATH, xpath_ph_template % '* Телефон: на него позвонит курьер']
comment_fld = [By.XPATH, xpath_ph_template % 'Комментарий для курьера']
date_field = [By.XPATH, xpath_ph_template % '* Когда привезти самокат']

selector = [By.XPATH, "//*[contains(@class, 'Dropdown-arrow')]"]
selector_option = [By.XPATH, "//*[contains(@class, 'Dropdown-option')]"]

next_btn = [By.XPATH, xpath_text_template % 'Далее']
order_btn = [By.XPATH, xpath_text_template % 'Заказать']
approve_btn = [By.XPATH, xpath_text_template % 'Нет']
choice_box = [By.XPATH, xpath_text_template % 'чёрный жемчуг']
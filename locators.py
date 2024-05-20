cookie_btn = "//*[contains(text(), 'да все привыкли')]"

selector = "//*[contains(@class, 'Dropdown-arrow')]"
selector_option = "//*[contains(@class, 'Dropdown-option')]"


xpath_ph_template = "//input[@placeholder='%s']"
name_fld = xpath_ph_template % '* Имя'
lname_fld = xpath_ph_template % '* Фамилия'
subway_fld = xpath_ph_template % '* Станция метро'
address_fld = xpath_ph_template % '* Адрес: куда привезти заказ'
phone_fld = xpath_ph_template % '* Телефон: на него позвонит курьер'
comment_fld = xpath_ph_template % 'Комментарий для курьера'
date_field = xpath_ph_template % '* Когда привезти самокат'


xpath_text_template = "//*[contains(text(), '%s')]"
next_btn = xpath_text_template % 'Далее'
order_btn = xpath_text_template % 'Заказать'
approve_btn = xpath_text_template % 'Нет'
choice_box = xpath_text_template % 'чёрный жемчуг'


main = '[alt="Scooter"]'
yndx = '[alt="Yandex"]'
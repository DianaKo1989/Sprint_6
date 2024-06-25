from selenium.webdriver.common.by import By 

cookie_btn = [By.XPATH, "//*[contains(text(), 'да все привыкли')]"]
main = [By.CSS_SELECTOR, '[alt="Scooter"]']
yndx = [By.CSS_SELECTOR, '[alt="Yandex"]']

xpath_text_template = "//*[contains(text(), '%s')]"

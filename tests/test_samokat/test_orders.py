import pytest
import allure
from selenium.webdriver.common.by import By       
import locators as locs
from selenium.webdriver.common.keys import Keys



@allure.story('Оформление заказа')
class TestOrders:
    @allure.title('E2E тест заказа')
    @pytest.mark.parametrize('data', [
        [0, 'Борис', 'Бритва', 'Преображенская площадь', 'ул. Пушкина', '89217657867', '14.05.2024', 2, 'домофон'],
        [1, 'Олег', 'Сикрет', 'Юго-западная', 'ул. Садовое кольцо', '89117647162', '16.05.2024', 5, 'спущусь']
    ])
    def test_make_order_e2e(self, wb, data):
        wb.find_element(By.XPATH, locs.cookie_btn).click()
        with allure.step('Нажимаем кнопку «Заказать», на странице их две'):
            wb.find_elements(By.XPATH, locs.order_btn)[data[0]].click()
        with allure.step('Заполняем форму заказа'):
            wb.find_element(By.XPATH, locs.name_fld).send_keys(data[1])
            wb.find_element(By.XPATH, locs.lname_fld).send_keys(data[2])
            sub_fld = wb.find_element(By.XPATH, locs.subway_fld)
            sub_fld.click()
            sub_fld.send_keys(data[3])
            sub_fld.send_keys(Keys.ARROW_DOWN)
            sub_fld.send_keys(Keys.ENTER)
            wb.find_element(By.XPATH, locs.address_fld).send_keys(data[4])
            wb.find_element(By.XPATH, locs.phone_fld).send_keys(data[5])
            wb.find_element(By.XPATH, locs.next_btn).click()
            wb.find_element(By.XPATH, locs.date_field).send_keys(data[6])
            wb.find_elements(By.XPATH, locs.selector)[-1].click()
            wb.find_elements(By.XPATH, locs.selector_option)[data[7]].click()
            wb.find_element(By.XPATH, locs.choice_box).click()
            wb.find_element(By.XPATH, locs.comment_fld).send_keys(data[8])
            wb.find_elements(By.XPATH, locs.order_btn)[-1].click()
        with allure.step('Проверяем, что появилось всплывающее окно и закрыавем его'):
            wb.find_element(By.XPATH, locs.approve_btn).click()
        with allure.step('Нажимаем на логотип «Самоката»'):
            wb.find_element(By.CSS_SELECTOR, locs.main).click()
            with allure.step('Проверяем, что открылась главная страница «Самоката»'):
                assert wb.current_url == 'https://qa-scooter.praktikum-services.ru/'
        with allure.step('Нажимаем на логотип «Яндекса»'):
            wb.find_element(By.CSS_SELECTOR, locs.yndx).click()
            tabs = wb.window_handles
            wb.switch_to.window(tabs[1])
            with allure.step('Проверяем, что открылась страница «Дзэна»'):
                assert 'dzen.ru' in wb.current_url
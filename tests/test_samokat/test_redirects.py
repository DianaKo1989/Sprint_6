import allure
from pages.order_page import OrderPage



@allure.story('Редиректы логотипа')
class TestOrders:
    @allure.title('E2E тест на клик по логотипам')
    def test_make_order_e2e(self):
        op = OrderPage()
        op.click_logo_scooter()
        with allure.step('Проверяем, что открылась главная страница «Самоката»'):
            assert op.wb.current_url == 'https://qa-scooter.praktikum-services.ru/'
        op.click_logo_yndx()
        tabs = op.wb.window_handles
        op.wb.switch_to.window(tabs[1])
        with allure.step('Проверяем, что открылась страница «Дзэна»'):
            assert 'dzen.ru' in op.wb.current_url
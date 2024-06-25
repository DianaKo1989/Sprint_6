import pytest
import allure
from pages.order_page import OrderPage



@allure.story('Оформление заказа')
class TestOrders:
    @allure.title('E2E тест заказа')
    @pytest.mark.parametrize('data', [
        ['top', 'Борис', 'Бритва', 'Преображенская площадь', 'ул. Пушкина', '89217657867', '14.05.2024', 2, 'домофон'],
        ['bottom', 'Олег', 'Сикрет', 'Юго-западная', 'ул. Садовое кольцо', '89117647162', '16.05.2024', 5, 'спущусь']
    ])
    def test_make_order_e2e(self, data):
        op = OrderPage()
        with allure.step(f'Нажимаем кнопку «Заказать» - {data[0]} (их две)'):
            getattr(op, f'click_{data[0]}_order_button')()
        with allure.step('Заполняем форму заказа'):
            op.fill_the_order(data[1:])
        with allure.step('Проверяем, что появилось всплывающее окно и закрыавем его'):
            op.close_modal()
        with allure.step('Нажимаем на логотип «Самоката»'):
            op.click_logo_scooter()
            with allure.step('Проверяем, что открылась главная страница «Самоката»'):
                assert op.wb.current_url == 'https://qa-scooter.praktikum-services.ru/'
        with allure.step('Нажимаем на логотип «Яндекса»'):
            op.click_logo_yndx()
            tabs = op.wb.window_handles
            op.wb.switch_to.window(tabs[1])
            with allure.step('Проверяем, что открылась страница «Дзэна»'):
                assert 'dzen.ru' in op.wb.current_url
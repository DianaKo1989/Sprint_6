from pages.redirect_page import RedirectPage
import allure


@allure.story('Редиректы логотипа')
class TestOrders:
    @allure.title('Тест на клик по логотипу Яндекса')
    def test_click_logo_main(self, wb):        
        rp = RedirectPage(wb)
        rp.click_logo_scooter()
        with allure.step('Проверяем, что открылась главная страница «Самоката»'):
            assert rp.wb.current_url == 'https://qa-scooter.praktikum-services.ru/'
        
    @allure.title('Тест на клик по логотипу Яндекса')
    def test_click_logo_dzen(self, wb):       
        rp = RedirectPage(wb) 
        rp.click_logo_yndx()
        rp.change_tab(1)
        with allure.step('Проверяем, что открылась страница «Дзэна»'):
            assert 'dzen.ru' in rp.wb.current_url
import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromLoginPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
    
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()                      # открываем страницу
        page = page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()

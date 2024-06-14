from pages.main_page import MainPage
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                      # открываем страницу
    product_page = ProductPage(browser,link)
    product_page.check_entities_should_be_product_page()
    product_page.solve_puzzle()


import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

@pytest.mark.step2
def test_step2_guest_can_add_product_to_basket(browser):
    promotext = "newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo={promotext}"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                      # открываем страницу
    product_page = ProductPage(browser,link)
    product_page.promo_text = promotext
    product_page.check_entities_should_be_product_page_step2()
    product_page.solve_puzzle_step2()

@pytest.mark.step3
def test_step3_guest_can_add_product_to_basket(browser):
    promotext = "newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promotext}"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                      # открываем страницу
    product_page = ProductPage(browser,link)
    product_page.promo_text = promotext
    product_page.check_entities_should_be_product_page_step3()
    product_page.solve_puzzle_step3()

@pytest.mark.step4
@pytest.mark.parametrize('promo_offer', [n if n != 7 else pytest.param(n, marks=pytest.mark.xfail) for n in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    promotext = f"offer{promo_offer}"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promotext}"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                      # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.promo_text = promotext
    product_page.check_entities_should_be_product_page_step3()
    product_page.solve_puzzle_step3()

@pytest.mark.step6
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                      # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_success_message()

@pytest.mark.step6
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                      # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_is_not_element_present()

@pytest.mark.step6
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                      # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_message_disappeared()

@pytest.mark.step8
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.step8
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.step10
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.click_cart_button()
    print(f"Processing URL: {browser.current_url}")
    page.should_not_be_product_block()
    page.should_be_cart_empty_text()

@pytest.mark.step10
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link)
    page.open()
    page.click_cart_button()
    print(f"Processing URL: {browser.current_url}")
    page.should_not_be_product_block()
    page.should_be_cart_empty_text()


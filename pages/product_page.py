from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.click_button_add_product()
    
    def check_entities_should_be_product_page_step2(self):
        print(f"Processing URL: {self.browser.current_url}")
        self.should_be_button_tell_me()

    def check_entities_should_be_product_page_step3(self):
        print(f"Processing URL: {self.browser.current_url}")
        self.should_be_button_add_product()

    def click_button_add_product(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        button_add_product.click()

    def click_button_tell_me(self):
        button_tell_me = self.browser.find_element(*ProductPageLocators.BUTTON_TELL_ME)
        button_tell_me.click()

    def compare_product_names(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        cart_added_product_name = self.browser.find_element(*ProductPageLocators.CART_ADDED_PRODUCT_NAME)
        assert product_name.text == cart_added_product_name.text,\
            f"url: {self.browser.current_url} product name: '{product_name.text}' != cart added product name: '{cart_added_product_name.text}'"

    def compare_product_prices(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_added_product_price = self.browser.find_element(*ProductPageLocators.CART_ADDED_PRODUCT_PRICE)
        assert product_price.text == cart_added_product_price.text,\
            f"url: {self.browser.current_url} product price: '{product_price.text}' != cart added product price basket: '{cart_added_product_price.text}'"

    def should_be_cart_added_product_name(self):
        assert self.is_element_present(*ProductPageLocators.CART_ADDED_PRODUCT_NAME), "Cart added product name is not presented"
        cart_added_product_name = self.browser.find_element(*ProductPageLocators.CART_ADDED_PRODUCT_NAME)
        print(f"Cart added product name: {cart_added_product_name.text}")

    def should_be_cart_added_product_price(self):
        assert self.is_element_present(*ProductPageLocators.CART_ADDED_PRODUCT_PRICE), "Cart added product price is not presented"
        cart_added_product_price = self.browser.find_element(*ProductPageLocators.CART_ADDED_PRODUCT_PRICE)
        print(f"Basket added product price: {cart_added_product_price.text}")

    def should_be_button_add_product(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_PRODUCT), "Add product button is not presented"

    def should_be_button_tell_me(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_TELL_ME), "Tell me button is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        print(f"Product name: {product_name.text}")

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        print(f"Product price: {product_price.text}")

    def should_be_promo_url(self):
        assert self.browser.current_url.find(f"?promo={self.promo_text}") != -1, f"url {self.browser.current_url} hasn't \"?promo={self.promo_text}\" substring"

    def should_be_element_us_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def should_be_is_not_element_present(self):
        print(f"current url: {self.browser.current_url}")
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_not_be_success_message()

    def should_be_message_disappeared(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_button_add_product()
        self.click_button_add_product()
        self.should_be_element_is_disappeared()

    def should_be_success_message(self):
        print(f"current url: {self.browser.current_url}")
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_button_add_product()
        self.click_button_add_product()
        self.should_not_be_success_message()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def solve_puzzle_step2(self):
        self.click_button_tell_me()
        self.solve_quiz_and_get_code()

    def solve_puzzle_step3(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_cart_added_product_name()
        self.should_be_cart_added_product_price()
        self.compare_product_names()
        self.compare_product_prices()

from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def check_entities_should_be_product_page(self):
        self.should_be_promo_url()
        self.should_be_button_tell_me()

    def solve_puzzle(self):
        self.click_button_tell_me()
        self.solve_quiz_and_get_code()

    def should_be_promo_url(self):
        assert self.browser.current_url.find("?promo=newYear") != -1, f"url {self.browser.current_url} hasn't \"?promo=newYear\" substring"

    def should_be_button_tell_me(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_TELL_ME), "Tell me button is not presented"

    def click_button_tell_me(self):
        button_tell_me = self.browser.find_element(*ProductPageLocators.BUTTON_TELL_ME)
        button_tell_me.click()

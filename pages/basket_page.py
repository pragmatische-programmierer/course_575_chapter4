from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):

    def should_not_be_product_block(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_BLOCK), \
            "Product block is presented, but should not be"

    def should_be_cart_empty_text(self):
        browser_lang = self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
        print(f"browser language:\"{browser_lang}\"")
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty."
        }
        expected_text = languages[browser_lang]
        print(f"should be text: \"{expected_text}\"")
        basket_info = self.browser.find_element(*BasketPageLocators.CART_TEXT)
        assert basket_info.text.find(expected_text) != -1
        

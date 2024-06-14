from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")

class BasketPageLocators():
    PRODUCT_BLOCK = (By.CSS_SELECTOR,"div.basket-items")
    CART_TEXT = (By.CSS_SELECTOR, "div#content_inner p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, "form#add_to_basket_form button[type='submit']")
    BUTTON_TELL_ME = (By.CSS_SELECTOR, "form#alert_form button[type='submit']")
    CART_ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    CART_ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "div#messages div.alert-info div.alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "article.product_page div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert-success") 

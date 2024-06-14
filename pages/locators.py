from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, "article.product_pod button[type='submit']")
    BUTTON_TELL_ME = (By.CSS_SELECTOR, "form#alert_form button[type='submit']")
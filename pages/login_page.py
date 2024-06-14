from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка корректности адреса URL
        assert self.browser.current_url.find("login") != -1, "url hasn't \"login\" substring"

    def should_be_login_form(self):
        # Проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email_val, password_val):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        login = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        login.send_keys(email_val)
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        registration_password.send_keys(password_val)
        registration_password_confirm.send_keys(password_val)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()

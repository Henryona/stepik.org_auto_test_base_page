from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка, что в адресе страницы есть "login"
        assert "login" in self.browser.current_url, "No 'login' in url on this page!"

    def should_be_login_form(self):
        # проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form on page!"

    def should_be_register_form(self):
        # проверка наличия формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form on page!"
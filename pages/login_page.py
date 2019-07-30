from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        substring = LoginPageLocators.SUBSTRING_LOGIN
        # проверка, что в адресе страницы есть "login"
        assert substring in self.browser.current_url, "No 'login' in url on this page!"

    def should_be_login_form(self):
        # проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form on page!"

    def should_be_register_form(self):
        # проверка наличия формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form on page!"

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        self.email = email
        self.password = password

        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDR_INPUT)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT)
        pass_input.send_keys(password)
        pass_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT)
        pass_confirm.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()
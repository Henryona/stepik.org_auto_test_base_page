from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
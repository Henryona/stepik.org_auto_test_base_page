from selenium.webdriver.common.by import By

class MainPageLocators():
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com"
    LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():
    SUBSTRING_LOGIN = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
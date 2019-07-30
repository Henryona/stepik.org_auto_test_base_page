from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    # тут стало пусто, поэтому тут заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

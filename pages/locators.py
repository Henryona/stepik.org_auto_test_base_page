from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com"
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    SUBSTRING_LOGIN = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    PRODUCT_PAGE_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    BOOK_TO_COMPARE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_TO_COMPARE = (By.CLASS_NAME, "price_color")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRICE_NUMBER = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")
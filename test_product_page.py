from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

'''@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])'''
class TestUserAddToCartFromProductPage(object):
    def test_guest_can_add_product_to_cart(browser): #, link):
        link = ProductPageLocators.PRODUCT_PAGE_PROMO
    
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
        page = ProductPage(browser, link)

        # открываем нужную страницу
        page.open()

        bookToCompare = page.find_book_name()
        priceToCompare = page.find_book_price()

        # добавляем товар в корзину
        page.add_item_to_cart()

        page.solve_quiz_and_get_code()
        page.right_book_and_right_price_message(bookToCompare, priceToCompare)

def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = MainPage(browser, link)
	# открываем нужную страницу
    page.open()
	# выполняем метод страницы: переходим на страницу логина
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
	

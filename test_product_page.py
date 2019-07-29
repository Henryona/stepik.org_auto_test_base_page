from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    link = link
    
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

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

'''def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = ProductPage(browser, link)

    # открываем нужную страницу
    page.open()

    bookToCompare = page.find_book_name()
    priceToCompare = page.find_book_price()

    # добавляем товар в корзину
    page.add_item_to_cart()
    page.should_not_be_success_message()'''

def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = ProductPage(browser, link)

	# открываем нужную страницу
    page.open()
    page.should_not_be_success_message()

'''def test_message_disappeared_after_adding_product_to_cart(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = ProductPage(browser, link)

    # открываем нужную страницу
    page.open()
    page.add_item_to_cart()
    page.should_disappear()'''
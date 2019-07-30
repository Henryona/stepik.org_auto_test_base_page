from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def find_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_TO_COMPARE).text
        
    def find_book_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_TO_COMPARE).text
 
    def add_item_to_cart(self):
        # находим кнопку и добавляем товар в корзину
        addButton = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        addButton.click()
    
    def right_book_and_right_price_message(self, bookToCompare, priceToCompare):
        self.should_be_right_book_name(bookToCompare)
        self.should_be_right_price_for_book(priceToCompare)

    def should_be_right_book_name(self, bookToCompare):
        # проверка сообщения о добавлении в корзину нужной книги
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == bookToCompare, "No added book in a cart!"

    def should_be_right_price_for_book(self, priceToCompare):
        # проверка сообщения о цене товара в корзине
        assert self.browser.find_element(*ProductPageLocators.PRICE_NUMBER).text == priceToCompare, "Wrong price for the book!"

    def should_not_be_success_message(self):
        # проверка, что элемент не появился, так как не должен был
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear(self):
        # проверка, что элемент исчез
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message is not disappeared, but should"

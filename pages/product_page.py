from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def find_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_TO_COMPARE).text
        
    def find_book_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_TO_COMPARE).text
 
    def add_item_to_cart(self):
        # находим кнопку и добавляем товар в корзину
        addButton = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        addButton.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def right_book_and_right_price_message(self, bookToCompare, priceToCompare):
        self.should_be_right_book_name(bookToCompare)
        self.should_be_right_price_for_book(priceToCompare)

    def should_be_right_book_name(self, bookToCompare):
        # проверка сообщения о добавлении в корзину нужной книги
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == bookToCompare, "No added book in a cart!"

    def should_be_right_price_for_book(self, priceToCompare):
        # проверка сообщения о цене товара в корзине
        assert self.browser.find_element(*ProductPageLocators.PRICE_NUMBER).text == priceToCompare, "Wrong price for the book!"

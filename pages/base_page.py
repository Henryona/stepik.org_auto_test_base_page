from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class BasePage(object):
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
	
    def open(self):
        self.browser.get(self.url)
		
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

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        # перехватим исключение
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # проверка, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

'''Можно добавить в BasePage абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени: 

def is_not_element_present(self, how, what, timeout=4):
    try:
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return True

    return False

Тогда его использование Page Object для страницы товара будет выглядеть так: 

def should_not_be_success_message(self):
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем: 

def is_disappeared(self, how, what, timeout=4):
    try:
        WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return False

    return True

Метод-проверка в классе про страницу товара будет выглядеть аналогично should_not_be_success_message, напишите его самостоятельно.

 

Обратите внимание на разницу между методами is_not_element_present и is_disappeared. 

is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый. 

is_disappeared: будет ждать до тех пор, пока элемент не исчезнет. '''
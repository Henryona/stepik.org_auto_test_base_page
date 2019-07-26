from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
	
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        # перехватим исключение
        except (NoSuchElementException):
            return False
        return True
from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

def test_guest_should_see_login_link(browser):
    link = MainPageLocators.MAIN_PAGE_LINK
    
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = MainPage(browser, link)

    # открываем нужную страницу
    page.open()
	# выполняем метод страницы: ищем переход на страницу логина
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.MAIN_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = MainPage(browser, link)
	# открываем нужную страницу
    page.open()
	# выполняем метод страницы: переходим на страницу логина
    login_page = page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
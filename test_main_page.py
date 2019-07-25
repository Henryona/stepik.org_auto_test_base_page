from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" 

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = MainPage(browser, link)

	# открываем нужную страницу
    page.open()
	# выполняем метод страницы: переходим на страницу логина
    page.go_to_login_page()
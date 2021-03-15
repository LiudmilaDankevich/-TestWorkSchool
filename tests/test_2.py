from pages.login_in_page import LoginPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from time import sleep


def test_user_login(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    login_page = LoginPage(browser)
    sleep(1)
    login_page.login('liudmilaDan@gmail.com', '111111')
    sleep(2)

    # duck = CartPage(browser)
    # duck.choice_duck()


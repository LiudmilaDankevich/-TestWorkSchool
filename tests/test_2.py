from pages.login_in_page import LoginPage
from pages.rubber_duck_page import RubberDuckPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from time import sleep


def test_buy_ducks_in_the_store(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    login_page = LoginPage(browser)
    sleep(1)
    login_page.login('liud@gmail.com', '1111')
    sleep(2)
    duck = RubberDuckPage(browser)
    duck.choose_duck()
    sleep(2)
    duck.change_the_number_of_duck('3')
    duck.click_add_to_cart()
    # cart_page = CartPage(browser)
    # cart_page.click_cart()
    # cart_page.should_be_quantity_duck()
    # sleep(2)
    # cart_page.should_be_sum_duck()






from pages.login_in_page import LoginPage
from pages.rubber_duck_page import RubberDuckPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from time import sleep



def test_buy_ducks_in_the_store(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    login_page = LoginPage(browser)
    login_page.login('liud@gmail.com', '1111')
    duck = RubberDuckPage(browser)
    duck.choose_duck()
    duck.change_the_number_of_duck('3')
    duck.click_add_to_cart()
    sleep(2)
    duck.click_cart()

    cart_page = CartPage(browser)
    # cart_page.click_cart()
    # cart_page
    cart_page.should_be_quantity_duck()
    # cart_page.should_be_cost_duck()
    cart_page.click_confirm_order()
    # data_base = DataBase()
    # data_base.connect()






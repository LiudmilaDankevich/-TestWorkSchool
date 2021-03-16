from pages.base_page import BasePage
from locator.cart_locator import CartPageLocator
from time import sleep


class CartPage(BasePage):

    def click_cart(self):
        click_cart_order = self.find_element(
            CartPageLocator.LOCATOR_CURT_BUTTON
        )
        click_cart_order.click()
        sleep(2)


    def should_be_quantity_duck(self):

        check_quantity_duck_text = self.find_element(CartPageLocator.LOCATOR_QUANTITY_CHECK).text
        check_quantity = "3"
        assert check_quantity_duck_text == check_quantity, f'Text on UI {check_quantity_duck_text} is not eq {check_quantity}'


    def should_be_sum_duck(self):

        check_sum_duck = self.find_element(CartPageLocator.LOCATOR_SUM_CHECK).text
        check_sum = "43.56 €"
        assert check_sum_duck == check_sum, f'Text on UI {check_sum_duck} is not eq {check_sum}'



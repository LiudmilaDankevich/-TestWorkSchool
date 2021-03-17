from pages.base_page import BasePage
from locator.cart_locator import CartPageLocator
from time import sleep


class CartPage(BasePage):


    def should_be_quantity_duck(self):

        check_quantity_duck_text = self.find_element(CartPageLocator.LOCATOR_QUANTITY_CHECK).text
        check_quantity = '3'
        assert check_quantity_duck_text == check_quantity, f'Text on UI {check_quantity_duck_text} is not eq {check_quantity}'


    # def should_be_cost_duck(self):
    #
    #     check_cost_duck = self.find_element(CartPageLocator.LOCATOR_COST_CHECK).text
    #     check_cost = "14.52 €"
    #     assert check_cost_duck == check_cost, f'Text on UI {check_cost_duck} is not eq {check_cost}'

    def click_confirm_order(self):
        click_order = self.find_element(
            CartPageLocator.LOCATOR_BUTTON_ORDER
        )
        click_order.click()




from pages.base_page import BasePage
from locator.rubber_duck_page_locator import RubberDuckPageLocator
from time import sleep


class RubberDuckPage(BasePage):
    def choose_duck(self):
        choose_duck_click = self.find_element(
            RubberDuckPageLocator.LOCATOR_DUCK_CLICK
        )
        choose_duck_click.click()

    def change_the_number_of_duck(self, number):
        change_the_number_of_duck = self.find_element(
            RubberDuckPageLocator.LOCATOR_QUANTITY_DUCK_FIELD
        )
        change_the_number_of_duck.click()
        change_the_number_of_duck.clear()
        change_the_number_of_duck.send_keys(number)

    def click_add_to_cart(self):
        add_to_cart = self.find_element(
            RubberDuckPageLocator.LOCATOR_ADD_TO_CART_BUTTON
        )
        add_to_cart.click()
        sleep(5)

    def click_cart(self):
        click_cart_order = self.find_element(
            RubberDuckPageLocator.LOCATOR_CURT_BUTTON
        )
        click_cart_order.click()



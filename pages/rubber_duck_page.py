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
        sleep(2)
        change_the_number_of_duck.send_keys(number)
        sleep(3)

    def click_add_to_cart(self):
        add_to_cart = self.find_element(
            RubberDuckPageLocator.LOCATOR_ADD_TO_CART_BUTTON
        )
        add_to_cart.click()


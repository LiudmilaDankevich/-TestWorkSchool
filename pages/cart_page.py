from pages.base_page import BasePage
from locator.cart_locator import CartPageLocator


class CartPage(BasePage):
    def choice_duck(self):
        choice_duck_click = self.find_element(
            CartPageLocator.LOCATOR_DUCK_CLICK
        )
        choice_duck_click.click()
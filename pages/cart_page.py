from pages.base_page import BasePage
from locator.cart_locator import CartPageLocator


class MainPage(BasePage):
    def choice_duck_by_name(self, name):
        choice_duck_click = self.find_element(
            CartPageLocator.get_duck_name_locator(name)
        )
        choice_duck_click.click()
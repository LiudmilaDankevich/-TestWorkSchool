from pages.base_page import BasePage
from locator.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def open_regional_page(self):
        regional_change_button = self.find_element(
            MainPageLocator.LOCATOR_REGIONAL_CHANGE_BUTTON
        )
        regional_change_button.click()





    def get_closes_name_on_the_page(self):
        pass
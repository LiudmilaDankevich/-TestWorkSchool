from pages.base_page import BasePage
from pages.main_page import MainPage
from locator.regional_settings_page_locator import RegionalSettingsPageLocator


class RegionalSettingsPage(BasePage):


    def should_be_regional_settings_page(self):

        regional_settings_text = self.find_element(RegionalSettingsPageLocator.LOCATOR_REGIONAL_SETTINGS_TEXT).text
        check_text = "Regional Settings"
        assert regional_settings_text == check_text, f'Text on UI {regional_settings_text} is not eq {check_text}'

    def select_currency(self):
        regional_change_button = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_CURRENCY_SELECT_BUTTON
        )
        regional_change_button.click()

    def select_country(self):
        country_change_button = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_COUNTRY_SELECT_BUTTON
        )
        country_change_button.click()

    def check_country(self, country):
        country_text = self.find_element(RegionalSettingsPageLocator.LOCATOR_COUNTRY_SELECT_BUTTON).text
        assert country_text == country, f'Country on regional setting page {country_text} is not eq {country}'

    def should_be_currency(self):
        currency_text = self.find_element(RegionalSettingsPageLocator.LOCATOR_CURRENCY_SELECT_BUTTON).text
        check_text = "US Dollars"
        assert currency_text == check_text, f'Text on UI {currency_text} is not eq {check_text}'
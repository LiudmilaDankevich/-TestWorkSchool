from pages.base_page import BasePage
from pages.main_page import MainPage
from locator.regional_settings_page_locator import RegionalSettingsPageLocator


class RegionalSettingsPage(BasePage):


    def should_be_regional_settings_page(self):

        regional_settings_text = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_REGIONAL_SETTINGS_TEXT
        ).text
        check_text = "Regional Settings"
        assert regional_settings_text == check_text, f'Text on UI {regional_settings_text} ' \
                                                     f'is not eq {check_text}'
    def select_language(self):
        language_change_button = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_LANGUAGE_SELECT_BUTTON
        )
        language_change_button.click()

    def should_be_language(self):
        language_text = self.find_element(RegionalSettingsPageLocator.LOCATOR_LANGUAGE_SELECT_BUTTON).text
        check_text = "English"
        assert language_text == check_text, f'Text on UI {language_text} is not eq {check_text}'

    def select_currency(self):
        regional_change_button = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_CURRENCY_SELECT_BUTTON
        )
        regional_change_button.click()

    def should_be_currency(self):
        currency_text = self.find_element(RegionalSettingsPageLocator.LOCATOR_CURRENCY_SELECT_BUTTON).text
        check_text = "US Dollars"
        assert currency_text == check_text, f'Text on UI {currency_text} is not eq {check_text}'

    def select_country(self):
        country_change_button = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_COUNTRY_SELECT_BUTTON
        )
        country_change_button.click()

    def should_be_country(self):
        country_text = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_COUNTRY_SELECT_BUTTON
        ).text
        check_text = "Belarus"
        assert country_text == check_text, f'Text on UI {country_text} is not eq {check_text}'

    def select_zone_code(self):
        zone_code_change_button = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_ZONE_CODE_BUTTON
        )
        zone_code_change_button.click()

    def should_be_zone_code(self):
        zone_code_text = self.find_element(RegionalSettingsPageLocator.LOCATOR_ZONE_CODE_BUTTON).text
        check_text = ''
        assert zone_code_text == check_text, f'Text on UI {zone_code_text} is not eq {check_text}'

    def select_display_prices_including_tax(self):
        display_prices_including_tax_radio_button = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_DISPLAY_PRICES_INCLUDING_TAX)
        display_prices_including_tax_radio_button.click()

    def select_display_prices_excluding_tax(self):
        display_prices_excluding_tax_radio_button = self.find_element(
            RegionalSettingsPageLocator.LOCATOR_DISPLAY_PRICES_EXCLUDING_TAX)
        display_prices_excluding_tax_radio_button.click()

    def click_save_button(self):
        save_button = self.find_element(RegionalSettingsPageLocator.LOCATOR_SAVE_BUTTON)
        save_button.click()


from pages.main_page import MainPage
from pages.app_menu_page import RegionalSettingsPage
from time import sleep


def test_click_regional_change_button(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.open_regional_page()
    regional_settings_page = RegionalSettingsPage(browser)
    regional_settings_page.should_be_regional_settings_page()
    regional_settings_page.select_currency()
    regional_settings_page.should_be_currency()
    regional_settings_page.select_country()
    regional_settings_page.should_be_country()
    regional_settings_page.select_language()
    regional_settings_page.should_be_language()
    regional_settings_page.select_zone_code()
    regional_settings_page.should_be_zone_code()
    regional_settings_page.select_display_prices_including_tax()
    regional_settings_page.select_display_prices_excluding_tax()
    regional_settings_page.click_save_button()






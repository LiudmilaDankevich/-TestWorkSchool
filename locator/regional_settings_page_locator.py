from selenium.webdriver.common.by import By



class RegionalSettingsPageLocator:

    LOCATOR_REGIONAL_SETTINGS_TEXT = (By.LINK_TEXT, 'Regional Settings')
    LOCATOR_CURRENCY_SELECT_BUTTON = (By.XPATH, '// *[ @ id = "box-regional-settings"] '
                                                '/ div / form / table / tbody / tr[1] / td[2] / '
                                                'select / option[2]')
    LOCATOR_COUNTRY_SELECT_BUTTON  = (By.XPATH, '//select[@name="country_code"]//option[@value="BY"]')
    LOCATOR_LANGUAGE_SELECT_BUTTON = (By.XPATH, '//select[@name="language_code"]//option[@value="en"]')
    LOCATOR_ZONE_CODE_BUTTON = (By.XPATH, '//*[@id="box-regional-settings"]'
                                          '/div/form/table/tbody/tr[2]/td[2]/select')
    LOCATOR_DISPLAY_PRICES_INCLUDING_TAX = (
        By.XPATH, '//input[@type="radio"][@name="display_prices_including_tax"][@value="1"]')
    LOCATOR_DISPLAY_PRICES_EXCLUDING_TAX = (
        By.XPATH,'//input[@type="radio"][@name="display_prices_including_tax"][@value="0"]')
    LOCATOR_SAVE_BUTTON = (By.XPATH, '// button[@type="submit"][@name="save"][@value ="Save"]')

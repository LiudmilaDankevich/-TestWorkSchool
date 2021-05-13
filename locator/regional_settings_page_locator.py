from selenium.webdriver.common.by import By



class RegionalSettingsPageLocator:

    LOCATOR_REGIONAL_SETTINGS_TEXT = (By.LINK_TEXT, 'Regional Settings')
    LOCATOR_CURRENCY_SELECT_BUTTON = (By.XPATH, '//select[@name="currency_code"]//option[@value="USD"]')
    LOCATOR_COUNTRY_SELECT_BUTTON  = (By.XPATH, '//select[@name="country_code"]//option[@value="BY"]')
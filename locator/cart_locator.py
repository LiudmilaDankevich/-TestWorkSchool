from selenium.webdriver.common.by import By


class CartPageLocator:

    LOCATOR_QUANTITY_CHECK = (By.XPATH, '//td[@style="text-align: center;"]')
    LOCATOR_COST_CHECK = (By.CLASS_NAME, 'unit-cost')
    LOCATOR_BUTTON_ORDER = (By.XPATH, '//button[@value="Confirm Order"]')




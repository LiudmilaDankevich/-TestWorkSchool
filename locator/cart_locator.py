from selenium.webdriver.common.by import By


class CartPageLocator:
    LOCATOR_CURT_BUTTON = (
        By.XPATH, 'Cart:')
    LOCATOR_QUANTITY_CHECK = (By.XPATH, '//input[@name="quantity"]')
    LOCATOR_SUM_CHECK = (By.XPATH, '43.56 €')




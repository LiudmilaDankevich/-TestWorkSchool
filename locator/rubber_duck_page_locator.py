from selenium.webdriver.common.by import By


class RubberDuckPageLocator:
    LOCATOR_DUCK_CLICK = (
        By.XPATH, '//li[@class="product column shadow hover-light"]/a[@class="link"]//img[@alt="Blue Duck"]')
    LOCATOR_QUANTITY_DUCK_FIELD = (By.XPATH, '//input[@name="quantity"]')
    LOCATOR_ADD_TO_CART_BUTTON = (By.XPATH, '//button[@name="add_cart_product"]')
    LOCATOR_CURT_BUTTON = (By.LINK_TEXT, 'Checkout »')

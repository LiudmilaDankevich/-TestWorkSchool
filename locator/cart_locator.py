from selenium.webdriver.common.by import By


class CartPageLocator:

    LOCATOR_DUCK_CLICK = (By.XPATH, '//li[@class="product column shadow hover-light"]/a[@class="link"]//img[@alt="Blue Duck"]')
    LOCATOR_CHOICE_OF_COLLIDING = (By.XPATH, '//input[@name="quantity"][@step="1"]')
    LOCATOR_SING_IN_BUTTON = (By.XPATH, '//button[@name="add_cart_product"]')


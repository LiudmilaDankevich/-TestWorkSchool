from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_EMAIL_FIELD = (By.XPATH, '//input[@type="text"]')
    LOCATOR_PASSWD_FIELD = (By.XPATH, '//input[@type="password"]')
    LOCATOR_REMEMBER_ME = (By.XPATH, '// input[ @ name = "remember_me"]')
    LOCATOR_SING_IN_BUTTON = (By.XPATH, '//button[@name="login"]')

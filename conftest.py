from selenium import webdriver
import pytest
import json
import os.path

def load_config(file_path):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    with open(config_path) as f:
        target = json.load(f)
    return



@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('http://localhost/litecart/en/')
    yield driver
    driver.quit()


@pytest.fixture()
def user_config_data():
    config_data = load_config("recources/variables/user_data.json")
    return config_data['email'], config_data['passwd']


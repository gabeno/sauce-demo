import pytest
from selenium.webdriver.common.by import By

TEST_URL = "https://www.saucedemo.com/"

def test_landing_page_is_loaded(driver):
    driver.get(TEST_URL)
    assert "Swag Labs" == driver.title

import enum

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

WEB_DRIVER_WAIT_SEC = 2
PAGE_URL = "https://www.saucedemo.com/"


@enum.unique
class ErrorType(enum.Enum):
    USERNAME_AND_PASSWORD_ERROR = "Epic sadface: Username and password do not match any user in this service"
    USERNAME_ERROR = "Epic sadface: Username is required"
    PASSWORD_ERROR = "Epic sadface: Password is required"
    LOCKED_OUT_ERROR = "Epic sadface: Sorry, this user has been locked out."


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, name, by_type):
        LOCATORS = {"id": By.ID, "xpath": By.XPATH, "classname": By.CLASS_NAME}
        try:
            el = WebDriverWait(self.driver, WEB_DRIVER_WAIT_SEC).until(
                EC.presence_of_element_located((LOCATORS[by_type], name))
            )
        except (
            StaleElementReferenceException,
            NoSuchElementException,
            TimeoutException,
        ) as e:
            raise Exception(
                f"An exception of type {type(e).__name__} occurred."
            )
        return el

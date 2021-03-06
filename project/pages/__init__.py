import enum
from collections import namedtuple

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

WEB_DRIVER_WAIT_SEC = 3
PAGE_URL = "https://www.saucedemo.com/"
INVENTORY_ITEM_NAMES = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
]


@enum.unique
class LoginFormError(enum.Enum):
    USERNAME_AND_PASSWORD_ERROR = "Epic sadface: Username and password do not match any user in this service"
    USERNAME_ERROR = "Epic sadface: Username is required"
    PASSWORD_ERROR = "Epic sadface: Password is required"
    LOCKED_OUT_ERROR = "Epic sadface: Sorry, this user has been locked out."


@enum.unique
class CheckoutUserInfoFormError(enum.Enum):
    FIRST_NAME_ERROR = "Error: First Name is required"
    LAST_NAME_ERROR = "Error: Last Name is required"
    POSTAL_CODE_ERROR = "Error: Postal Code is required"


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, name, by_type="xpath", condition="present"):
        LOCATORS = {"id": By.ID, "xpath": By.XPATH}
        EXPECTED_CONDITIONS = {
            "present": EC.presence_of_element_located,
            "clickable": EC.element_to_be_clickable,
        }
        try:
            el = WebDriverWait(self.driver, WEB_DRIVER_WAIT_SEC).until(
                EXPECTED_CONDITIONS[condition]((LOCATORS[by_type], name))
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

    def get_field(self, _id):
        return self.get_element(name=_id, by_type="id")

    def set_field(self, _id, value):
        self.get_field(_id).send_keys(value)

    def make_inventory_list(self, items):
        Item = namedtuple("Item", ["name", "price", "quantity"])
        cart_items = []

        for item in items:
            # find_elements_by_class returns a list
            name = item.find_elements_by_class_name("inventory_item_name")[
                0
            ].text
            # slice string to remove dollar sign: "$7.77" -> "7.77"
            price = float(
                item.find_elements_by_class_name("inventory_item_price")[
                    0
                ].text[1:]
            )
            try:
                # quantity does not exist in the inventory page
                quantity = int(
                    item.find_elements_by_class_name("cart_quantity")[0].text
                )
            except Exception:
                quantity = 0
            cart_items.append(Item(name, price, quantity))

        return cart_items

    def get_title(self):
        return self.get_element(name="//span[@class='title']").text

    def get_button(self, name, selector_type="id", tag="button"):
        return self.get_element(name=f"//{tag}[@{selector_type}='{name}']")

    def get_link(self, name, selector_type="id", tag="a"):
        return self.get_element(
            name=f"//{tag}[@{selector_type}='{name}']",
            condition="clickable",
        )

    def get_error_message(self):
        return self.get_element(name="//h3").text

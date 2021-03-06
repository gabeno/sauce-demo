import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from project.pages import User
from project.pages.page_cart import CartPage
from project.pages.page_checkout_complete import CheckoutCompletePage
from project.pages.page_checkout_confirmation import CheckoutConfirmationPage
from project.pages.page_checkout_information import CheckoutInformationPage
from project.pages.page_inventory import InventoryPage
from project.pages.page_login import LoginPage

REMOTE_URL = "http://selenium-hub:4444"


def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="Provide browser type",
    )


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    driver = request.config.getoption("--driver")
    supported_browsers = ("chrome", "firefox", "edge")
    if driver.lower() not in supported_browsers:
        print(f"Support browsers are: {supported_browsers}")
    if driver == "chrome":
        conn = webdriver.Remote(
            command_executor=REMOTE_URL,
            desired_capabilities=DesiredCapabilities.CHROME.copy(),
        )
    elif driver == "firefox":
        conn = webdriver.Remote(
            command_executor=REMOTE_URL,
            desired_capabilities=DesiredCapabilities.FIREFOX.copy(),
        )
    elif driver == "edge":
        capabilities = DesiredCapabilities.EDGE.copy()
        capabilities["platform"] = "LINUX"
        conn = webdriver.Remote(
            command_executor=REMOTE_URL,
            desired_capabilities=capabilities,
        )
    yield conn
    conn.quit()


user = User("standard_user", "secret_sauce")


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver, user)


@pytest.fixture(scope="function")
def inventory_page(driver):
    page = InventoryPage(driver, user)
    yield page
    page.reset_app_state()


@pytest.fixture(scope="function")
def inventory_page_without_reset(driver):
    yield InventoryPage(driver, user)


@pytest.fixture(scope="function")
def cart_page(driver):
    yield CartPage(driver, user)


@pytest.fixture(scope="function")
def checkout_information_page(driver):
    yield CheckoutInformationPage(driver, user)


@pytest.fixture(scope="function")
def checkout_confirmation_page(driver):
    yield CheckoutConfirmationPage(driver, user)


@pytest.fixture(scope="function")
def checkout_complete_page(driver):
    yield CheckoutCompletePage(driver, user)

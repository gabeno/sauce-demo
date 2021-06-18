import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def inventory_page(driver):
    page = InventoryPage(driver)
    yield page
    # guard against breaking test__logout_from_inventory_page__ok test
    if page.is_logged_in():
        page.reset_app_state()
        # XXX occassionally ElementClickInterceptedException is observed so we
        # introduce 50ms delay before logout is clicked
        sleep(0.05)
        page.logout()


@pytest.fixture(scope="function")
def cart_page(driver):
    page = CartPage(driver)
    return page


@pytest.fixture(scope="function")
def checkout_information_page(driver):
    page = CheckoutInformationPage(driver)
    return page


@pytest.fixture(scope="function")
def checkout_confirmation_page(driver):
    page = CheckoutConfirmationPage(driver)
    return page


@pytest.fixture(scope="function")
def checkout_complete_page(driver):
    page = CheckoutCompletePage(driver)
    return page

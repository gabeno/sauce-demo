import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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
    login_page = LoginPage(driver)
    return login_page

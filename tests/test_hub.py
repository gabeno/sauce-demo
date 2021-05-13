from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444'
)

print(driver)


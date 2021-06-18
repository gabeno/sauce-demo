from project.pages import PAGE_URL, Page


class LoginPage(Page):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver.get(PAGE_URL)

    def get_login_page_logo(self):
        login_logo_container = self.get_element(
            name="login_logo", by_type="classname"
        )
        return login_logo_container.size != 0

    def get_error_button(self):
        return self.get_button_by_class("error-button")

    def get_error_message(self):
        return self.get_element(name="//h3", by_type="xpath").text

    def set_username(self, username):
        self.set_field("user-name", username)

    def set_password(self, password):
        self.set_field("password", password)

    def click_login_button(self):
        login_button = self.get_element(name="login-button", by_type="id")
        login_button.click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def click_error_button(self):
        self.get_error_button().click()

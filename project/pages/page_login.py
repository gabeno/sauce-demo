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

    def set_username(self, username):
        username_field = self.get_element(name="user-name", by_type="id")
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.get_element(name="password", by_type="id")
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.get_element(name="login-button", by_type="id")
        login_button.click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def get_error_message(self):
        return self.get_element(name="//h3", by_type="xpath").text

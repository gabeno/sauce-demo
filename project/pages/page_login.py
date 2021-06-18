from project.pages import PAGE_URL, Page


class LoginPage(Page):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver.get(PAGE_URL)

    def set_username(self, username):
        self.set_field("user-name", username)

    def set_password(self, password):
        self.set_field("password", password)

    def click_login_button(self):
        self.get_button("login-button", tag="input").click()

    def click_error_button(self):
        self.get_button("error-button", selector_type="class").click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

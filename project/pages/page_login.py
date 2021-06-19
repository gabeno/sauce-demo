from project.pages import PAGE_URL, Page


class LoginPage(Page):
    def __init__(self, driver, user):
        super(LoginPage, self).__init__(driver)
        self.driver.get(PAGE_URL)
        self.user = user
        self.login()

    def is_login_page(self):
        try:
            self.get_element("//div[@id='login_button_container']")
            return True
        except Exception:
            return False

    def set_username(self):
        self.set_field("user-name", self.user.username)

    def set_password(self):
        self.set_field("password", self.user.password)

    def click_login_button(self):
        self.get_button("login-button", tag="input").click()

    def click_error_button(self):
        self.get_button("error-button", selector_type="class").click()

    def login(self):
        self.set_username()
        self.set_password()
        self.click_login_button()

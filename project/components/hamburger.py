from project.pages.page_login import LoginPage


class HamburgerComponent(LoginPage):
    def __init__(self, driver, user):
        super(HamburgerComponent, self).__init__(driver, user)

    def get_burger_menu_open_button(self):
        return self.get_button("react-burger-menu-btn")

    def get_burger_menu_close_button(self):
        return self.get_button("react-burger-cross-btn")

    def click_burger_menu_open_button(self):
        self.get_burger_menu_open_button().click()

    def click_burger_menu_close_button(self):
        self.get_burger_menu_close_button().click()

    def click_reset_app_link(self):
        self.get_link("reset_sidebar_link").click()

    def click_logout_link(self):
        self.get_link("logout_sidebar_link").click()

    def reset_app_state(self):
        self.click_burger_menu_open_button()
        self.click_reset_app_link()
        self.click_burger_menu_close_button()

    def logout(self):
        self.click_burger_menu_open_button()
        self.click_logout_link()

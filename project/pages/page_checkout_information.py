from project.components.hamburger import HamburgerComponent


class CheckoutInformationPage(HamburgerComponent):
    def __init__(self, driver, user):
        super(CheckoutInformationPage, self).__init__(driver, user)

    @property
    def title(self):
        return self.get_title()

    def set_first_name(self, value):
        self.set_field("first-name", value)

    def set_last_name(self, value):
        self.set_field("last-name", value)

    def set_postal_code(self, value):
        self.set_field("postal-code", value)

    def set_user_information(self, first_name, last_name, postal_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_postal_code(postal_code)

    def click_continue_button(self):
        self.get_button("continue", tag="input").click()

    def click_clear_error_button(self):
        self.get_button("error-button", selector_type="class").click()

    def click_cancel_button(self):
        self.get_button("cancel").click()

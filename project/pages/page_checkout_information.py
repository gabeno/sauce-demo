from project.pages.page_login import LoginPage


class CheckoutInformationPage(LoginPage):
    def __init__(self, driver):
        super(CheckoutInformationPage, self).__init__(driver)

    @property
    def title(self):
        return self.get_title()

    def set_first_name(self, value):
        self.set_field("first-name", value)

    def set_last_name(self, value):
        self.set_field("last-name", value)

    def set_postal_code(self, value):
        self.set_field("postal-code", value)

    def get_error_message(self):
        return self.get_element(name="//h3", by_type="xpath").text

    def get_continue_button(self):
        return self.get_element(
            name="//input[@id='continue']",
            by_type="xpath",
            condition="clickable",
        )

    def set_user_information(self, first_name, last_name, postal_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_postal_code(postal_code)

    def click_continue_button(self):
        self.get_continue_button().click()

from project.pages.page_login import LoginPage


class CheckoutConfirmationPage(LoginPage):
    def __init__(self, driver):
        super(CheckoutConfirmationPage, self).__init__(driver)

    @property
    def title(self):
        return self.get_title()

    def get_finish_button(self):
        return self.get_button_by_id("finish")

    def get_cancel_button(self):
        return self.get_button_by_id("cancel")

    def click_finish_button(self):
        self.get_finish_button().click()

from project.pages.page_login import LoginPage


class CheckoutCompletePage(LoginPage):
    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver)

    @property
    def title(self):
        return self.get_title()

    def get_back_button(self):
        return self.get_button_by_id("back-to-products")

    def click_back_button(self):
        self.get_back_button().click()

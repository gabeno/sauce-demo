from project.pages.page_login import LoginPage


class CheckoutCompletePage(LoginPage):
    # def __init__(self, driver, user):
    #    super(CheckoutCompletePage, self).__init__(driver, user)

    @property
    def title(self):
        return self.get_title()

    def click_back_button(self):
        self.get_button("back-to-products").click()

from project.components.hamburger import HamburgerComponent


class CheckoutConfirmationPage(HamburgerComponent):
    def __init__(self, driver, user):
        super(CheckoutConfirmationPage, self).__init__(driver, user)

    @property
    def title(self):
        return self.get_title()

    def click_cancel_button(self):
        self.get_button("cancel").click()

    def click_finish_button(self):
        self.get_button("finish").click()

    def click_cancel_button(self):
        self.get_button("cancel").click()

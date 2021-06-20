from project.components.hamburger import HamburgerComponent


class CheckoutCompletePage(HamburgerComponent):
    def __init__(self, driver, user):
       super(CheckoutCompletePage, self).__init__(driver, user)

    @property
    def title(self):
        return self.get_title()

    def click_back_button(self):
        self.get_button("back-to-products").click()

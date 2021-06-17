from project.pages.page_login import LoginPage


class CheckoutCompletePage(LoginPage):
    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver)

    @property
    def title(self):
        return self.get_title()

    def get_back_button(self):
        return self.get_element(
            name="//button[@id='back-to-products']",
            by_type="xpath",
            condition="clickable",
        )

    def click_back_button(self):
        self.get_back_button().click()

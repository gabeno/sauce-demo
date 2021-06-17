from project.pages.page_login import LoginPage


class CheckoutConfirmationPage(LoginPage):
    def __init__(self, driver):
        super(CheckoutConfirmationPage, self).__init__(driver)

    def get_title(self):
        return self.get_element(
            name="//span[@class='title']", by_type="xpath"
        ).text

    def get_finish_button(self):
        return self.get_element(
            name="//button[@id='finish']",
            by_type="xpath",
            condition="clickable",
        )

    def get_cancel_button(self):
        return self.get_element(
            name="//button[@id='cancel']",
            by_type="xpath",
            condition="clickable",
        )

    def click_finish_button(self):
        self.get_finish_button().click()

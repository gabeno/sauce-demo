from project.pages.page_login import LoginPage
from project.pages.utils import make_id_from_name


class CartPage(LoginPage):
    def __init__(self, driver):
        super(CartPage, self).__init__(driver)
        self.login("standard_user", "secret_sauce")

    @property
    def title(self):
        return self.get_title()

    def get_cart_link(self):
        return self.get_element(
            name="//div[@id='shopping_cart_link']", by_type="xpath"
        )

    def get_checkout_button(self):
        return self.get_button_by_id("checkout")

    def get_cart_items(self):
        parent = self.get_element(
            name="//*[@class='cart_list']", by_type="xpath"
        )
        cart_items = parent.find_elements_by_class_name("cart_item")
        return self.make_inventory_list(cart_items)

    def click_cart_link(self):
        cart_link = self.get_cart_link()
        cart_link.click()

    def click_remove_item_button(self, item_name):
        item_name = make_id_from_name(item_name)
        item_id = f"remove-{item_name}"
        remove_item_button = self.get_button_by_id(item_id)
        remove_item_button.click()

    def click_checkout_button(self):
        button = self.get_checkout_button()
        button.click()

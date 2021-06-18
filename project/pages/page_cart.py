from project.pages.page_login import LoginPage
from project.pages.utils import make_id_from_name


class CartPage(LoginPage):
    def __init__(self, driver):
        super(CartPage, self).__init__(driver)
        self.login("standard_user", "secret_sauce")

    @property
    def title(self):
        return self.get_title()

    def get_checkout_button(self):
        return self.get_button("checkout")

    def get_cart_items(self):
        parent = self.get_element(
            name="//*[@class='cart_list']", by_type="xpath"
        )
        cart_items = parent.find_elements_by_class_name("cart_item")
        return self.make_inventory_list(cart_items)

    def click_cart_link(self):
        self.get_link("shopping_cart_link", tag="div").click()

    def click_remove_item_button(self, item_name):
        item_name = make_id_from_name(item_name)
        item_id = f"remove-{item_name}"
        self.get_button(item_id).click()

    def click_checkout_button(self):
        self.get_checkout_button().click()

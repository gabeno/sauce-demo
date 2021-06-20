from project.components.hamburger import HamburgerComponent
from project.pages.utils import make_id_from_name


class CartPage(HamburgerComponent):
    def __init__(self, driver, user):
        super(CartPage, self).__init__(driver, user)

    @property
    def title(self):
        return self.get_title()

    def get_cart_items(self):
        parent = self.get_element(name="//*[@class='cart_list']")
        cart_items = parent.find_elements_by_class_name("cart_item")
        return self.make_inventory_list(cart_items)

    def click_cart_link(self):
        self.get_link("shopping_cart_link", tag="div").click()

    def click_remove_item_button(self, item_name):
        item_name = make_id_from_name(item_name)
        item_id = f"remove-{item_name}"
        self.get_button(item_id).click()

    def click_checkout_button(self):
        self.get_button("checkout").click()

    def click_continue_shopping_button(self):
        self.get_button("continue-shopping").click()

import enum

from project.pages import Page
from project.pages.page_login import LoginPage
from project.pages.utils import make_id_from_name


@enum.unique
class SortOption(enum.Enum):
    NAME_A_TO_Z = "az"
    NAME_Z_TO_A = "za"
    PRICE_LOW_TO_HIGH = "lohi"
    PRICE_HIGH_TO_LOW = "hilo"

    @property
    def to_classname(self):
        _map = {
            "NAME_A_TO_Z": "name",
            "NAME_Z_TO_A": "name",
            "PRICE_LOW_TO_HIGH": "price",
            "PRICE_HIGH_TO_LOW": "price",
        }
        return _map[self.name]


class MenuComponent(LoginPage):
    def __init__(self, driver, user):
        super(MenuComponent, self).__init__(driver, user)

    def get_burger_menu_open_button(self):
        return self.get_button("react-burger-menu-btn")

    def get_burger_menu_close_button(self):
        return self.get_button("react-burger-cross-btn")

    def click_burger_menu_open_button(self):
        self.get_burger_menu_open_button().click()

    def click_burger_menu_close_button(self):
        self.get_burger_menu_close_button().click()

    def click_reset_app_link(self):
        self.get_link("reset_sidebar_link").click()

    def click_logout_link(self):
        self.get_link("logout_sidebar_link").click()

    def reset_app_state(self):
        self.click_burger_menu_open_button()
        self.click_reset_app_link()
        self.click_burger_menu_close_button()

    def logout(self):
        self.click_burger_menu_open_button()
        self.click_logout_link()


class InventoryPage(MenuComponent):
    def __init__(self, driver, user):
        super(InventoryPage, self).__init__(driver, user)

    @property
    def title(self):
        return self.get_title()

    def is_logged_in(self):
        try:
            self.get_title()
            return True
        except Exception:
            return False

    def has_items_in_cart(self):
        try:
            self.get_cart_items_count()
            return True
        except Exception:
            return False

    def get_cart_items_count(self):
        return self.get_element(
            name="//span[@class='shopping_cart_badge']"
        ).text

    def get_sort_option(self, option):
        return self.get_element(
            name=f"//select[@class='product_sort_container']/option[@value='{option.value}']",
        )

    def get_inventory_list(self, option=SortOption.NAME_A_TO_Z):
        """Get list of inventory items as per filter selection"""
        parent = self.get_element(name="//*[@class='inventory_list']")
        products = parent.find_elements_by_class_name("inventory_item")
        return self.make_inventory_list(products)

    def click_cart_link(self):
        self.get_link("shopping_cart_link", selector_type="class").click()

    def click_add_item_button(self, item_name):
        item_name = make_id_from_name(item_name)
        item_id = f"add-to-cart-{item_name}"
        self.get_button(item_id).click()

    def click_remove_item_button(self, item_name):
        item_name = make_id_from_name(item_name)
        item_id = f"remove-{item_name}"
        self.get_button(item_id).click()

    def click_sort_option(self, option):
        self.get_sort_option(option).click()

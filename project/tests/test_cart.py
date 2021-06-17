import pytest

from project.pages import INVENTORY_ITEM_NAMES


@pytest.mark.parametrize(
    "inventory_list, count, products",
    [
        ([], 0, []),  # zero item
        (["Sauce Labs Onesie"], 1, ["Sauce Labs Onesie"]),  # one item
        (
            [
                "Sauce Labs Onesie",
                "Sauce Labs Backpack",
                "Test.allTheThings() T-Shirt (Red)",
            ],
            3,
            [
                "Sauce Labs Onesie",
                "Sauce Labs Backpack",
                "Test.allTheThings() T-Shirt (Red)",
            ],
        ),  # multiple items
    ],
)
def test__add_items_to_cart__items_exist_in_cart(
    inventory_page, cart_page, inventory_list, count, products
):
    [inventory_page.click_add_item_button(item) for item in inventory_list]
    inventory_page.click_cart_link()
    cart_items = cart_page.get_cart_items()
    assert cart_page.title == "YOUR CART"
    assert len(cart_items) == count
    assert sorted([item.name for item in cart_items]) == sorted(products)


@pytest.mark.parametrize(
    "inventory_list, items_to_remove, before_count, after_count",
    [
        (
            [
                "Sauce Labs Onesie",
                "Sauce Labs Backpack",
                "Test.allTheThings() T-Shirt (Red)",
            ],
            [
                "Sauce Labs Onesie",
            ],
            3,
            2,
        ),
        (
            [
                "Sauce Labs Onesie",
                "Sauce Labs Backpack",
                "Test.allTheThings() T-Shirt (Red)",
            ],
            [
                "Sauce Labs Onesie",
                "Sauce Labs Backpack",
            ],
            3,
            1,
        ),
        (
            [
                "Sauce Labs Onesie",
                "Sauce Labs Backpack",
                "Test.allTheThings() T-Shirt (Red)",
            ],
            [
                "Sauce Labs Onesie",
                "Sauce Labs Backpack",
                "Test.allTheThings() T-Shirt (Red)",
            ],
            3,
            0,
        ),
    ],
)
def test__remove_items_from_cart__cart_items_count_ok(
    inventory_page,
    cart_page,
    inventory_list,
    items_to_remove,
    before_count,
    after_count,
):
    [inventory_page.click_add_item_button(item) for item in inventory_list]
    inventory_page.click_cart_link()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == before_count
    [cart_page.click_remove_item_button(item) for item in items_to_remove]
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == after_count

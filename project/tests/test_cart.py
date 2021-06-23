import pytest

from project.pages import INVENTORY_ITEM_NAMES


@pytest.mark.parametrize(
    "items_to_add",
    [
        ([]),
        (["Sauce Labs Onesie"]),
        (
            [
                "Sauce Labs Onesie",
                "Sauce Labs Backpack",
                "Test.allTheThings() T-Shirt (Red)",
            ]
        ),
    ],
)
def test__add_items_to_cart__items_exist_in_cart(
    inventory_page,
    cart_page,
    items_to_add,
):
    [inventory_page.click_add_item_button(item) for item in items_to_add]
    inventory_page.click_cart_link()
    assert cart_page.title == "YOUR CART"
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == len(items_to_add)
    assert sorted([item.name for item in cart_items]) == sorted(items_to_add)
    [cart_page.click_remove_item_button(item) for item in items_to_add]


@pytest.mark.parametrize(
    "inventory_list, items_to_remove",
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
        ),
    ],
)
def test__remove_items_from_cart__cart_items_count_ok(
    inventory_page,
    cart_page,
    inventory_list,
    items_to_remove,
):
    [inventory_page.click_add_item_button(item) for item in inventory_list]
    inventory_page.click_cart_link()
    cart_items = cart_page.get_cart_items()
    count_before = len(cart_items)
    [cart_page.click_remove_item_button(item) for item in items_to_remove]
    count_after = len(cart_page.get_cart_items())
    assert count_before == count_after + len(items_to_remove)


def test__navigate_back_to_inventory_page__ok(
    inventory_page,
    cart_page,
):
    inventory_page.click_add_item_button(INVENTORY_ITEM_NAMES[0])
    inventory_page.click_cart_link()
    # no exception raised
    cart_page.click_continue_shopping_button()
    assert inventory_page.get_cart_items_count() == "1"

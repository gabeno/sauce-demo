from operator import attrgetter

import pytest

from project.pages import INVENTORY_ITEM_NAMES
from project.pages.page_inventory import SortOption


def test__page_loaded_after_login__ok(inventory_page):
    assert inventory_page.get_title() == "PRODUCTS"


def test__logout_from_inventory_page__ok(inventory_page):
    assert inventory_page.is_logged_in() is True
    inventory_page.logout()
    assert inventory_page.is_logged_in() is False


def test__initial_page_load__no_items_in_cart(inventory_page):
    assert inventory_page.has_items_in_cart() is False


@pytest.mark.parametrize(
    "item_name",
    INVENTORY_ITEM_NAMES,
)
def test__add_items_to_cart__ok(inventory_page, item_name):
    inventory_page.click_add_item_button(item_name)
    assert inventory_page.get_cart_items_count() == "1"


@pytest.mark.parametrize(
    "item_name",
    INVENTORY_ITEM_NAMES,
)
def test__remove_items_from_cart__ok(inventory_page, item_name):
    inventory_page.click_add_item_button(item_name)
    inventory_page.click_remove_item_button(item_name)
    assert inventory_page.has_items_in_cart() is False


def test__add_multiple_items_to_cart__ok(inventory_page):
    for item in INVENTORY_ITEM_NAMES:
        inventory_page.click_add_item_button(item)
    assert inventory_page.get_cart_items_count() == str(
        len(INVENTORY_ITEM_NAMES)
    )


def test__sort_by_name_a_to_z__ok(inventory_page):
    option = SortOption.NAME_A_TO_Z
    list_before_sort = inventory_page.get_inventory_list()
    inventory_page.click_sort_option(option)
    list_after_sort = inventory_page.get_inventory_list(option)
    assert list_before_sort == list_after_sort


def test__sort_by_name_z_to_a__ok(inventory_page):
    option = SortOption.NAME_Z_TO_A
    list_before_sort = inventory_page.get_inventory_list()
    inventory_page.click_sort_option(option)
    list_after_sort = inventory_page.get_inventory_list(option)
    assert (
        sorted(list_before_sort, key=attrgetter("name"), reverse=True)
        == list_after_sort
    )


def test__sort_by_price_lo_to_hi__ok(inventory_page):
    option = SortOption.PRICE_LOW_TO_HIGH
    list_before_sort = inventory_page.get_inventory_list()
    inventory_page.click_sort_option(option)
    list_after_sort = inventory_page.get_inventory_list(option)
    assert sorted(list_before_sort, key=attrgetter("price")) == list_after_sort


def test__sort_by_price_hi_to_lo__ok(inventory_page):
    option = SortOption.PRICE_HIGH_TO_LOW
    list_before_sort = inventory_page.get_inventory_list()
    inventory_page.click_sort_option(option)
    list_after_sort = inventory_page.get_inventory_list(option)
    assert (
        sorted(list_before_sort, key=attrgetter("price"), reverse=True)
        == list_after_sort
    )
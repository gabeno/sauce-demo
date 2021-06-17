from project.pages import INVENTORY_ITEM_NAMES


def test__checkout_confirmation__ok(
    checkout_information_page,
    checkout_confirmation_page,
    inventory_page,
    cart_page,
):
    inventory_page.click_add_item_button(INVENTORY_ITEM_NAMES[0])
    inventory_page.click_cart_link()
    cart_page.click_checkout_button()
    checkout_information_page.set_user_information("a", "b", "0")
    checkout_information_page.click_continue_button()
    assert checkout_confirmation_page.title == "CHECKOUT: OVERVIEW"

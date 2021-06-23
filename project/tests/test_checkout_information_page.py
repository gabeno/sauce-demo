import pytest

from project.pages import INVENTORY_ITEM_NAMES, CheckoutUserInfoFormError


@pytest.mark.parametrize(
    "first_name,last_name,postal_code,error_message",
    [
        ("", "", "", CheckoutUserInfoFormError.FIRST_NAME_ERROR.value),
        ("a", "", "", CheckoutUserInfoFormError.LAST_NAME_ERROR.value),
        ("", "b", "", CheckoutUserInfoFormError.FIRST_NAME_ERROR.value),
        ("", "", "0", CheckoutUserInfoFormError.FIRST_NAME_ERROR.value),
        ("a", "b", "", CheckoutUserInfoFormError.POSTAL_CODE_ERROR.value),
        ("a", "", "0", CheckoutUserInfoFormError.LAST_NAME_ERROR.value),
        ("", "b", "0", CheckoutUserInfoFormError.FIRST_NAME_ERROR.value),
    ],
)
def test__checkout_invalid_credentials__error_message_shown(
    checkout_information_page,
    inventory_page,
    cart_page,
    first_name,
    last_name,
    postal_code,
    error_message,
):
    inventory_page.click_add_item_button(INVENTORY_ITEM_NAMES[0])
    inventory_page.click_cart_link()
    cart_page.click_checkout_button()

    assert checkout_information_page.title == "CHECKOUT: YOUR INFORMATION"

    checkout_information_page.set_user_information(
        first_name, last_name, postal_code
    )
    checkout_information_page.click_continue_button()

    assert checkout_information_page.get_error_message() == error_message

    checkout_information_page.click_clear_error_button()


def test__checkout_valid_credentials__no_error_message_shown(
    checkout_information_page, inventory_page, cart_page
):
    with pytest.raises(Exception):
        inventory_page.click_add_item_button(INVENTORY_ITEM_NAMES[0])
        inventory_page.click_cart_link()
        cart_page.click_checkout_button()
        checkout_information_page.set_user_information("a", "b", "0")
        checkout_information_page.click_continue_button()
        checkout_information_page.get_error_message()


def test__navigate_back_to_cart__ok(
    checkout_information_page, inventory_page, cart_page
):
    inventory_page.click_add_item_button(INVENTORY_ITEM_NAMES[0])
    inventory_page.click_cart_link()
    cart_page.click_checkout_button()
    checkout_information_page.title == "CHECKOUT: YOUR INFORMATION"
    # no exception raised
    checkout_information_page.click_cancel_button()

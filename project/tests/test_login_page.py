import pytest

from project.pages import ErrorType


def test__login_page_logo_exists__ok(login_page):
    assert login_page.get_login_page_logo() is True


@pytest.mark.parametrize(
    "username,password,error_message",
    [
        (
            "fake_username",
            "fake_password",
            ErrorType.USERNAME_AND_PASSWORD_ERROR.value,
        ),
    ],
)
def test__login_with_improper_credentials__login_error_shown(
    login_page, username, password, error_message
):
    login_page.login(username, password)
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize(
    "username,password,error_message",
    [
        ("", "fake_password", ErrorType.USERNAME_ERROR.value),
    ],
)
def test__login_with_missing_username__username_error_shown(
    login_page, username, password, error_message
):
    login_page.login(username, password)
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize(
    "username,password,error_message",
    [
        ("", "", ErrorType.USERNAME_ERROR.value),
    ],
)
def test__login_with_missing_credentials__username_error_shown(
    login_page, username, password, error_message
):
    login_page.login(username, password)
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize(
    "username,password,error_message",
    [
        ("fake_username", "", ErrorType.PASSWORD_ERROR.value),
    ],
)
def test__login_with_missing_password__password_error_shown(
    login_page, username, password, error_message
):
    login_page.login(username, password)
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize(
    "username,password,error_message",
    [
        (
            "locked_out_user",
            "secret_sauce",
            ErrorType.LOCKED_OUT_ERROR.value,
        ),
    ],
)
def test__login_locked_out_user__locked_out_error_shown(
    login_page, username, password, error_message
):
    login_page.login(username, password)
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ],
)
def test__login_with_proper_credentials__inventory_page_loaded(
    login_page, username, password
):
    login_page.login(username, password)
    inventory_page_title = login_page.get_element(
        name="title", by_type="classname"
    ).text
    assert inventory_page_title == "PRODUCTS"

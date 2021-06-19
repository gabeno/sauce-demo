import pytest

from project.pages import LoginFormError, User
from project.pages.page_login import LoginPage


@pytest.mark.parametrize(
    "username,password,error_message",
    [
        (
            "fake_username",
            "fake_password",
            LoginFormError.USERNAME_AND_PASSWORD_ERROR.value,
        ),
        ("", "fake_password", LoginFormError.USERNAME_ERROR.value),
        ("", "", LoginFormError.USERNAME_ERROR.value),
        ("fake_username", "", LoginFormError.PASSWORD_ERROR.value),
        (
            "locked_out_user",
            "secret_sauce",
            LoginFormError.LOCKED_OUT_ERROR.value,
        ),
    ],
)
def test__failed_logins__error_message_shown(
    driver, username, password, error_message
):
    user = User(username, password)
    login_page = LoginPage(driver, user)
    assert login_page.get_error_message() == error_message

    # clear error message
    # this is not strictly needed but documents the full flow
    login_page.click_error_button()


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ],
)
def test__login_with_proper_credentials__inventory_page_loaded(
    driver, username, password
):
    with pytest.raises(Exception):
        user = User(username, password)
        login_page = LoginPage(driver, user)
        # raises because no error on success
        login_page.get_error_message()

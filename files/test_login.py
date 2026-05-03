import pytest
from pages.login_page import LoginPage

VALID_USER = "mngr593986"
VALID_PASS = "amErAby"


class TestLogin:
    """Test suite for Guru99 Bank Login functionality."""

    def test_valid_login(self, page):
        """TC_LOGIN_01 - Valid credentials should log in successfully."""
        login = LoginPage(page)
        login.navigate()
        login.login(VALID_USER, VALID_PASS)
        assert login.is_logged_in(), "Expected to be logged in with valid credentials."

    def test_blank_username(self, page):
        """TC_LOGIN_02 - Blank username should show alert."""
        login = LoginPage(page)
        login.navigate()

        # Handle browser alert
        page.on("dialog", lambda dialog: dialog.accept())
        login.login("", VALID_PASS)

    def test_blank_password(self, page):
        """TC_LOGIN_03 - Blank password should show alert."""
        login = LoginPage(page)
        login.navigate()

        page.on("dialog", lambda dialog: dialog.accept())
        login.login(VALID_USER, "")

    def test_invalid_credentials(self, page):
        """TC_LOGIN_04 - Wrong credentials should show error."""
        login = LoginPage(page)
        login.navigate()
        login.login("wronguser", "wrongpass")
        error = login.get_error_message()
        assert "User or Password is not valid" in error, f"Unexpected error: {error}"

    def test_reset_clears_fields(self, page):
        """TC_LOGIN_05 - Reset button should clear input fields."""
        login = LoginPage(page)
        login.navigate()
        page.fill("input[name='uid']", VALID_USER)
        page.fill("input[name='password']", VALID_PASS)
        login.reset()
        assert page.input_value("input[name='uid']") == ""
        assert page.input_value("input[name='password']") == ""

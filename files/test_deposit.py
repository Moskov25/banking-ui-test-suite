import pytest


class TestDeposit:
    """Test suite for Deposit Amount functionality."""

    def test_blank_account_number(self, logged_in_page):
        """TC_DEP_01 - Blank account number should trigger validation."""
        logged_in_page.click("a[href='DepositInput.php']")
        logged_in_page.wait_for_load_state("networkidle")
        logged_in_page.click("input[name='accountno']")
        logged_in_page.press("input[name='accountno']", "Tab")
        error = logged_in_page.inner_text("label#message2")
        assert "Account Number must not be blank" in error

    def test_characters_not_allowed_in_account(self, logged_in_page):
        """TC_DEP_02 - Characters in account number field should show error."""
        logged_in_page.click("a[href='DepositInput.php']")
        logged_in_page.wait_for_load_state("networkidle")
        logged_in_page.fill("input[name='accountno']", "abcd")
        logged_in_page.press("input[name='accountno']", "Tab")
        error = logged_in_page.inner_text("label#message2")
        assert "Characters are not allowed" in error

    def test_blank_amount_shows_error(self, logged_in_page):
        """TC_DEP_03 - Blank amount field should trigger validation."""
        logged_in_page.click("a[href='DepositInput.php']")
        logged_in_page.wait_for_load_state("networkidle")
        logged_in_page.click("input[name='ammount']")
        logged_in_page.press("input[name='ammount']", "Tab")
        error = logged_in_page.inner_text("label#message1")
        assert "Amount field must not be blank" in error

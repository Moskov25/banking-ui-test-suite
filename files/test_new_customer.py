import pytest
import random
import string
from pages.new_customer_page import NewCustomerPage


def random_email():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"testuser_{suffix}@gmail.com"


class TestNewCustomer:
    """Test suite for Add New Customer functionality."""

    def test_add_customer_successfully(self, logged_in_page):
        """TC_NC_01 - Valid data should create a new customer."""
        nc = NewCustomerPage(logged_in_page)
        nc.navigate()
        nc.fill_customer_form(
            name="Hope Sinha",
            dob="01/01/1995",
            address="123 Main Street",
            city="Bengaluru",
            state="Karnataka",
            pin="560001",
            mobile="9876543210",
            email=random_email(),
            password="Test@1234"
        )
        nc.submit()
        assert nc.is_success(), "Customer registration should succeed with valid data."

    def test_blank_name_shows_error(self, logged_in_page):
        """TC_NC_02 - Blank name field should trigger validation."""
        nc = NewCustomerPage(logged_in_page)
        nc.navigate()
        logged_in_page.click("input[name='name']")
        logged_in_page.press("input[name='name']", "Tab")
        error = logged_in_page.inner_text("label#message")
        assert "Customer name must not be blank" in error

    def test_numeric_name_shows_error(self, logged_in_page):
        """TC_NC_03 - Numeric characters in name should show error."""
        nc = NewCustomerPage(logged_in_page)
        nc.navigate()
        logged_in_page.fill("input[name='name']", "1234")
        logged_in_page.press("input[name='name']", "Tab")
        error = logged_in_page.inner_text("label#message")
        assert "Numbers are not allowed" in error

    def test_invalid_pin_shows_error(self, logged_in_page):
        """TC_NC_04 - PIN less than 6 digits should show error."""
        nc = NewCustomerPage(logged_in_page)
        nc.navigate()
        logged_in_page.fill("input[name='pinno']", "123")
        logged_in_page.press("input[name='pinno']", "Tab")
        error = logged_in_page.inner_text("label#message14")
        assert "PIN Code must have 6 Digits" in error

    def test_invalid_email_shows_error(self, logged_in_page):
        """TC_NC_05 - Invalid email format should show error."""
        nc = NewCustomerPage(logged_in_page)
        nc.navigate()
        logged_in_page.fill("input[name='emailid']", "notanemail")
        logged_in_page.press("input[name='emailid']", "Tab")
        error = logged_in_page.inner_text("label#message9")
        assert "Email-ID is not valid" in error

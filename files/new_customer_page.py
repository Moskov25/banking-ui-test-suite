class NewCustomerPage:
    """Page Object for Add New Customer functionality."""

    def __init__(self, page):
        self.page = page

        # Locators
        self.name_input = "input[name='name']"
        self.dob_input = "input[name='dob']"
        self.address_input = "textarea[name='addr']"
        self.city_input = "input[name='city']"
        self.state_input = "input[name='state']"
        self.pin_input = "input[name='pinno']"
        self.mobile_input = "input[name='telephoneno']"
        self.email_input = "input[name='emailid']"
        self.password_input = "input[name='password']"
        self.submit_button = "input[name='sub']"
        self.reset_button = "input[name='res']"

    def navigate(self):
        self.page.click("a[href='addcustomer.php']")
        self.page.wait_for_load_state("networkidle")

    def fill_customer_form(self, name, dob, address, city, state, pin, mobile, email, password):
        self.page.fill(self.name_input, name)
        self.page.fill(self.dob_input, dob)
        self.page.fill(self.address_input, address)
        self.page.fill(self.city_input, city)
        self.page.fill(self.state_input, state)
        self.page.fill(self.pin_input, pin)
        self.page.fill(self.mobile_input, mobile)
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)

    def submit(self):
        self.page.click(self.submit_button)
        self.page.wait_for_load_state("networkidle")

    def reset(self):
        self.page.click(self.reset_button)

    def get_customer_id(self) -> str:
        """Extract newly created customer ID from success table."""
        try:
            return self.page.inner_text("td:has-text('Customer ID') + td")
        except Exception:
            return ""

    def is_success(self) -> bool:
        return "Customer Registered Successfully" in self.page.content()

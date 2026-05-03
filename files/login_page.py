class LoginPage:
    """Page Object for Guru99 Bank Login Page."""

    def __init__(self, page):
        self.page = page
        self.url = "https://demo.guru99.com/v4/"

        # Locators
        self.username_input = "input[name='uid']"
        self.password_input = "input[name='password']"
        self.login_button = "input[name='btnLogin']"
        self.reset_button = "input[name='btnClear']"
        self.error_message = "p.barone"

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        self.page.wait_for_load_state("networkidle")

    def reset(self):
        self.page.click(self.reset_button)

    def get_error_message(self) -> str:
        return self.page.inner_text(self.error_message)

    def is_logged_in(self) -> bool:
        return "Guru99 Bank Manager HomePage" in self.page.title()

import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://demo.guru99.com/v4/"
ADMIN_USER = "mngr593986"
ADMIN_PASS = "amErAby"


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    """Returns a page already logged in as admin."""
    page.goto(BASE_URL)
    page.fill("input[name='uid']", ADMIN_USER)
    page.fill("input[name='password']", ADMIN_PASS)
    page.click("input[name='btnLogin']")
    page.wait_for_load_state("networkidle")
    yield page

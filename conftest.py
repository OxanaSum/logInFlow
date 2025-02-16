import pytest
from playwright.sync_api import  Page, sync_playwright

from components.base_page import BasePage
from components.login_page import LoginPage
from components.password_page import PasswordPage

@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def password_page(page: Page):
    return PasswordPage(page)

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context()

        yield context
        context.close()
        browser.close()
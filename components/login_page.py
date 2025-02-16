from playwright.sync_api import Page, expect
from settings import PRE_LOGIN_URL
from locators.login_page_locators import login_page_title_locator, email_field_locator, next_btn_locator, \
    error_message_locator


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self):
        self.page.goto(PRE_LOGIN_URL)

    def check_login_page_is_open(self):
        title = self.page.locator(login_page_title_locator)
        expect(title).to_be_visible()

    def check_email_field_is_visible(self):
        email_field = self.page.locator(email_field_locator)
        expect(email_field).to_be_visible()

    def check_next_btn_is_visible(self):
        next_btn = self.page.locator(next_btn_locator)
        expect(next_btn).to_be_visible()

    def fill_email(self, email):
        self.page.locator(email_field_locator).fill(email)

    def click_next_btn(self):
        self.page.locator(next_btn_locator).click()

    def check_error_message_is_visible(self):
        error_message = self.page.locator(error_message_locator)
        expect(error_message).to_be_visible()
        assert error_message.text_content(), "Required field"
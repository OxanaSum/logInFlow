from playwright.sync_api import Page, expect
from settings import PRE_LOGIN_URL

from locators.login_page_locators import email_field_locator, next_btn_locator
from locators.password_page_locators import submit_btn_locator, password_field_locator, page_title_locator, \
    error_message_locator, several_errors_message_locator


class PasswordPage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, email):
        self.page.goto(PRE_LOGIN_URL)
        self.page.locator(email_field_locator).fill(email)
        self.page.locator(next_btn_locator).click()

    def check_password_page_is_open(self):
        title = self.page.locator(page_title_locator)
        expect(title).to_be_visible()

    def check_password_field_is_visible(self):
        password_field = self.page.locator(password_field_locator)
        expect(password_field).to_be_visible()

    def check_submit_btn_is_visible(self):
        submit_btn = self.page.locator(submit_btn_locator)
        expect(submit_btn).to_be_visible()

    def fill_password(self, passw):
        self.page.locator(password_field_locator).fill(passw)

    def click_submit_btn(self):
        self.page.locator(submit_btn_locator).click()

    def check_error_message(self):
        error_message = self.page.locator(error_message_locator)
        error_message.is_visible()
        assert error_message.text_content(), "Unable to log in"

    def check_several_errors_message(self):
        error_message = self.page.locator(several_errors_message_locator)
        error_message.is_visible()
        assert error_message.text_content(), "We found several errors. Please check that the form is filled out correctly and make corrections."


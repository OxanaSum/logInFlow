from playwright.sync_api import Page, expect
from settings import BASE_URL
from locators.base_page_locators import base_page_title_loc,base_page_login_loc


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self):
        self.page.goto(BASE_URL)

    def check_base_page_is_open(self):
        title = self.page.locator(base_page_title_loc)
        expect(title).to_be_visible()
        #assert "Demos that win.", title

    def check_login_btn_is_visible(self):
        login_btn = self.page.locator(base_page_login_loc)
        expect(login_btn).to_be_visible()

    def click_login_btn(self):
        self.page.locator(base_page_login_loc).click()


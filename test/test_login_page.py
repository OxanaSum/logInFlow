from conftest import login_page
from data import valid_login, invalid_login, login_320_chars, login_1000_chars, non_email

#TC_004
def test_pre_login_page_is_visible(login_page):
    login_page.visit()
    login_page.check_login_page_is_open()

#TC_005
def test_email_field_is_visible(login_page):
    login_page.visit()
    login_page.check_email_field_is_visible()

#TC_006
def test_next_btn_is_visible(login_page):
    login_page.visit()
    login_page.check_email_field_is_visible()

#TC_007
def test_next_btn_with_valid_email(login_page, password_page):
    login_page.visit()
    login_page.fill_email(valid_login)
    login_page.click_next_btn()
    password_page.check_password_page_is_open()

#TC_008
def test_next_btn_with_invalid_email(login_page, password_page):
    login_page.visit()
    login_page.fill_email(invalid_login)
    login_page.click_next_btn()
    password_page.check_password_page_is_open()

#TC_009
def test_next_btn_with_invalid_email_320_chars(login_page, password_page):
    login_page.visit()
    login_page.fill_email(login_320_chars)
    login_page.click_next_btn()
    password_page.check_password_page_is_open()

#TC_010
def test_next_btn_with_invalid_email_1000_chars(login_page, password_page):
    login_page.visit()
    login_page.fill_email(login_1000_chars)
    login_page.click_next_btn()
    password_page.check_password_page_is_open()

#TC_011
def test_next_btn_with_empty_email(login_page):
    login_page.visit()
    login_page.fill_email("")
    login_page.click_next_btn()
    login_page.check_error_message_is_visible()

#TC_012
def test_next_btn_with_non_email_string(login_page):
    login_page.visit()
    login_page.fill_email(non_email)
    login_page.click_next_btn()
    login_page.check_error_message_is_visible()
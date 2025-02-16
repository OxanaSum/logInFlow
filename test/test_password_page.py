from conftest import password_page
from data import valid_login, invalid_login, login_320_chars, login_1000_chars, invalid_password, long_password_320_chars


#TC_013
def test_passw_field_is_visible(password_page):
    password_page.visit(valid_login)
    password_page.check_password_field_is_visible()

#TC_014
def test_submit_btn_is_visible(password_page):
    password_page.visit(valid_login)
    password_page.check_submit_btn_is_visible()

#TC_015
def test_submit_btn_click_with_invalid_passw(password_page):
    password_page.visit(valid_login)
    password_page.fill_password(invalid_password)
    password_page.click_submit_btn()
    password_page.check_error_message()

#TC_016
def test_submit_btn_click_with_empty_passw(password_page):
    password_page.visit(valid_login)
    password_page.fill_password("")
    password_page.click_submit_btn()
    password_page.check_several_errors_message()

#TC_017
def test_submit_btn_click_with_invalid_email_and_passw(password_page):
    password_page.visit(invalid_login)
    password_page.fill_password(invalid_password)
    password_page.click_submit_btn()
    password_page.check_error_message()

#TC_018
def test_submit_btn_click_with_email_320chars_and_invalid_passw(password_page):
    password_page.visit(login_320_chars)
    password_page.fill_password(invalid_password)
    password_page.click_submit_btn()
    password_page.check_error_message()

#TC_019
def test_submit_btn_click_with_email_1000chars_and_invalid_passw(password_page):
    password_page.visit(login_1000_chars)
    password_page.fill_password(invalid_password)
    password_page.click_submit_btn()
    password_page.check_error_message()

#TC_020
def test_submit_btn_click_with_long_passw_320_chars(password_page):
    password_page.visit(valid_login)
    password_page.fill_password(long_password_320_chars)
    password_page.click_submit_btn()
    password_page.check_error_message()

from conftest import base_page

#TC_001
def test_base_page_is_visible(base_page):
    base_page.visit()
    base_page.check_base_page_is_open()

#TC_002
def test_login_btn_is_visible(base_page):
    base_page.visit()
    base_page.check_login_btn_is_visible()

#TC_003
def test_loging_click(base_page, login_page):
    base_page.visit()
    base_page.click_login_btn()
    login_page.check_login_page_is_open()



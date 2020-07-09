def test_find_button_on_the_page(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button, "button not found"

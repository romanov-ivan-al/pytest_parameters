import pytest
from selenium import webdriver
#import time 

def test_guest_should_see_button_add(browser,language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207"
    browser.get(link)
    #time.sleep(30)
    button = browser.find_elements_by_id("add_to_basket_form") 
    assert len(button) > 0, """!!!"add to cart button" not found!!!"""
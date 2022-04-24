from urllib import request
import pytest
from selenium import webdriver
    
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Choose language: ru or es")

@pytest.fixture
def language(request):
    return request.config.getoption("language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


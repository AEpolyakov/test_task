import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """parse parameter"""
    parser.addoption('--language', action='store', default='en', help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    """fixture that open chrome webbrowser and yield it"""
    user_language = request.config.getoption('language')

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    # browser.implicitly_wait(2)

    yield browser
    browser.quit()

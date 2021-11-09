import pytest
from .pages.search_page import SearchPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class TestBuyIn10Seconds:

    link = 'https://buy-in-10-seconds.company.site/search'

    def test_keyword(self, browser):
        page = SearchPage(browser, self.link)



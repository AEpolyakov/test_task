import pytest
from .pages.search_page import SearchPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestBuyIn10Seconds:

    link = 'https://buy-in-10-seconds.company.site/search'

    def test_price_filter(self, browser):
        page = SearchPage(browser, self.link)
        page.open()

        # check for products in page before filtering
        page.check_products()

        # apply price_from filter and check products
        prices = {'from': '1'}
        page.set_price(prices)
        page.check_products(prices=prices)

        # apply price_from and price_to filters and check products
        prices = {'from': '1', 'to': '4'}
        page.set_price(prices)
        page.check_products(prices=prices)

        # apply price_to filter and check products
        prices = {'to': '4'}
        page.set_price(prices)
        page.check_products(prices=prices)

        # apply no price filters and check products
        page.set_price()
        page.check_products(prices=prices)

    # def test_in_stock_filter(self, browser):
    #     page = SearchPage(browser, self.link)
    #     page.open()
    #
    #     # check for products in page before filtering
    #     page.check_products()
    #
    #     page.toggle_in_stock()
    #     page.check_products(in_stock=True)
    #
    #     page.toggle_in_stock()
    #     page.check_products()

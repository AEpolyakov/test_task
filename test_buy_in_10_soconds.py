import pytest
from .pages.search_page import SearchPage
from .pages.constants import DISCOUNT, KEYWORD, IN_STOCK, PRICE_FROM, PRICE_TO


class TestBuyIn10Seconds:

    link = 'https://buy-in-10-seconds.company.site/search'

    def test_out_of_stock(self, browser):
        """
        test in stock filter in search page

        1) go to search page
        2) click on in stock filter
        3) check if filter is applied
        4) check if there are no product that out of stock
        """
        check_method = {IN_STOCK}

        page = SearchPage(browser, self.link)
        page.open()
        page.toggle_in_stock()
        page.check_filter(check_method)
        page.check_products(check_method)

    def test_discount(self, browser):
        """
        test discount filter in search page

        1) go to search page
        2) click on discount filter
        3) check if filter is applied
        4) check if all product have discount label
        """
        check_method = {DISCOUNT}

        page = SearchPage(browser, self.link)
        page.open()
        page.toggle_discount()
        page.check_filter(check_method)
        page.check_products(check_method)

    def test_price_filter(self, browser):
        """
        test price filter in search page

        1) go to search page
        2) set price
        3) check if filter is applied
        4) check if product prices are within price limits
        """
        check_method = {PRICE_FROM: 2}

        page = SearchPage(browser, self.link)
        page.open()
        page.set_price(check_method)
        page.check_filter(check_method)
        page.check_products(check_method)

    @pytest.mark.xfail(reason='filter is broken')
    def test_name_filter(self, browser):
        """
        test keyword filter in search page

        1) go to search page
        2) set name in keyword filter and press enter
        3) check if filter is applied
        4) check if all product names contains keyword filter value
        """
        name_filter_value = 'Товар 3'
        check_method = {KEYWORD: name_filter_value}

        page = SearchPage(browser, self.link)
        page.open()
        page.set_name_filter(name_filter_value)
        page.check_filter(check_method)
        page.check_products(check_method)

    @pytest.mark.xfail(reason="discount filter become not intractable after price filter apply")
    def test_price_and_discount_filters(self, browser):
        """
        test price filter and discount filter in search page

        1) go to search page
        2) set price in price filter
        3) check if filter is applied
        4) check if all product prices are within limits
        5) click on discount filter
        6) check if both filters are applied
        7) check products satisfy specified values
        """
        check_method = {PRICE_FROM: 1, PRICE_TO: 3}

        page = SearchPage(browser, self.link)
        page.open()

        page.set_price(check_method)
        page.check_filter(check_method)

        page.toggle_discount()
        check_method[DISCOUNT] = None
        page.check_filter(check_method)

        page.check_products(check_method)

    def test_price_and_in_stock_filters(self, browser):
        """
        test price filter and in stock filter in search page

        1) go to search page
        2) set price in price filter
        3) check if filter is applied
        4) check if all product prices are within limits
        5) click on in stock filter
        6) check if both filters are applied
        7) check products satisfy specified values
        """
        check_method = {PRICE_FROM: 1, PRICE_TO: 3}

        page = SearchPage(browser, self.link)
        page.open()

        page.set_price(check_method)
        page.check_filter(check_method)

        page.toggle_in_stock()
        check_method[IN_STOCK] = None
        page.check_filter(check_method)

        page.check_products(check_method)


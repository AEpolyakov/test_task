import pytest
from .pages.search_page import SearchPage


class TestBuyIn10Seconds:

    link = 'https://buy-in-10-seconds.company.site/search'

    def test_out_of_stock(self, browser):
        """
        test in stock filter in search page

        1) go to search page
        2) click on in stock filter
        3) check if there are no product that out of stock
        """
        check_by = {'in_stock'}

        page = SearchPage(browser, self.link)
        page.open()

        page.toggle_in_stock()

        page.check_products(check_by)

    def test_discount(self, browser):
        """
        test discount filter in search page

        1) go to search page
        2) click on discount filter
        3) check if all product have discount label
        """
        check_by = {'discount'}

        page = SearchPage(browser, self.link)
        page.open()

        page.toggle_discount()

        page.check_products(check_by)

    def test_price_filter(self, browser):
        """
        test price filter in search page

        1) go to search page
        2) set price
        3) check if product prices are within price limits
        """
        prices = {'from': 1, 'to': 3}
        check_by = {'price': (prices['from'], prices['to'])}

        page = SearchPage(browser, self.link)
        page.open()

        page.set_price(prices)

        page.check_products(check_by)

    @pytest.mark.xfail
    def test_name_filter(self, browser):
        """
        test keyword filter in search page

        1) go to search page
        2) set name in keyword filter and press enter
        3) check if all product names contains keyword filter value
        """
        name_filter_value = 'Товар 3'
        check_by = {'name': name_filter_value}

        page = SearchPage(browser, self.link)
        page.open()

        page.set_name_filter(name_filter_value)

        page.check_products(check_by)

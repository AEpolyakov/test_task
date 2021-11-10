import pytest
import time
from .pages.search_page import SearchPage


class TestBuyIn10Seconds:

    link = 'https://buy-in-10-seconds.company.site/search'

    # def test_out_of_stock(self, browser):
    #     page = SearchPage(browser, self.link)
    #     page.open()
    #
    #     check_by = {'in_stock'}
    #     page.toggle_in_stock()
    #     page.check_products(check_by)
    #
    # def test_discount(self, browser):
    #     page = SearchPage(browser, self.link)
    #     page.open()
    #
    #     check_by = {'discount'}
    #     page.toggle_discount()
    #     page.check_products(check_by)

    # def test_price_filter(self, browser):
    #     page = SearchPage(browser, self.link)
    #     page.open()
    #
    #     prices = {'from': 1, 'to': 3}
    #     check_by = {'price': (prices['from'], prices['to'])}
    #     page.set_price(prices)
    #     page.check_products(check_by)

    @pytest.mark.xfail
    def test_name_filter(self, browser):
        page = SearchPage(browser, self.link)
        page.open()

        name_filter_value = 'Товар 3'
        check_by = {'name': name_filter_value}
        page.set_name_filter(name_filter_value)
        page.check_products(check_by)
        time.sleep(5)

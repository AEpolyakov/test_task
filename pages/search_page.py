import re
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import SearchPageLocators
from .products import Products
from .constants import DISCOUNT, KEYWORD, IN_STOCK, PRICE_FROM, PRICE_TO


class SearchPage(BasePage):
    """
    search page class
    realises methods for search page
    """

    def get_products(self):
        products = Products()
        product_elements = self.get_elements(SearchPageLocators.PRODUCTS, timeout=5)
        for element in product_elements:
            name = self.get_sub_element_text(element, SearchPageLocators.PRODUCT_NAME)
            price = self.get_sub_element_text(element, SearchPageLocators.PRODUCT_PRICE)
            label_sale = self.get_sub_element_text(element, SearchPageLocators.PRODUCT_LABEL_SALE)
            label_out_of_stock = self.get_sub_element_text(element, SearchPageLocators.PRODUCT_LABEL_OUT_OF_STOCK)
            products.append(name, price, label_sale, label_out_of_stock)
        return products

    def check_products(self, check_method):
        """
        search for products on search page.
        in products search for name, price, labels
        """

        time.sleep(self.default_script_timeout)
        products = None
        for find_try in range(self.default_timeout):
            try:
                products = self.get_products()
                break
            except StaleElementReferenceException:
                time.sleep(self.default_script_timeout)
        print(products)

        if DISCOUNT in check_method:
            print('assert products by discount')
            assert products.are_discount_only(), 'there are products without discount'

        if IN_STOCK in check_method:
            print('assert products by in stock')
            assert products.are_not_out_of_stock(), 'there are out of stock products'

        if PRICE_FROM in check_method:
            print('assert products by in price from')
            assert products.are_in_price_from(check_method[PRICE_FROM]), \
                f'there are products with price less than {check_method[PRICE_FROM]}'

        if PRICE_TO in check_method:
            print('assert products by in price to')
            assert products.are_in_price_to(check_method[PRICE_TO]), \
                f'there are products with price more than {check_method[PRICE_TO]}'

        if KEYWORD in check_method:
            print('assert products by in keyword')
            assert products.are_in_name_filter(check_method[KEYWORD]), 'name filter not working'

    def get_filters(self, check_method):
        filters = {}
        if DISCOUNT in check_method:
            filters[DISCOUNT] = self.get_element(SearchPageLocators.FILTER_WITH_DISCOUNT).get_attribute('checked'),

        if IN_STOCK in check_method:
            filters[IN_STOCK] = self.get_element(SearchPageLocators.FILTER_IN_STOCK).get_attribute('checked')

        filter_pills = self.get_elements(SearchPageLocators.FILTER_PILL)
        for pill in filter_pills:
            pill_text = pill.text
            if '$' in pill_text:
                price_pill_text = pill.text
                prices = re.findall(r'\$\d+', price_pill_text)
                if PRICE_FROM in check_method and PRICE_TO in check_method:
                    filters[PRICE_FROM] = prices[0].replace('$', '')
                    filters[PRICE_TO] = prices[1].replace('$', '')
                elif PRICE_FROM in check_method:
                    filters[PRICE_FROM] = prices[0].replace('$', '')
                elif PRICE_TO in check_method:
                    filters[PRICE_TO] = prices[0].replace('$', '')
            if KEYWORD in check_method and check_method[KEYWORD] in pill_text:
                filters[KEYWORD] = pill_text
        return filters

    def check_filter(self, check_method):
        time.sleep(self.default_script_timeout)

        filters = {}
        for find_try in range(self.default_timeout):
            try:
                filters = self.get_filters(check_method)
                break
            except (StaleElementReferenceException, NoSuchElementException):
                time.sleep(1)

        print(f'FILTERS: {filters}')

        if DISCOUNT in check_method:
            print('assert filters by discount')
            assert DISCOUNT in filters, 'discount filter have not been applied'

        if IN_STOCK in check_method:
            print('assert filters by in stock')
            assert IN_STOCK in filters, 'in stock filter have not been applied'

        if PRICE_FROM in check_method:
            print('assert filters by in price from')
            assert float(filters[PRICE_FROM]) == check_method[PRICE_FROM], 'price from filter is not working'

        if PRICE_TO in check_method:
            print('assert filters by in price to')
            assert float(filters[PRICE_TO]) == check_method[PRICE_TO], 'price to filter is not working'

        if KEYWORD in check_method:
            print('assert filters by in keyword')
            assert KEYWORD in check_method, 'keyword filter have not been applied'

    def clear_filters(self):
        """click to clear all filters link"""
        self.click_element(SearchPageLocators.FILTER_CLEAR_ALL)

    def set_price(self, check_method):
        """set price filter from given dict"""
        if PRICE_FROM in check_method:
            self.send_keys(check_method[PRICE_FROM], SearchPageLocators.FILTER_PRICE_FROM)
            self.send_keys(Keys.ENTER, SearchPageLocators.FILTER_PRICE_FROM)
            time.sleep(self.default_script_timeout)

        if PRICE_TO in check_method:
            self.send_keys(check_method[PRICE_TO], SearchPageLocators.FILTER_PRICE_TO)
            self.send_keys(Keys.ENTER, SearchPageLocators.FILTER_PRICE_TO)
            time.sleep(self.default_script_timeout)

    def toggle_in_stock(self):
        """find checkbox "in stock" and click on it"""
        self.click_element(SearchPageLocators.FILTER_IN_STOCK, timeout=5)

    def toggle_cat1(self):
        """find checkbox "category 1" and click on it"""
        self.click_element(SearchPageLocators.FILTER_CAT1, timeout=5)

    def toggle_discount(self):
        """find checkbox "discount" and click on it"""
        try:
            self.click_element(SearchPageLocators.FILTER_WITH_DISCOUNT, timeout=5)
        except ElementNotInteractableException:
            assert False, 'toggle filter is not intractable'

    def set_name_filter(self, filter_value):
        """find filter input and send keys to it"""
        self.send_keys(filter_value, SearchPageLocators.FILTER_KEYWORD)
        self.send_keys(Keys.ENTER, SearchPageLocators.FILTER_KEYWORD)

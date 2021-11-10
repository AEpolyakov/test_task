import time
from .base_page import BasePage
from .locators import SearchPageLocators
from .utils import Products
from selenium.common.exceptions import StaleElementReferenceException


class SearchPage(BasePage):
    """
    search page class
    realises methods for search page
    """
    default_timeout = 5

    def check_products(self, check_by=None):
        """
        search for products on search page.
        in products search for name, price, labels
        """
        products = Products()
        time.sleep(1)
        for find_try in range(self.default_timeout):
            print(f'for {find_try}')
            try:
                product_elements = self.get_elements(SearchPageLocators.PRODUCTS, timeout=5)
                for element in product_elements:
                    name = self.get_sub_element_text(element, SearchPageLocators.PRODUCT_NAME)
                    price = self.get_sub_element_text(element, SearchPageLocators.PRODUCT_PRICE)
                    label_sale = self.get_sub_element_text(element, SearchPageLocators.PRODUCT_LABEL_SALE)
                    label_out_of_stock = self.get_sub_element_text(element, SearchPageLocators.PRODUCT_LABEL_OUT_OF_STOCK)
                    products.append(name, price, label_sale, label_out_of_stock)
                break
            except StaleElementReferenceException:
                print(f'state element ref')
                time.sleep(1)
        print(products)

        if 'discount' in check_by:
            print('assert by discount')
            assert products.is_discount_only(), 'there are products without discount'

        if 'in_stock' in check_by:
            print('assert by in stock')
            assert products.is_not_out_of_stock(), 'there are out of stock products'

        if 'price' in check_by:
            print('assert by in price')
            assert products.is_in_price_range(check_by['price'][0], check_by['price'][1]), \
                'there are products with price out of range'

        if 'name' in check_by:
            print('assert by in keyword')
            assert products.is_in_name_filter(check_by['name']), 'name filter not working'

    def set_price(self, prices: dict):
        """set price filter from given dict"""
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{prices=} {prices["from"]=} {prices["to"]=}')
        if 'from' in prices:
            self.send_keys(keys=str(prices['from']),
                           locator=SearchPageLocators.FILTER_PRICE_FROM,
                           enter=True,
                           timeout=5)
        if 'to' in prices:
            self.send_keys(keys=str(prices['to']),
                           locator=SearchPageLocators.FILTER_PRICE_TO,
                           enter=True,
                           timeout=5)

    def clear_price_filter(self):
        """find clear price element and click on it"""
        self.click_element(SearchPageLocators.FILTER_PRICE_CLEAR, timeout=5)

    def toggle_in_stock(self):
        """find checkbox "in stock" and click on it"""
        self.click_element(SearchPageLocators.FILTER_IN_STOCK, timeout=5)

    def toggle_cat1(self):
        """find checkbox "category 1" and click on it"""
        self.click_element(SearchPageLocators.FILTER_CAT1, timeout=5)

    def toggle_discount(self):
        """find checkbox "discount" and click on it"""
        self.click_element(SearchPageLocators.FILTER_WITH_DISCOUNT, timeout=5)

    def set_name_filter(self, filter_value):
        """find filter input and send keys to it"""
        self.send_keys(keys=filter_value,
                       locator=SearchPageLocators.FILTER_KEYWORD,
                       enter=True)

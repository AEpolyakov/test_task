from .base_page import BasePage
from .locators import SearchPageLocators


class SearchPage(BasePage):

    def check_products_grid(self):
        pass

    def check_products(self, prices=None, in_stock=False, cat1=False):
        products = self.get_elements(SearchPageLocators.PRODUCTS)

    def set_price(self, prices=None):
        if 'from' in prices:
            self.send_keys(keys=prices['from'],
                           locator=SearchPageLocators.FILTER_PRICE_FROM,
                           enter=True)
        if 'to' in prices:
            self.send_keys(keys=prices['to'],
                           locator=SearchPageLocators.FILTER_PRICE_FROM,
                           enter=True)

    def clear_price_filter(self):
        self.click_element(SearchPageLocators.FILTER_PRICE_CLEAR)

    def toggle_in_stock(self):
        self.click_element(SearchPageLocators.FILTER_IN_STOCK)

    def toggle_cat1(self):
        self.click_element(SearchPageLocators.FILTER_CAT1)

    def toggle_discount(self):
        self.click_element(SearchPageLocators.FILTER_WITH_DISCOUNT)

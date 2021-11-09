from .base_page import BasePage
from .locators import SearchPageLocators


class SearchPage(BasePage):
    """
    search page class
    realises methods for search page
    """

    def check_products(self, prices=None, in_stock=False, cat1=False):
        """
        search for products on search page.
        in products search for name, price, labels
        """
        products = self.get_elements(SearchPageLocators.PRODUCTS)
        for product in products:
            name = self.get_sub_element(product, SearchPageLocators.PRODUCT_NAME)
            price = self.get_sub_element(product, SearchPageLocators.PRODUCT_PRICE)
            label_sale = self.get_sub_element(product, SearchPageLocators.PRODUCT_LABEL_SALE)
            label_out_of_stock = self.get_sub_element(product, SearchPageLocators.PRODUCT_LABEL_OUT_OF_STOCK)
            label_sale_text = label_sale.text if label_sale else ''
            label_out_of_stock_text = label_out_of_stock.text if label_out_of_stock else ''

            print(f'found product {name.text} {price.text} {label_sale_text} {label_out_of_stock_text}')

    def set_price(self, prices: dict):
        """set price filter from given dict"""
        if 'from' in prices:
            self.send_keys(keys=prices['from'],
                           locator=SearchPageLocators.FILTER_PRICE_FROM,
                           enter=True)
        if 'to' in prices:
            self.send_keys(keys=prices['to'],
                           locator=SearchPageLocators.FILTER_PRICE_TO,
                           enter=True)

    def clear_price_filter(self):
        """find clear price element and click on it"""
        self.click_element(SearchPageLocators.FILTER_PRICE_CLEAR)

    def toggle_in_stock(self):
        """find checkbox "in stock" and click on it"""
        self.click_element(SearchPageLocators.FILTER_IN_STOCK)

    def toggle_cat1(self):
        """find checkbox "category 1" and click on it"""
        self.click_element(SearchPageLocators.FILTER_CAT1)

    def toggle_discount(self):
        """find checkbox "discount" and click on it"""
        self.click_element(SearchPageLocators.FILTER_WITH_DISCOUNT)

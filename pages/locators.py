from selenium.webdriver.common.by import By


class BasePageLocators:
    PRODUCT_COUNT = (1, 1)
    FILTER_KEYWORD = (1, 1)
    FILTER_PRICE_FROM = (1, 1)
    FILTER_PRICE_UP_TO = (1, 1)
    FILTER_IN_STOCK = (1, 1)
    FILTER_WITH_DISCOUNT = (1, 1)
    FILTER_CAT1 = (1, 1)
    FILTER_SORT = (1, 1)

    PRODUCTS_GRID = (By.CSS_SELECTOR, '.grid__wrap-inner')






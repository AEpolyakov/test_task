from selenium.webdriver.common.by import By


class SearchPageLocators:
    PRODUCT_COUNT = (1, 1)
    PRODUCTS = (By.CSS_SELECTOR, '.grid-product--has-shadow')
    PRODUCT_NAME = (By.XPATH, './/div[@class="grid-product__title-inner"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.ec-price-item')
    PRODUCT_LABEL_OUT_OF_STOCK = (By.CSS_SELECTOR, '.ec-label.label--attention')
    PRODUCT_LABEL_SALE = (By.CSS_SELECTOR, '.ec-label.label--notice')

    FILTER_KEYWORD = (By.XPATH, '//input[@name="keyword"]')

    FILTER_PRICE_FROM = (By.CSS_SELECTOR, '.ec-filter__price-from input')
    FILTER_PRICE_TO = (By.CSS_SELECTOR, '.ec-filter__price-to input')
    FILTER_PRICE_CLEAR = (By.CSS_SELECTOR, '.ec-filter--price .ec-link--hover')

    FILTER_IN_STOCK = (By.ID, 'checkbox-in_stock')
    FILTER_WITH_DISCOUNT = (By.ID, 'checkbox-on_sale')
    FILTER_CAT1 = (By.ID, 'checkbox-category-122178970')

    PRODUCTS_GRID = (By.CSS_SELECTOR, '.grid__wrap-inner')

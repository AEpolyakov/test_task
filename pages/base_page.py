from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def click_element(self, locator):
        self.browser.find_element(*locator).click()

    def get_elements(self, locator):
        return self.browser.find_elements(*locator)

    def get_sub_element(self, element, locator):
        return element.find_element(*locator)

    def send_keys(self, keys, locator, enter=False):
        suffix = Keys.ENTER if enter else ''
        self.browser.find_element(*locator).send_keys(keys + suffix)

    def open(self):
        self.browser.open(self.link)





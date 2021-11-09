from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """base page class. Realise common methods."""

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def click_element(self, locator):
        """find element and click on it"""
        self.browser.find_element(*locator).click()

    def get_elements(self, locator, timeout=3):
        """wait until at least 1 element show on page. Returns list of webelements or None"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.presence_of_element_located(locator))
            return self.browser.find_elements(*locator)
        except NoSuchElementException:
            return None

    @staticmethod
    def get_sub_element(element, locator):
        """search for element inside given element"""
        try:
            return element.find_element(*locator)
        except NoSuchElementException:
            return None

    def send_keys(self, keys, locator, enter=False):
        """
        find element and send keys to it
        If enter==True also appended key ENTER
        """
        suffix = Keys.ENTER if enter else ''
        self.browser.find_element(*locator).send_keys(keys + suffix)

    def open(self):
        """open page"""
        self.browser.get(self.link)





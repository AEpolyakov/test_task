import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """base page class. Realise common methods."""

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link
        self.default_timeout = 3

    def click_element(self, locator, timeout=0):
        """find element and click on it"""

        element = self.get_element(locator)
        if element:
            element.click()

    def get_element(self, locator, timeout=3):
        element = WebDriverWait(driver=self.browser,
                                timeout=timeout,
                                ignored_exceptions=(TimeoutException, NoSuchElementException)).until(
            EC.presence_of_element_located(locator))
        return element

    def get_elements(self, locator, timeout=0):
        """wait until at least 1 element show on page. Returns list of webelements or None"""
        elements = WebDriverWait(driver=self.browser,
                                 timeout=timeout,
                                 ignored_exceptions=(TimeoutException, NoSuchElementException)).until(
            EC.presence_of_all_elements_located(locator))
        return elements

    @staticmethod
    def get_sub_element_text(element, locator):
        try:
            sub_element = element.find_element(*locator)
            return sub_element.text
        except NoSuchElementException:
            return ''

    def send_keys(self, keys, locator, enter=False, timeout=0):
        """
        find element and send keys to it
        If enter==True also appended key ENTER
        """
        element = self.get_element(locator, timeout=timeout)
        if element:
            element.send_keys(keys)

    def open(self):
        """open page"""
        self.browser.get(self.link)

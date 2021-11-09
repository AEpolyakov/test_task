

class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open(self):
        self.browser.open(self.link)

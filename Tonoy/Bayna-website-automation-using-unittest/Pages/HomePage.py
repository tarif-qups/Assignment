# from telnetlib import EC
#
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver import ActionChains
#
# from Locators import Locators


class HomePage(object):
    def __init__(self, driver, base_url=""):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element2(self, *locator):
        return self.driver.find_element(*locator)

    def find_all_element(self, *locator):
        return self.driver.find_elements(*locator)


    def scroll_to(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView()", locator)

    def scroll_to1(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView()", locator)

    def scroll_to2(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView()", locator)

    def scroll_to3(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView()", locator)
from Pages.HomePage import HomePage
from Locators.Locators import TopBar


class TopBarPage(HomePage):

    def __init__(self, driver):
        self.locator = TopBar
        self.driver = driver
        super(TopBarPage, self).__init__(driver)

    def click_home(self):
        self.driver.find_element(*self.locator.home_XPATH).click()

    def click_greenchicken(self):
        self.driver.find_element(*self.locator.greenchicken_XPATH).click()

    def click_orderchicken(self):
        self.driver.find_element(*self.locator.orderchicken_XPATH).click()

    def click_addorderchicken(self):
        self.driver.find_element(*self.locator.addorderchicken_XPATH).click()

    def click_beef(self):
        self.driver.find_element(*self.locator.beef_XPATH).click()

    def click_orderbeef(self):
        self.driver.find_element(*self.locator.orderbeef_XPATH).click()

    def click_addorderbeef(self):
        self.driver.find_element(*self.locator.addorderbeef_XPATH).click()

    def click_avatar(self):
        self.driver.find_element(*self.locator.avatar_XPATH).click()

    def click_logout(self):
        self.driver.find_element(*self.locator.logout_link_XPATH).click()

    def scroll_to_element1(self):
        element1 = self.driver.find_element(*self.locator.orderbeef_XPATH)
        self.scroll_to(element1)

    def scroll_to_element2(self):
        element2 = self.driver.find_element(*self.locator.Myacclogo_Xpath)
        self.scroll_to(element2)
from Pages.HomePage import HomePage
from Locators.Locators import LeftBar


class LeftBarPage(HomePage):

    def __init__(self, driver):
        self.locator = LeftBar
        self.driver = driver
        super(LeftBarPage, self).__init__(driver)

    def click_dashboard(self):
        self.driver.find_element(*self.locator.dashboard_link_XPATH).click()

    def click_orders(self):
        self.driver.find_element(*self.locator.orders_link_XPATH).click()

    def click_view(self):
        self.driver.find_element(*self.locator.view_link_XPATH).click()

    # def click_invoice(self):
    #     self.driver.find_element(By.LINK_TEXT, self.invoice_link_linkText).click()

    def click_Downloads(self):
        self.driver.find_element(*self.locator.Downloads_link_linkText).click()

    def click_Browse(self):
        self.driver.find_element(*self.locator.Browse_link_XPATH).click()

    def click_cart(self):
        self.driver.find_element(*self.locator.cartclick_link_XPATH).click()

    def click_addcart(self):
        self.driver.find_element(*self.locator.addcart_XPATH).click()

    def click_Addresses(self):
        self.driver.find_element(*self.locator.Addresses_link_linkText).click()

    def click_Account(self):
        self.driver.find_element(*self.locator.Account_link_linkText).click()

    def accmobilenum(self, accmobilenum):
        self.driver.find_element(*self.locator.accmobilenum_XPATH).clear()
        self.driver.find_element(*self.locator.accmobilenum_XPATH).send_keys(accmobilenum)

    def accfirstname(self, accfirstname):
        self.driver.find_element(*self.locator.accfirstname_XPATH).clear()
        self.driver.find_element(*self.locator.accfirstname_XPATH).send_keys(accfirstname)

    def acclastname(self, acclastname):
        self.driver.find_element(*self.locator.acclastname_XPATH).clear()
        self.driver.find_element(*self.locator.acclastname_XPATH).send_keys(acclastname)

    def accdisplayname(self, accdisplayname):
        self.driver.find_element(*self.locator.accdisplayname_XPATH).clear()
        self.driver.find_element(*self.locator.accdisplayname_XPATH).send_keys(accdisplayname)

    def accemailadd(self, accemailadd):
        self.driver.find_element(*self.locator.accemailadd_XPATH).clear()
        self.driver.find_element(*self.locator.accemailadd_XPATH).send_keys(accemailadd)

    def acccurrpass(self, acccurrpass):
        self.driver.find_element(*self.locator.acccurrpass_XPATH).clear()
        self.driver.find_element(*self.locator.acccurrpass_XPATH).send_keys(acccurrpass)

    def accnewpass(self, accnewpass):
        self.driver.find_element(*self.locator.accnewpass_XPATH).clear()
        self.driver.find_element(*self.locator.accnewpass_XPATH).send_keys(accnewpass)

    def accconfirmpass(self, accconfirmpass):
        self.driver.find_element(*self.locator.accconfirmpass_XPATH).clear()
        self.driver.find_element(*self.locator.accconfirmpass_XPATH).send_keys(accconfirmpass)

    def scroll_to_element3(self):
        element3 = self.driver.find_element(*self.locator.addcart_XPATH)
        self.scroll_to(element3)

    def scroll_to_element4(self):
        element4 = self.driver.find_element(*self.locator.Myacclogo_Xpath)
        self.scroll_to(element4)

    def scroll_to_element5(self):
        element5 = self.driver.find_element(*self.locator.cartclick_link_XPATH)
        self.scroll_to(element5)
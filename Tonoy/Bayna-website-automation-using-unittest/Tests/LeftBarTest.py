import time
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.LeftBarPage import LeftBarPage


class LoginTestY(BasePage):
    def test_LeftBar_navigation(self):
        tb = LeftBarPage(self.driver)
        loginPage = LoginPage(self.driver)

        # tb.scroll_to_element()

        loginPage.enter_mobilenumber("01736457478")
        time.sleep(2)

        loginPage.enter_password("Tonoy@#123")
        time.sleep(2)

        loginPage.click_login()
        time.sleep(2)

        tb.scroll_to_element4()
        tb.click_dashboard()
        tb.scroll_to_element4()
        tb.click_orders()
        tb.scroll_to_element4()
        time.sleep(3)
        tb.scroll_to_element4()
        tb.click_view()
        time.sleep(3)
        tb.scroll_to_element4()
        tb.click_Downloads()
        time.sleep(3)
        tb.click_Browse()
        time.sleep(3)

        tb.scroll_to_element5()
        tb.click_cart()
        time.sleep(3)

        tb.scroll_to_element3()
        tb.click_addcart()
        self.driver.back()
        self.driver.back()

        tb.scroll_to_element4()
        tb.click_Addresses()
        time.sleep(3)
        tb.scroll_to_element4()
        tb.click_Account()
        time.sleep(5)

        tb.accmobilenum("014554425454")
        tb.accfirstname("ghfrueihtgeirtuiwh")
        time.sleep(3)
        tb.acclastname("breueirire")
        time.sleep(3)
        tb.accdisplayname("dfdredgfbbdgf")
        time.sleep(3)
        tb.accemailadd("dfsyugfdgfsu@gmail.com")
        time.sleep(3)
        tb.acccurrpass("123456")
        time.sleep(3)
        tb.accnewpass("123456")
        tb.accconfirmpass("123456")
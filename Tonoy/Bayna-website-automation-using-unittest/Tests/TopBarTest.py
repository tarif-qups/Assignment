import time
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.TopBarPage import TopBarPage


class LoginTestU(BasePage):
    def test_topbar_navigation(self):
        tb = TopBarPage(self.driver)
        loginPage = LoginPage(self.driver)

        loginPage.enter_mobilenumber("01736457478")
        time.sleep(2)

        loginPage.enter_password("Tonoy@#123")
        time.sleep(2)

        loginPage.click_login()
        time.sleep(2)

        tb.click_home()
        tb.click_greenchicken()
        time.sleep(3)
        tb.click_orderchicken()
        time.sleep(3)
        tb.click_addorderchicken()
        time.sleep(3)
        tb.click_beef()
        time.sleep(3)

        tb.scroll_to_element1()
        time.sleep(1)
        tb.click_orderbeef()
        time.sleep(3)
        tb.click_addorderbeef()

        tb.click_avatar()
        time.sleep(3)

        tb.scroll_to_element2()
        tb.click_logout()
        time.sleep(5)

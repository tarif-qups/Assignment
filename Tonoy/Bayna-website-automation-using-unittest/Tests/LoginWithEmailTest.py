import time
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage


class LoginTest(BasePage):
    def test_login_page(self):
        loginPage = LoginPage(self.driver)

        loginPage.scroll_to_element()
        time.sleep(1)
        loginPage.click_lostpass()
        time.sleep(2)

        loginPage.lostpassemail("bdhdsdfsu@gmail.com")
        time.sleep(2)
        self.driver.back()

        loginPage.enter_mobilenumber("01736457478")
        time.sleep(2)

        loginPage.enter_password("Tonoy@#123")
        time.sleep(2)

        loginPage.click_login()
        time.sleep(2)

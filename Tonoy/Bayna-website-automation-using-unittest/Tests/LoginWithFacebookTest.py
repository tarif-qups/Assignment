import time
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage


class LoginTestF(BasePage):
    def test_login_page(self):
        loginPage = LoginPage(self.driver)

        loginPage.scroll_to_element()
        loginPage.click_fb()
        time.sleep(2)
        loginPage.enter_fbemail("rayhan@gmail.com")
        time.sleep(2)

        loginPage.enter_fbpassword("123456789")
        time.sleep(2)

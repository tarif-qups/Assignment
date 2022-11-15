import time
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage


class LoginTestR(BasePage):
    def test_login_page(self):
        loginPage = LoginPage(self.driver)

        loginPage.scroll_to_element()
        loginPage.click_Register()
        time.sleep(2)
        loginPage.regusername("Rayan")
        time.sleep(2)

        loginPage.regfirstname("TONOY")
        time.sleep(2)

        loginPage.regemailmobile("rayhan@gmail.com")
        time.sleep(2)

        loginPage.regmobile("01736451412")
        time.sleep(2)

        loginPage.regpassword("123545522")

        # loginPage.reglogin()
        time.sleep(2)

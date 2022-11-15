from Pages.HomePage import HomePage
from Locators.Locators import LogIn

class LoginPage(HomePage):
    def __init__(self, driver):
        self.locator =  LogIn
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_Register(self):
        self.find_element2(*self.locator.Register_XPATH).click()

    def regusername(self, regusername):
        self.driver.find_element(*self.locator.regusername_ID).clear()
        self.driver.find_element(*self.locator.regusername_ID).send_keys(regusername)

    def regfirstname(self, regfirstname):
        self.driver.find_element(*self.locator.regfirstname_ID).clear()
        self.driver.find_element(*self.locator.regfirstname_ID).send_keys(regfirstname)

    def regemailmobile(self, regemailmobile):
        self.driver.find_element(*self.locator.regemailmobile_ID).clear()
        self.driver.find_element(*self.locator.regemailmobile_ID).send_keys(regemailmobile)

    def regmobile(self, regmobile):
        self.driver.find_element(*self.locator.regmobile_ID).clear()
        self.driver.find_element(*self.locator.regmobile_ID).send_keys(regmobile)

    def regpassword(self, regpassword):
        self.driver.find_element(*self.locator.regpassword_ID).clear()
        self.driver.find_element(*self.locator.regpassword_ID).send_keys(regpassword)

    def reglogin(self):
        self.driver.find_element(*self.locator.reglogin_XPATH).click()

    # login with facebook  create ALL FUNCTIONS
    def click_fb(self):
        self.driver.find_element(*self.locator.fb_XPATH).click()

    def enter_fbemail(self, fbemail):
        self.driver.find_element(*self.locator.fbemail_XPATH).clear()
        self.driver.find_element(*self.locator.fbemail_XPATH).send_keys(fbemail)

    def enter_fbpassword(self, fbpassword):
        self.driver.find_element(*self.locator.fbpassword_XPATH).clear()
        self.driver.find_element(*self.locator.fbpassword_XPATH).send_keys(fbpassword)

    # forget password create ALL FUNCTIONS
    def click_lostpass(self):
        self.driver.find_element(*self.locator.lostpass_XPATH).click()

    def lostpassemail(self, lostpassemail):
        self.driver.find_element(*self.locator.lostpassemail_XPATH).clear()
        self.driver.find_element(*self.locator.lostpassemail_XPATH).send_keys(lostpassemail)

    # login page create ALL FUNCTIONS
    def enter_mobilenumber(self, mobilenumber):
        self.driver.find_element(*self.locator.mobilenumber_textbox_XPATH).clear()
        self.driver.find_element(*self.locator.mobilenumber_textbox_XPATH).send_keys(mobilenumber)

    def enter_password(self, password):
        self.driver.find_element(*self.locator.password_textbox_XPATH).clear()
        self.driver.find_element(*self.locator.password_textbox_XPATH).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.locator.login_button_XPATH).click()

    def scroll_to_element(self):
        element = self.driver.find_element(*self.locator.loginlogo_XPATH)
        self.scroll_to(element)


from selenium.webdriver.common.by import By


class LogIn():
    # login_registor_page objects
    Register_XPATH = (By.XPATH, "//a[normalize-space()='Register']")
    regusername_ID = (By.ID, "reg_username")
    regfirstname_ID = (By.ID, "reg_billing_first_name")
    regemailmobile_ID = (By.ID, "reg_email")
    regmobile_ID = (By.ID, "secondmailormobile")
    regpassword_ID = (By.ID, "reg_password")
    reglogin_XPATH = (By.XPATH, "//a[normalize-space()='Login']")

    # login with facebook  create cobjects

    fb_XPATH = (By.XPATH, "//a[normalize-space()='Facebook']")
    fbemail_XPATH = (By.XPATH, "//input[@id='email']")
    fbpassword_XPATH = (By.XPATH, "//input[@id='pass']")

    # forget password create objects
    loginlogo_XPATH = (By.XPATH, "//h2[normalize-space()='Login']")
    lostpass_XPATH = (By.XPATH, "//a[normalize-space()='Lost your password?']")
    lostpassemail_XPATH = (By.XPATH, "//input[@id='user_login']")

    # login page create objects
    mobilenumber_textbox_XPATH = (By.XPATH, "//input[@id='username']")
    password_textbox_XPATH = (By.XPATH, "//input[@id='password']")
    login_button_XPATH = (By.XPATH, "//button[normalize-space()='Log in']")


class LeftBar():
    # # home page leftbar create objects
    dashboard_link_XPATH = (By.XPATH, "//nav[@class='woocommerce-MyAccount-navigation']//a[normalize-space()='Dashboard']")
    orders_link_XPATH = (By.XPATH, "//div[@class='orders-link']//a[normalize-space()='Orders']")
    view_link_XPATH = (By.XPATH, "//a[normalize-space()='#22420']")
    # invoice_link_linkText = "Invoice"
    Downloads_link_linkText = (By.LINK_TEXT, "Downloads")
    Browse_link_XPATH = (By.XPATH, "//a[normalize-space()='Browse products']")
    cartclick_link_XPATH = (By.XPATH, "//a[@class='product-image-link']//img[@alt='aloo puri price in Bangladesh']")
    addcart_XPATH = (By.XPATH, "//div[@class='summary-inner']//button[@name='add-to-cart'][normalize-space()='Add to cart']")
    Addresses_link_linkText = (By.LINK_TEXT, "Addresses")
    Account_link_linkText = (By.LINK_TEXT, "Account details")
    accmobilenum_XPATH = (By.XPATH, "//input[@id='username']")
    accfirstname_XPATH = (By.XPATH, "//input[@id='account_first_name']")
    acclastname_XPATH = (By.XPATH, "//input[@id='account_last_name']")
    accdisplayname_XPATH = (By.XPATH, "// input[ @ id = 'account_display_name']")
    accemailadd_XPATH = (By.XPATH, "//input[@id='account_email']")
    acccurrpass_XPATH = (By.XPATH, "//input[@id='password_current']")
    accnewpass_XPATH = (By.XPATH, "//input[@id='password_1']")
    accconfirmpass_XPATH = (By.XPATH, "//input[@id='password_2']")
    Myacclogo_Xpath = (By.XPATH, "//h3[normalize-space()='My account']")


class TopBar():
    # HOMEPAGE CREATE OBJECTS
    home_XPATH = (By.XPATH, "//div[@class='whb-flex-row whb-header-bottom-inner']//span[@class='nav-link-text'][normalize-space()='Home']")

    greenchicken_XPATH = (By.XPATH, "//div[@class='whb-flex-row whb-header-bottom-inner']//span[@class='nav-link-text'][normalize-space()='Green Chicken']")
    orderchicken_XPATH = (By.XPATH, "//div[contains(@class,'type-product post-17626 status-publish instock product_cat-green-chicken has-post-thumbnail sale taxable shipping-taxable purchasable product-type-simple')]//img[contains(@class,'attachment-woocommerce_thumbnail size-woocommerce_thumbnail')]")
    addorderchicken_XPATH = (By.XPATH, "//div[@class='summary-inner']//button[@name='add-to-cart'][normalize-space()='Add to cart']")

    beef_XPATH = (By.XPATH, "//div[@class='whb-flex-row whb-header-bottom-inner']//span[@class='nav-link-text'][normalize-space()='Beef']")
    orderbeef_XPATH = (By.XPATH, "//div[@role='main']//div[1]//div[1]//div[1]//a[1]//img[1]")
    addorderbeef_XPATH = (By.XPATH, "//div[@class='summary-inner']//button[@name='add-to-cart'][normalize-space()='Add to cart']")

    avatar_XPATH = (By.XPATH, "//header[contains(@class,'whb-header whb-sticky-shadow whb-scroll-slide whb-sticky-clone whb-hide-on-scroll')]//div[contains(@class,'wd-design-1 wd-account-style-icon')]//span[contains(@class,'wd-tools-icon')]")
    Myacclogo_Xpath =(By.XPATH, "//h3[normalize-space()='My account']")
    logout_link_XPATH = (By.XPATH, "//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']//a[contains(text(),'Logout')]")









import unittest
from unittest import runner

from Tests.LoginWithEmailTest import LoginTest
from Tests.LoginWithFacebookTest import LoginTestF
from Tests.SignupWithRegister import LoginTestR
from Tests.TopBarTest import LoginTestU
from Tests.LeftBarTest import LoginTestY


login_email = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
login_facebook = unittest.TestLoader().loadTestsFromTestCase(LoginTestF)
signup_reg = unittest.TestLoader().loadTestsFromTestCase(LoginTestR)
test_TopBar = unittest.TestLoader().loadTestsFromTestCase(LoginTestU)
test_LeftBar = unittest.TestLoader().loadTestsFromTestCase(LoginTestY)

test_suite = unittest.TestSuite([login_email, login_facebook,  signup_reg, test_TopBar, test_LeftBar])
unittest.TextTestRunner().run(test_suite)

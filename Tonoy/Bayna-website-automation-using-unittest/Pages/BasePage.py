import time
import unittest

# from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class BasePage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # serv_obj = Service(executable_path=ChromeDriverManager().install())
        # cls.driver = webdriver.Chrome(service=serv_obj)
        # serv_obj = Service(executable_path="C:\Users\\USER\PycharmProjects\\Quality UP Services\\python-selenium-unittest-pom-master-bayna store\\Driver\\chromedriver.exe")
        # cls.driver = webdriver.Chrome(Service=serv_obj)
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\Quality UP Services\\python-selenium-unittest-pom-master-bayna store\\Driver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://bayna.store/my-account/")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")


if __name__ == "__main__":
    unittest.main()

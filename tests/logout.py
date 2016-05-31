from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest, time, re
from res import page 


class logout(unittest.TestCase):
    """test class to test the logout feature"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.schibsted.cl/"
        driver = self.driver
        driver.get(self.base_url + "testqa/index.php")
        login = page.LoginPage(self.driver)
        login.enter_user('test')
        login.enter_password('123123')
        login.click_submit_button()
        Login_Page = page.LoginPage(self.driver)
        assert Login_Page.is_successful_login, "User or password is not valid."

    def test_HappyPath(self):
        logout = page.SearchResultsPage(self.driver)
        logout.click_logout_button()
        Login_Page = page.LoginPage(self.driver)
        assert Login_Page.is_at_homescreen 

    def tearDown(self):
         self.driver.close()

if __name__ == "__main__":
     unittest.main()
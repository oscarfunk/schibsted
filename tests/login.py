from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest, time, re
from res import page


class login(unittest.TestCase):
    """test class to test the login feature"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "http://www.schibsted.cl/"
        self.bad_pswd = "User or password is not valid." 
        driver = self.driver
        driver.get(self.base_url + "testqa/index.php")

    def test_HappyPath(self):
        login = page.LoginPage(self.driver)
        login.enter_user('test')
        login.enter_password('123123')
        login.click_submit_button()
        Login_Page = page.LoginPage(self.driver)
        assert Login_Page.is_successful_login, "User or password is not valid."
        self.driver.save_screenshot('C:\\schibsted\\results\\screenshots\\test_HappyPath.png')

#     def test_Invalid_Password(self):
#         login = page.LoginPage(self.driver)
#         login.enter_user('test')
#         login.enter_password('123126')
#         login.click_submit_button()
#         Login_Page = page.LoginPage(self.driver)
#         assert Login_Page.is_failed_login

#     def test_Invalid_User(self):
#         login = page.LoginPage(self.driver)
#         login.enter_user('invalid')
#         login.enter_password('123126')
#         login.click_submit_button()
#         Login_Page = page.LoginPage(self.driver)
#         assert Login_Page.is_failed_login

#     def test_Valid_User_no_Password(self):
#         login = page.LoginPage(self.driver)
#         login.enter_user('test')
#         login.click_submit_button()
#         Login_Page = page.LoginPage(self.driver)
#         assert Login_Page.is_failed_login

#     def test_No_User(self):
#         login = page.LoginPage(self.driver)
#         login.enter_password('123456')
#         login.click_submit_button()
#         Login_Page = page.LoginPage(self.driver)
#         assert Login_Page.is_failed_login

#     def test_No_Input(self):
#         login = page.LoginPage(self.driver)
#         login.click_submit_button()
#         Login_Page = page.LoginPage(self.driver)
#         assert Login_Page.is_failed_login

#     def tearDown(self):
#          self.driver.close()

if __name__ == "__main__":
     unittest.main()
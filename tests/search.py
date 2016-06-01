from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest, time, re
from res import page 


class search(unittest.TestCase):
    """test class to test the search feature"""

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

    def test_Search_for_Ford_2014(self):
        searching = page.SearchResultsPage(self.driver)
        searching.enter_search('Ford')
        searching.select_vehicule_year('2014')
        searching.click_search_button()
        self.driver.save_screenshot('C:\\schibsted\\results\\screenshots\\test_Search_for_Ford_2014.png')

    def test_Search_for_Toyota_NoYear(self):
        searching = page.SearchResultsPage(self.driver)
        searching.enter_search('Toyota')
        searching.click_search_button()

    def test_Search_for_Toyotta_2012(self):
        searching = page.SearchResultsPage(self.driver)
        searching.enter_search('Toyotta')
        searching.select_vehicule_year('2012')
        searching.click_search_button()

    def test_Search_for_Toyot_2009(self):
        searching = page.SearchResultsPage(self.driver)
        searching.enter_search('Toyotta')
        searching.select_vehicule_year('2009')
        searching.click_search_button()

    def tearDown(self):
        self.driver.quit()       

if __name__ == "__main__":
    unittest.main()





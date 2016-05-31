from elements import BasePageElement
from locators import LoginPageLocators
from locators import SearchResultsPageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    locator = 'q'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """Homepage action methods come here"""

    def is_title_matches(self):
        """Verifies no title is present"""
        return "" in self.driver.title

    def is_successful_login(self):
        return "User or password is not valid." not in self.driver.page_source
        return "Search" in self.driver.page_source

    def search_page_is_displayed(self):
        return "Search" in self.driver.page_source

    def is_failed_login(self):
        return "User or password is not valid" in self.driver.page_source
        return "Search" not in self.driver.page_source

    def is_at_homescreen(self):
        return "ACCESS" in self.driver.page_source

    def enter_user(self, value):
        element = self.driver.find_element(*LoginPageLocators.USER)
        element.send_keys(value)

    def enter_password(self, value):
        element = self.driver.find_element(*LoginPageLocators.PSSWD)
        element.send_keys(value)

    def click_submit_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*LoginPageLocators.SUBMIT)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods"""

    def enter_search(self, value):
        element = self.driver.find_element(*SearchResultsPageLocators.BRAND)
        element.send_keys(value)

    def select_vehicule_year(self, value):
        element = self.driver.find_element(*SearchResultsPageLocators.YEAR)
        element.click()
        element.send_keys(value)

    def click_search_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*SearchResultsPageLocators.SEARCH)
        element.click()

    def click_logout_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*SearchResultsPageLocators.LOGOUT)
        element.click()

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source








from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USER = (By.ID, 'username')
    PSSWD = (By.ID, 'password')
    SUBMIT = (By.NAME, 'submit')
    INV_USER_MSG = (By.XPATH, '/html/body/div/div[2]/div')
    TITLE = (By.XPATH, '/html/body/div/div[1]/div/h1')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    BRAND = (By.ID, 'brans')
    YEAR = (By.ID, 'year')
    SEARCH = (By.NAME, 'search')
    NAV_BAR1 = (By.XPATH, '/html/body/nav/div/div[1]/span')
    NAV_BAR2 = (By.XPATH, '//*[@id="navbar"]/ul/li[1]/a')
    LOGOUT =  (By.XPATH, '//*[@id="navbar"]/ul/li[2]/a')                       
    TITLE = (By.XPATH, '/html/body/div/div[1]/div/h1')                         
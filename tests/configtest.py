"""This is a set up method that contains all the generic requirements for all pages

    -- The ChromeDriver provides capabilities for navigating to web pages, user input,
        JavaScript execution, and more.
    -- The headless option is a boolean that enables and disables running the tests in headless mode
    -- The Implicit Wait is used to tell the web driver to wait for a certain amount of time in
    seconds before it throws a "No Such Element Exception".
    -- The maximize window is used to maximize the browser window size

    This method will run before every test method.
"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def setup():
    """This method runs before every test method."""

    # Run tests in Headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome_prefs = {}
    options.experimental_options["prefs"] = chrome_prefs
    
    driver = webdriver.Chrome()  

    driver.implicitly_wait(20)
    driver.maximize_window()
    
    return driver
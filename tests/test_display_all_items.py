from selenium import webdriver
from page_objects.home_page import HomePage
from utilities.custom_logger import LogGen
from tests.configtest import setup


logger = LogGen.loggen()
class TestFunctionality:
    def test_display_all_items(self, setup):
        # Initializing chrome WebDriver
        self.driver = setup
        self.driver.get("https://juice-shop.herokuapp.com/#/")
        
        logger.info("*************Test Cases running**********************")

        try:
            # Creating an instance of the HomePage
            home_page = HomePage(self.driver)

            # Scroll to the bottom of the page
            home_page.scroll_to_bottom()

            # Change items per page to the maximum value
            home_page.change_items_per_page_to_max()

            # Verify all items are displayed
            item_count = home_page.get_item_count()
            assert item_count == 24, f"Expected 24 items, but found {item_count}" 

            print("Test Passed: All items are displayed on the home page.")

        finally:
            driver.quit()
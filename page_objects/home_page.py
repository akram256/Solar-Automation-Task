from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.items_per_page_dropdown = (By.CSS_SELECTOR, "mat-select[aria-label='Items per page']")
        self.max_items_option = (By.XPATH, "//mat-option[contains(text(), '24')]")  
        self.items_grid = (By.CLASS_NAME, "mat-grid-tile")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def change_items_per_page_to_max(self):
        # Click on the dropdown
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.items_per_page_dropdown)
        ).click()
        # Select the maximum items per page
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.max_items_option)
        ).click()

    def get_item_count(self):
        # Wait for all items to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.items_grid)
        )
        return len(self.driver.find_elements(*self.items_grid))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.increase_quantity_buttons = (By.CSS_SELECTOR, "button[aria-label='Increase quantity']")
        self.delete_product_buttons = (By.CSS_SELECTOR, "button[aria-label='Remove']")
        self.total_price = (By.CSS_SELECTOR, "td.mat-footer-cell.mat-column-price")

    def increase_product_quantity(self, index=0):
        increase_buttons = self.driver.find_elements(*self.increase_quantity_buttons)
        increase_buttons[index].click()

    def delete_product(self, index=0):
        delete_buttons = self.driver.find_elements(*self.delete_product_buttons)
        delete_buttons[index].click()

    def get_total_price(self):
        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_price)
        )
        return float(total_price_element.text.replace("$", ""))
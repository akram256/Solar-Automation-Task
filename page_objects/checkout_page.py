from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.add_address_button = (By.ID, "addAddress")
        self.continue_button = (By.CSS_SELECTOR, "button[aria-label='Proceed to payment']")
        self.add_card_button = (By.CSS_SELECTOR, "button[aria-label='Add a credit or debit card']")
        self.card_number_field = (By.ID, "mat-input-0")
        self.expiry_field = (By.ID, "mat-input-1")
        self.card_code_field = (By.ID, "mat-input-2")
        self.submit_card_button = (By.ID, "submitButton")
        self.wallet_balance = (By.CSS_SELECTOR, ".mat-cell.mat-column-Balance")
        self.place_order_button = (By.ID, "checkoutButton")

    def add_address(self, address_details):
        self.driver.find_element(*self.add_address_button).click()

    def select_delivery_method(self):
        self.driver.find_element(By.CSS_SELECTOR, "mat-radio-button").click()
        self.driver.find_element(*self.continue_button).click()

    def add_credit_card(self, card_number, expiry_date, card_code):
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        self.driver.find_element(*self.expiry_field).send_keys(expiry_date)
        self.driver.find_element(*self.card_code_field).send_keys(card_code)
        self.driver.find_element(*self.submit_card_button).click()

    def assert_wallet_empty(self):
        balance = float(self.driver.find_element(*self.wallet_balance).text.replace("$", ""))
        assert balance == 0, "Wallet balance is not zero."

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

        # Locators for tasks
        # Task 1: Items per page
        self.items_per_page_dropdown = (By.CSS_SELECTOR, "mat-select[aria-label='Items per page']")
        self.max_items_option = (By.XPATH, "//mat-option[contains(text(), '24')]")
        self.items_grid = (By.CLASS_NAME, "mat-grid-tile")

        # Task 2: Product popup
        self.first_product = (By.XPATH, "//mat-card[contains(., 'Apple Juice')]")
        self.popup = (By.CLASS_NAME, "cdk-overlay-container")
        self.product_image = (By.CSS_SELECTOR, ".mat-dialog-content img")
        self.review_button = (By.CSS_SELECTOR, "button[aria-label='Expand for reviews']")
        self.close_button = (By.CSS_SELECTOR, "button[aria-label='Close Dialog']")

        # Task 3: Cart functionality
        self.product_cards = (By.CSS_SELECTOR, "mat-card")  # Select all product cards
        self.add_to_cart_buttons = (By.CSS_SELECTOR, "button[aria-label='Add to Basket']")
        self.cart_number = (By.CSS_SELECTOR, "span[class='fa-layers-counter']")
        self.success_popup = (By.CLASS_NAME, "mat-simple-snackbar")
        self.cart_button = (By.CSS_SELECTOR, "button[aria-label='Show the shopping cart']")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def change_items_per_page_to_max(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.items_per_page_dropdown)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.max_items_option)
        ).click()

    def get_item_count(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.items_grid)
        )
        return len(self.driver.find_elements(*self.items_grid))

    def click_first_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_product)
        ).click()

    def is_popup_displayed(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.popup)
        )
        return self.driver.find_element(*self.popup).is_displayed()

    def is_product_image_displayed(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.product_image)
        )
        return self.driver.find_element(*self.product_image).is_displayed()

    def expand_reviews(self):
        review_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.review_button)
        )
        if review_button:
            review_button.click()
        return True

    def close_product_form(self):
        WebDriverWait(self.driver, 2)
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_button)
        )
        close_button.click()

    def add_products_to_cart(self, num_products=5):
        products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.product_cards)
        )
        for i in range(min(num_products, len(products))):
            add_button = products[i].find_element(*self.add_to_cart_buttons)
            add_button.click()

            # Wait for the success popup to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.success_popup)
            )
            assert "added to your basket" in self.driver.find_element(*self.success_popup).text

    def assert_cart_number(self, expected_number):
        cart_number = int(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cart_number)
        ).text)
        assert cart_number == expected_number, f"Expected cart number {expected_number}, but got {cart_number}."

    def navigate_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        ).click()

# class RegistrationPage(BasePage):
#     def __init__(self, driver):
#         self.driver = driver
#         self.email_field = (By.ID, "emailControl")
#         self.password_field = (By.ID, "passwordControl")
#         self.repeat_password_field = (By.ID, "repeatPasswordControl")
#         self.security_question_dropdown = (By.CSS_SELECTOR, "mat-select[formcontrolname='securityQuestion']")
#         self.security_question_option = (By.XPATH, "//mat-option/span[text()='Your favorite book?']")  # Example option
#         self.security_answer_field = (By.ID, "securityAnswerControl")
#         self.show_password_advice = (By.CSS_SELECTOR, "button[aria-label='Show password advice']")
#         self.register_button = (By.ID, "registerButton")
#         self.validation_messages = (By.CSS_SELECTOR, ".mat-error")
#         self.success_message = (By.CSS_SELECTOR, "simple-snack-bar span")

#     def navigate_to_registration_page(self):
#         self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Show Account Menu']").click()
#         self.driver.find_element(By.ID, "navbarLoginButton").click()
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "newCustomerLink"))
#         ).click()

#     def assert_validation_messages(self):
#         self.driver.find_element(*self.email_field).click()
#         self.driver.find_element(*self.password_field).click()
#         self.driver.find_element(*self.repeat_password_field).click()
#         self.driver.find_element(*self.security_answer_field).click()
#         validation_elements = self.driver.find_elements(*self.validation_messages)
#         return [message.text for message in validation_elements]

#     def fill_registration_form(self, email, password, security_answer):
#         self.driver.find_element(*self.email_field).send_keys(email)
#         self.driver.find_element(*self.password_field).send_keys(password)
#         self.driver.find_element(*self.repeat_password_field).send_keys(password)
#         self.driver.find_element(*self.security_question_dropdown).click()
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(self.security_question_option)
#         ).click()
#         self.driver.find_element(*self.security_answer_field).send_keys(security_answer)
#         self.driver.find_element(*self.show_password_advice).click()
#         self.driver.find_element(*self.register_button).click()

#     def get_success_message(self):
#         return WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located(self.success_message)
#         ).text

# class CartPage(BasePage):
#     def __init__(self, driver):
#         self.driver = driver
#         self.increase_quantity_buttons = (By.CSS_SELECTOR, "button[aria-label='Increase quantity']")
#         self.delete_product_buttons = (By.CSS_SELECTOR, "button[aria-label='Remove']")
#         self.total_price = (By.CSS_SELECTOR, "td.mat-footer-cell.mat-column-price")

#     def increase_product_quantity(self, index=0):
#         increase_buttons = self.driver.find_elements(*self.increase_quantity_buttons)
#         increase_buttons[index].click()

#     def delete_product(self, index=0):
#         delete_buttons = self.driver.find_elements(*self.delete_product_buttons)
#         delete_buttons[index].click()

#     def get_total_price(self):
#         total_price_element = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located(self.total_price)
#         )
#         return float(total_price_element.text.replace("$", ""))

# class CheckoutPage(BasePage):
#     def __init__(self, driver):
#         self.driver = driver
#         self.add_address_button = (By.ID, "addAddress")
#         self.continue_button = (By.CSS_SELECTOR, "button[aria-label='Proceed to payment']")
#         self.add_card_button = (By.CSS_SELECTOR, "button[aria-label='Add a credit or debit card']")
#         self.card_number_field = (By.ID, "mat-input-0")
#         self.expiry_field = (By.ID, "mat-input-1")
#         self.card_code_field = (By.ID, "mat-input-2")
#         self.submit_card_button = (By.ID, "submitButton")
#         self.wallet_balance = (By.CSS_SELECTOR, ".mat-cell.mat-column-Balance")
#         self.place_order_button = (By.ID, "checkoutButton")

#     def add_address(self, address_details):
#         self.driver.find_element(*self.add_address_button).click()

#     def select_delivery_method(self):
#         self.driver.find_element(By.CSS_SELECTOR, "mat-radio-button").click()
#         self.driver.find_element(*self.continue_button).click()

#     def add_credit_card(self, card_number, expiry_date, card_code):
#         self.driver.find_element(*self.add_card_button).click()
#         self.driver.find_element(*self.card_number_field).send_keys(card_number)
#         self.driver.find_element(*self.expiry_field).send_keys(expiry_date)
#         self.driver.find_element(*self.card_code_field).send_keys(card_code)
#         self.driver.find_element(*self.submit_card_button).click()

#     def assert_wallet_empty(self):
#         balance = float(self.driver.find_element(*self.wallet_balance).text.replace("$", ""))
#         assert balance == 0, "Wallet balance is not zero."

#     def place_order(self):
#         self.driver.find_element(*self.place_order_button).click()

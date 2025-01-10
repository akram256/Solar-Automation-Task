from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from page_objects.home_page import HomePage
from page_objects.registration_page import RegistrationPage
from utilities.custom_logger import LogGen
from tests.configtest import setup
import random
import string

logger = LogGen.loggen()

class TestFunctionality:
    @staticmethod
    def generate_random_email():
        return f"user_{random.randint(1000, 9999)}@test.com"

    @staticmethod
    def generate_random_password():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

     @staticmethod
    def generate_random_card_info():
        card_number = "4111111111111111"  # Example valid card number
        expiry_date = "12/26"
        card_code = "123"
        return card_number, expiry_date, card_code


    def test_display_all_items(self, setup):
        self.driver = setup
        self.driver.get("https://juice-shop.herokuapp.com/#/")

        logger.info("*************Test Cases running**********************")

        try:
            home_page = HomePage(self.driver)
            home_page.scroll_to_bottom()
            home_page.change_items_per_page_to_max()
            item_count = home_page.get_item_count()
            assert item_count == 24, f"Expected 24 items, but found {item_count}"
            print("Test Passed: All items are displayed on the home page.")

        finally:
            self.driver.quit()

    def test_verify_apple_juice_popup(self, setup):
        self.driver = setup
        self.driver.maximize_window()

        try:
            self.driver.get("https://juice-shop.herokuapp.com/#/")
            home_page = HomePage(self.driver)
            home_page.click_first_product()
            assert home_page.is_popup_displayed(), "Popup did not appear."
            assert home_page.is_product_image_displayed(), "Product image is missing in the popup."
            if home_page.expand_reviews():
                print("Review expanded successfully.")
            home_page.close_product_form()
            print("Test Passed: Popup and product image are verified for 'Apple Juice'.")

        finally:
            self.driver.quit()

    def test_user_registration_and_login(self, setup):
        self.driver = setup
        self.driver.get("https://juice-shop.herokuapp.com/#/")
        self.driver.maximize_window()

        logger.info("************* Running User Registration and Login Test *************")

        try:
            registration_page = RegistrationPage(self.driver)
            registration_page.navigate_to_registration_page()

            # Assert validation messages by leaving fields empty
            validation_messages = registration_page.assert_validation_messages()
            assert "Please provide an email address." in validation_messages, "Email validation message is missing."
            assert "Please provide a password." in validation_messages, "Password validation message is missing."
            assert "Please repeat your password." in validation_messages, "Repeat password validation message is missing."
            assert "Please provide an answer to your security question." in validation_messages, "Security answer validation message is missing."
            print("Validation messages appeared correctly.")

            # Generate test data
            email = self.generate_random_email()
            password = self.generate_random_password()
            security_answer = "TestBook"

            # Fill the registration form and submit
            registration_page.fill_registration_form(email, password, security_answer)

            # Assert the success message
            success_message = registration_page.get_success_message()
            assert "Registration completed successfully" in success_message, "Registration success message is missing."
            print("Registration successful.")

            # Assert redirection to login page and login using the registered credentials
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/login")
            )
            self.driver.find_element(By.ID, "email").send_keys(email)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.ID, "loginButton").click()

            # Verify login by checking for logout button
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "logoutButton"))
            )
            assert logout_button.is_displayed(), "Login was not successful."
            print("Login successful.")

        finally:
            self.driver.quit()

    def test_purchase_with_credit_card(self, setup):
        self.driver = setup
        self.driver.get("https://juice-shop.herokuapp.com/#/")
        logger.info("************* Test: Purchase with Credit Card *************")

        try:
            # Login to the application
            home_page = HomePage(self.driver)
            registration_page = RegistrationPage(self.driver)
            email = "test_user@example.com"  # Replace with a valid email
            password = "Test@1234"  # Replace with a valid password
            registration_page.login_user(email, password)

            # Add 5 products to the cart
            home_page.add_products_to_cart(5)

            # Assert cart number is updated to 5
            home_page.assert_cart_number(5)

            # Navigate to the cart
            home_page.navigate_to_cart()

            # Modify the cart
            cart_page = CartPage(self.driver)
            initial_total = cart_page.get_total_price()
            cart_page.increase_product_quantity()
            cart_page.delete_product()

            # Assert total price has changed
            new_total = cart_page.get_total_price()
            assert initial_total != new_total, "Total price did not change as expected."

            # Proceed to checkout
            checkout_page = CheckoutPage(self.driver)
            checkout_page.add_address({"street": "123 Test St", "city": "Test City", "zip": "12345"})
            checkout_page.select_delivery_method()

            # Add credit card
            card_number, expiry_date, card_code = self.generate_random_card_info()
            checkout_page.add_credit_card(card_number, expiry_date, card_code)

            # Assert wallet is empty and complete the purchase
            checkout_page.assert_wallet_empty()
            checkout_page.place_order()

            print("Test Passed: Purchase completed successfully.")

        finally:
            self.driver.quit()

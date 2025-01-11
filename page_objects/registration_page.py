from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "emailControl")
        self.password_field = (By.ID, "passwordControl")
        self.repeat_password_field = (By.ID, "repeatPasswordControl")
        self.security_question_dropdown = (By.CSS_SELECTOR, "mat-select[formcontrolname='securityQuestion']")
        self.security_question_option = (By.XPATH, "//mat-option/span[text()='Your favorite book?']")  # Example option
        self.security_answer_field = (By.ID, "securityAnswerControl")
        self.show_password_advice = (By.CSS_SELECTOR, "button[aria-label='Show password advice']")
        self.register_button = (By.ID, "registerButton")
        self.validation_messages = (By.CSS_SELECTOR, ".mat-error")
        self.success_message = (By.CSS_SELECTOR, "simple-snack-bar span")

    def navigate_to_registration_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Show Account Menu']").click()
        self.driver.find_element(By.ID, "navbarLoginButton").click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "newCustomerLink"))
        ).click()

    def assert_validation_messages(self):
        self.driver.find_element(*self.email_field).click()
        self.driver.find_element(*self.password_field).click()
        self.driver.find_element(*self.repeat_password_field).click()
        self.driver.find_element(*self.security_answer_field).click()
        validation_elements = self.driver.find_elements(*self.validation_messages)
        return [message.text for message in validation_elements]

    def fill_registration_form(self, email, password, security_answer):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.repeat_password_field).send_keys(password)
        self.driver.find_element(*self.security_question_dropdown).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.security_question_option)
        ).click()
        self.driver.find_element(*self.security_answer_field).send_keys(security_answer)
        self.driver.find_element(*self.show_password_advice).click()
        self.driver.find_element(*self.register_button).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.success_message)
        ).text
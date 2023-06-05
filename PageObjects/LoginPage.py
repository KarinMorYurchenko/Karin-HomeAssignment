import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Login Page Objects")
class LoginPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    @allure.step("Username Input Box")
    def username_input_box_element(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="email-input"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="email-input"]')


    @allure.step("Password Input Box")
    def password_input_box_element(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="password-input"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="password-input"]')

    @allure.step("Submit button element")
    def submit_button_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="sign-in-button"]')))

    @allure.step("Error Alert")
    def invalid_input_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="login-error"]'))).text


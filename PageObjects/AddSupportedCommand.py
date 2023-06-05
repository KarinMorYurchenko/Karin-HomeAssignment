import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Login Page Objects")
class AddSupportedCommand:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    @allure.step("Friendly Name")
    def friendly_name_input_element(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="text-input-friendly_name"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="text-input-friendly_name"]')

    @allure.step("Description")
    def description_input_element(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="text-input-description"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="text-input-description"]')

    @allure.step("Name send to device")
    def name_sent_to_device_input_element(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="text-input-name"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="text-input-name"]')

    @allure.step("Create button element")
    def create_button_element(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="create-btn"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="create-btn"]')

    @allure.step("POPUP message")
    def popup_message(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'dialogTitle-5744')))
        return self.driver.find_element(By.ID, 'dialogTitle-5744')

    @allure.step("Name send to device")
    def alert_message(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.modal-body>p')))
        return self.driver.find_element(By.CSS_SELECTOR, '.modal-body>p')

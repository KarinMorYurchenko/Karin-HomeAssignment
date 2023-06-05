import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Models Page Object")
class ModelsPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    @allure.step("Model name element")
    def model_name_element(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#cell-cell_0_model > div > div > a')))
        return self.driver.find_element(By.CSS_SELECTOR, '#cell-cell_0_model > div > div > a')

    @allure.step("Supported Commands")
    def supported_commands_element(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="location-tab-commands"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="location-tab-commands"]')

    @allure.step("Supported Commands")
    def add_command_element(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="add-command-btn"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="add-command-btn"]')



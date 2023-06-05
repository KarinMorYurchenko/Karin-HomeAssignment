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
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#cell-cell_0_model > div > div > a')))
        return self.driver.find_element(By.CSS_SELECTOR, '#cell-cell_0_model > div > div > a')

    @allure.step("Supported Commands")
    def supported_commands_element(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="location-tab-commands"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="location-tab-commands"]')

    @allure.step("Add Command Button Element")
    def add_commands_element(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.mantine-1t9xh9a.mantine-Button-label')))
        return self.driver.find_element(By.CSS_SELECTOR, 'span.mantine-1t9xh9a.mantine-Button-label')

    # @allure.step("Add Command Button Element")
    # def checkbox_element(self):
    #     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'column-checkbox-4')))
    #     return self.driver.find_element(By.ID, 'column-checkbox-4')
    #
    # @allure.step("Add Command Button Element")
    # def remove_button(self):
    #     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div:nth-child(1) > div.mantine-Group-root.mantine-1e6jinj > button > div > span.mantine-1t9xh9a.mantine-Button-label')))
    #     return self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div.mantine-Group-root.mantine-1e6jinj > button > div > span.mantine-1t9xh9a.mantine-Button-label')

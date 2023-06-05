import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Sidebar Elements")
class SideBar:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    @allure.step("Username Input Box")
    def models_side_bar_element(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="sidebar-item-sidebar.models"]')))
        return self.driver.find_element(By.CSS_SELECTOR, '[data-testid="sidebar-item-sidebar.models"]')

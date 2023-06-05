import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.LoginPage import LoginPage


@allure.epic("Login Page Objects")
class TestLoginPage:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_01_valid_login(self, driver):
        login_page = LoginPage(driver)
        # Navigate to the login page
        driver.get('https://partners.xyte.io')
        assert 'Xyte - HWaaS Platform' in driver.title
        # Fill in the login form
        login_page.username_input_box_element().send_keys('karinayurchenko@gmail.com')
        login_page.password_input_box_element().send_keys('tq5vtNdwbqnzq3Aw!')
        login_page.submit_button_element().click()


    def test_02_invalid_login(self, driver):
        login_page = LoginPage(driver)
        driver.get('https://partners.xyte.io')
        assert 'Xyte - HWaaS Platform' in driver.title
        login_page.username_input_box_element().send_keys('karinayurchenko@gmail.com')
        login_page.password_input_box_element().send_keys('tq5vtNq3Aw!')
        login_page.submit_button_element().click()
        assert login_page.invalid_input_error_message() == 'Invalid login credentials. Please try again.'


    """
    test_03_invalid_email(self,driver):
        there is no popup element or another error message for invalid email.
    """




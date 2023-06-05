import allure
import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from PageObjects.Model import ModelsPage
from PageObjects.SideBar import SideBar


@allure.epic("Login Page Objects")
class TestModels:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()


    def test_01_click_on_models(self, driver):
        login_page = LoginPage(driver)
        sidebar = SideBar(driver)
        models = ModelsPage(driver)
        driver.get('https://partners.xyte.io')
        assert 'Xyte - HWaaS Platform' in driver.title
        # Fill in the login form
        login_page.username_input_box_element().send_keys('karinayurchenko@gmail.com')
        login_page.password_input_box_element().send_keys('tq5vtNdwbqnzq3Aw!')
        login_page.submit_button_element().click()
        sidebar.models_side_bar_element().click()
        models.model_name_element().click()
        models.supported_commands_element().click()


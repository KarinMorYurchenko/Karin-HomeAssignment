import allure
import pytest
from selenium import webdriver

from PageObjects.AddSupportedCommand import AddSupportedCommand
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

    def test_01_add_valid_command_for_supported_commands(self, driver):
        login_page = LoginPage(driver)
        sidebar = SideBar(driver)
        models = ModelsPage(driver)
        add_command = AddSupportedCommand(driver)
        driver.get('https://partners.xyte.io')
        assert 'Xyte - HWaaS Platform' in driver.title
        login_page.username_input_box_element().send_keys('karinayurchenko@gmail.com')
        login_page.password_input_box_element().send_keys('tq5vtNdwbqnzq3Aw!')
        login_page.submit_button_element().click()
        sidebar.models_side_bar_element().click()
        models.model_name_element().click()
        models.supported_commands_element().click()
        models.add_commands_element().click()
        add_command.friendly_name_input_element().send_keys('QATest')
        add_command.description_input_element().send_keys('QATest')
        add_command.name_sent_to_device_input_element().send_keys('QATest')
        add_command.create_button_element().click()

    def test_02_add_invalid_command_for_supported_commands(self, driver):
        login_page = LoginPage(driver)
        sidebar = SideBar(driver)
        models = ModelsPage(driver)
        add_command = AddSupportedCommand(driver)
        driver.get('https://partners.xyte.io')
        assert 'Xyte - HWaaS Platform' in driver.title
        login_page.username_input_box_element().send_keys('karinayurchenko@gmail.com')
        login_page.password_input_box_element().send_keys('tq5vtNdwbqnzq3Aw!')
        login_page.submit_button_element().click()
        sidebar.models_side_bar_element().click()
        models.model_name_element().click()
        models.supported_commands_element().click()
        models.add_commands_element().click()
        add_command.friendly_name_input_element().send_keys('reboot')
        add_command.description_input_element().send_keys('reboot')
        add_command.name_sent_to_device_input_element().send_keys('reboot')
        add_command.create_button_element().click()
        assert 'Name has already been taken' == add_command.alert_message().text

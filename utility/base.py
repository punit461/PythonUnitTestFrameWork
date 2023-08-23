from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time
import os
from utility.config_reader import ConfigReader
from test_suites import project_directory


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.config_reader = ConfigReader()

    def locate_element(self, locator, timeout=None):
        if timeout is None:
            timeout = self.config_reader.get_timeout()

        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Element {locator} not found within {timeout} seconds.")

    def click_element(self, locator, timeout=None):
        if timeout is None:
            timeout = self.config_reader.get_timeout()

        element = self.locate_element(locator, timeout)
        element.click()

    def send_keys(self, locator, text, timeout=None):
        if timeout is None:
            timeout = self.config_reader.get_timeout()

        element = self.locate_element(locator, timeout)
        element.clear()
        element.send_keys(text)



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from Utilities import ConfigReader as cr


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.config_reader = cr.ConfigReader

    def def_timeout(self):
        timeout = self.config_reader.get_timeout
        return float(timeout)

    def locate_element(self, locator, timeout=def_timeout):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Element {locator} not found within {timeout} seconds.")

    def click_element(self, locator, timeout=def_timeout):
        element = self.locate_element(locator, timeout)
        element.click()

    def send_keys(self, locator, text, timeout=def_timeout):
        element = self.locate_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def take_screenshot(self, screenshot_name):
        timestamp = time.strftime('%Y%m%d%H%M%S')
        screenshot_path = f"Reporting/Screenshots/{screenshot_name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path

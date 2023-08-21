from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from .config_reader import ConfigReader


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.config_reader = ConfigReader()

    def locate_element(self, locator, timeout=None):
        if timeout is None:
            timeout = self.config_reader.get_timeout()

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
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

    def take_screenshot(self, screenshot_name):
        timestamp = time.strftime('%Y%m%d%H%M%S')
        screenshot_path = f"Reporting/Screenshots/{screenshot_name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path

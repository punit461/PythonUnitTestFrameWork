from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Element {locator} not found within {timeout} seconds.")

    def take_screenshot(self, screenshot_name):
        timestamp = time.strftime('%Y%m%d%H%M%S')
        screenshot_path = f"screenshots/{screenshot_name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path

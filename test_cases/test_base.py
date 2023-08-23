import unittest
from utility.driver_manager import DriverManager
from utility.config_reader import ConfigReader
from utility.custom_logger import capture_screenshot
import tracemalloc


class TestBase(unittest.TestCase):
    def setUp(self):
        tracemalloc.start()
        self.config_reader = ConfigReader()
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.get_driver()
        self.driver.maximize_window()
        self.driver.get(self.config_reader.get_baseurl())

    def tearDown(self):
        screenshot_mode = str(self.config_reader.read_ss_config())
        current_test_name = self.id().split(".")[-1]  # Get the current test method name
        # print("Current Test Case Name is ", current_test_name)
        if screenshot_mode == 'after_every_test_case':
            capture_screenshot(self, current_test_name)

        if screenshot_mode == 'on_failure' and self._outcome.errors:
            capture_screenshot(self, current_test_name)

        tracemalloc.stop()
        self.driver.close()
        self.driver.quit()

    # def addSuccess(self, test, err=None):
    #     screenshot_mode = str(self.config_reader.read_ss_config())
    #     current_test_name = self.id().split(".")[-1]  # Get the current test method name
    #
    #     if screenshot_mode == 'after_every_test_case':
    #         BC.capture_screenshot(current_test_name)
    #
    #     # Continue with the default behavior for test success
    #     super().addSuccess(test)
    #
    # def addFailure(self, test, err):
    #     screenshot_mode = str(self.config_reader.read_ss_config())
    #     current_test_name = self.id().split(".")[-1]  # Get the current test method name
    #
    #     if screenshot_mode == 'after_every_test_case':
    #         BC.capture_screenshot(current_test_name)
    #
    #     # Continue with the default behavior for test failures
    #     super().addFailure(test, err)

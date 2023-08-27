import unittest
from utility.driver_manager import DriverManager
from utility.config_reader import ConfigReader
from utility.custom_logger import capture_screenshot
from utility.test_data_reader import ReadData
import tracemalloc


class TestBase(unittest.TestCase):

    def setUp(self):
        # self._outcome = None
        self.msg_lines = ["Temp error text"]
        tracemalloc.start()
        self.config_reader = ConfigReader()
        self.driver_manager = DriverManager()
        self.read_test_data = ReadData()
        self.driver = self.driver_manager.get_driver()
        self.driver.maximize_window()
        self.driver.get(self.config_reader.get_baseurl())

    def tearDown(self):
        screenshot_mode = str(self.config_reader.get_ss_mode())
        current_test_name = self.id().split(".")[-1]  # Get the current test method name
        print(f"Test Case {current_test_name} Executed")
        if screenshot_mode == 'after_every_test_case':
            capture_screenshot(self, current_test_name)
        elif screenshot_mode == 'on_failure':
            if str(self._outcome.errors).lower().__contains__("error"):
                capture_screenshot(self, current_test_name)
            else:
                print("Test Case Passed")
        else:
            print("Screenshot Capture Mode turned off")

        tracemalloc.stop()
        self.driver.close()
        self.driver.quit()

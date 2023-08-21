import unittest
from utility.driver_manager import DriverManager
from utility.config_reader import ConfigReader
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
        tracemalloc.stop()
        self.driver.close()
        self.driver.quit()

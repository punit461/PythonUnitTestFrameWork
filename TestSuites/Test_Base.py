import unittest
from Utilities.DriverManager import DriverManager
from Utilities.ConfigReader import ConfigReader


class TestBase(unittest.TestCase):
    def setUp(self):
        self.config_reader = ConfigReader()
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.get_driver()
        self.driver.get(self.config_reader.get_baseurl())

    def tearDown(self):
        self.driver.quit()

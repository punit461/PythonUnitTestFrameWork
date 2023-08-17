from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from Utilities.ConfigReader import ConfigReader


class DriverManager:
    def __init__(self):
        self.config_reader = ConfigReader()

    def get_driver(self):
        browser_name = self.config_reader.get_browser()

        if browser_name.lower() == "chrome":
            return self._get_chrome_driver()
        elif browser_name.lower() == "firefox":
            return self._get_firefox_driver()
        elif browser_name.lower() == "edge":
            return self._get_edge_driver()
        else:
            raise Exception(f"Unsupported browser: {browser_name}")

    def _get_chrome_driver(self):
        chrome_options = ChromeOptions()

        if self.config_reader.get_browser_headless():
            chrome_options.add_argument('--headless')

        service = ChromeService(executable_path=self.config_reader.get_browser_path("chrome"))
        return webdriver.Chrome(service=service, options=chrome_options)

    def _get_firefox_driver(self):
        firefox_options = FirefoxOptions()

        if self.config_reader.get_browser_headless():
            firefox_options.add_argument('--headless')

        service = FirefoxService(executable_path=self.config_reader.get_browser_path("firefox"))
        return webdriver.Firefox(service=service, options=firefox_options)

    def _get_edge_driver(self):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True

        if self.config_reader.get_browser_headless():
            edge_options.add_argument('--headless')

        service = EdgeService(executable_path=self.config_reader.get_browser_path("edge"))
        return webdriver.Edge(service=service, options=edge_options)

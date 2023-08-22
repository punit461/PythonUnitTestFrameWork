import unittest
import HtmlTestRunner
from test_cases.test_base import TestBase
from pages.login_page_class import LoginPage
from test_cases import project_directory


class TestLoginPage(TestBase):
    def test_successful_login(self):
        username = self.config_reader.get_username()
        password = self.config_reader.get_password()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        print(self.driver.title)
        # Add assertions to verify successful login
        self.assertEqual(self.driver.title, "Dashboard / nopCommerce administration")

        # print(tracemalloc.take_snapshot().statistics('lineno'))






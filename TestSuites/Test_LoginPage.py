import tracemalloc
import unittest
from Test_Base import TestBase
from Pages.LoginPageClass import LoginPage


class TestLoginPage(TestBase):
    def test_successful_login(self):
        username = self.config_reader.get_username()
        password = self.config_reader.get_password()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        print(self.driver.title)
        # Add assertions to verify successful login
        # print(tracemalloc.take_snapshot().statistics('lineno'))


if __name__ == "__main__":
    unittest.main()

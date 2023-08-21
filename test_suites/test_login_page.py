import tracemalloc

import unittest
from test_base import TestBase
from pages.login_page_class import LoginPage
from utilities import html_test_runner


class TestLoginPage(TestBase):
    def test_successful_login(self):
        """
            This is a Login test case.
            This test case checks for Login Functionality.
            Tester: John Doe
            Report: ./reporting/html_reports/my_test_report.html
            """
        username = self.config_reader.get_username()
        password = self.config_reader.get_password()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        print(self.driver.title)
        assert self.driver.title == "Dashboard / nopCommerce administration"
        # Add assertions to verify successful login
        # print(tracemalloc.take_snapshot().statistics('lineno'))


if __name__ == "__main__":
    fp = file('./reporting/html_reports/', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Python unittest Framework Report',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    # HTMLTestRunner.main()
    unittest.main(testRunner=runner)
    # unittest.main(testRunner=HTMLTestRunner(output='.\reporting\html_reports'))


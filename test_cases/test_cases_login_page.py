from test_cases.test_base import TestBase
from pages.login_page_class import LoginPage
from pages.dashboard_page_class import DashboardPage
from test_suites import project_directory
from utility.custom_logger import logmethod


class TestLoginPage(TestBase):

    @logmethod
    def test_successful_login(self):
        print("Verify Login Functionality of NopCommerce WebApp")
        username = self.config_reader.get_username()
        password = self.config_reader.get_password()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        print("WebApp Page Title after Login -", self.driver.title)
        # Add assertions to verify successful login
        self.assertEqual(self.driver.title, "Dashboard / nopCommerce administration")

        # print(tracemalloc.take_snapshot().statistics('lineno'))

    @logmethod
    def test_failure_login(self):
        print("Verify Login Functionality of NopCommerce WebApp")
        username = self.config_reader.get_username()
        password = self.config_reader.get_password()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        print("WebApp Page Title after Login -", self.driver.title)
        # Add assertions to verify successful login
        self.assertEqual(self.driver.title, "Fail")

    @logmethod
    def test_global_search_product_attribute(self):
        print("Verify User able to perform global search")
        search_txt = self.read_test_data.read_ini(project_directory +
                                                  r"\test_data\configurations\test_data_dp_page.ini",
                                                  'global_search', "search_text_pa")
        username = self.config_reader.get_username()
        password = self.config_reader.get_password()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.do_click_on_search_send_value(search_txt)
        print("WebApp Page Title after Login -", self.driver.title)
        self.assertTrue(self.driver.title.__contains__("Product attributes"))

    @logmethod
    def test_fail_global_search_product_attribute(self):
        print("Verify User able to perform global search")
        search_txt = self.read_test_data.read_ini(project_directory +
                                                  r"\test_data\configurations\test_data_dp_page.ini",
                                                  'global_search', "search_text_pa")
        username = self.config_reader.get_username()
        password = self.config_reader.get_password()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.do_click_on_search_send_value(search_txt)
        print("WebApp Page Title after Login -", self.driver.title)
        self.assertTrue(self.driver.title.__contains__("Fail"))

from test_cases.test_base import TestBase
from pages.login_page_class import LoginPage
from pages.dashboard_page_class import DashboardPage
from pages.add_customer_page_class import CustomerPage
from test_suites import project_directory
from utility.custom_logger import logmethod
import random

class TestCustomerPage(TestBase):

    @logmethod
    def test_add_customer(self):
        print("Verify user should be able to create new customer")

        #json file name & Read the data from data file
        json_file = project_directory + r"\test_data\jsons\test_data_add_user.json"
        set_email = str(random.randint(1,100)) + self.read_test_data.read_json(json_file, "email")
        set_password = self.read_test_data.read_json(json_file, "password")
        first_name = self.read_test_data.read_json(json_file, "first_name")
        last_name = self.read_test_data.read_json(json_file, "last_name")
        gender = self.read_test_data.read_json(json_file, "gender")
        dob = self.read_test_data.read_json(json_file, "dob")
        company_name = self.read_test_data.read_json(json_file, "company_name")
        vendor = self.read_test_data.read_json(json_file, "vendor")
        comment = self.read_test_data.read_json(json_file, "comment")
        success_msg = self.read_test_data.read_json(json_file, "success_msg")

        #perform login
        username = self.config_reader.get_username()
        password = self.config_reader.get_password()
        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        customer_page = CustomerPage(self.driver)
        customer_page.click_customer_menu()
        customer_page.click_customer_submenu()
        customer_page.click_add_new()
        print("WebApp Page Title after Clicking Customers Button -", self.driver.title)
        customer_page.set_email(set_email)
        customer_page.set_password(set_password)
        customer_page.set_fname(first_name)
        customer_page.set_lname(last_name)
        customer_page.set_gender(gender)
        customer_page.set_dob(dob)
        customer_page.set_company_name(company_name)
        customer_page.set_manage_of_vendor(vendor)
        customer_page.set_admin_comment(comment)

        customer_page.click_save_btn()

        self.assertTrue(self.driver.page_source.__contains__(success_msg))
        print("Customer Added Successfully")








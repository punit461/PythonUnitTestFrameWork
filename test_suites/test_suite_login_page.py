import datetime
import unittest
from HtmlTestRunner import HTMLTestRunner
from test_cases import project_directory
from test_cases.test_cases_login_page import TestLoginPage


def login_page_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestLoginPage("test_successful_login"))
    return test_suite


if __name__ == '__main__':
    # unittest.TextTestRunner(verbosity=2).run(login_page_suite())
    # outfile = open(report_loc, 'w')
    report_loc = str(project_directory + r"\reporting\html_reports")
    runner = HTMLTestRunner(output=report_loc,
                            verbosity=2,
                            report_title='Python-Unittest-Automation-Framework',
                            descriptions='Test report')
    runner.run(login_page_suite())

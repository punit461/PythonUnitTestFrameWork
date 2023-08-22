#imports from libs
import datetime
import os
import sys
import unittest
from HtmlTestRunner import HTMLTestRunner
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#Imports of user created modules
from test_cases.test_cases_login_page import TestLoginPage
from test_suites import project_directory


def login_page_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestLoginPage("test_successful_login"))
    return test_suite


if __name__ == '__main__':
    # unittest.TextTestRunner(verbosity=2).run(login_page_suite())
    # outfile = open(report_loc, 'w')
    report_loc = str(r".\reporting\html_reports")
    print(report_loc)
    runner = HTMLTestRunner(output=report_loc,
                            verbosity=2,
                            report_title='Python-Unittest-Automation-Framework',
                            descriptions='Test report')
    if __name__ == '__main__':
        runner.run(login_page_suite())

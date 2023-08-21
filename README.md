# UI Automation Framework

Welcome to the UI Automation Framework! This framework is designed to facilitate the automation of user interface testing using Selenium and Python's unittest framework. It follows the Page Object Model (POM) design pattern for improved maintainability and readability.

## Project Structure

The project is structured as follows:

- `Configurations`: Configuration files and settings related to the automation setup.
- `Locators`: Element locators (selectors) for the application's pages.
- `Pages`: Page Object classes encapsulating elements and methods for each page.
- `Reporting`: Handles different types of reports and logs.
  - `HtmlReports`: HTML reports generated from test runs.
  - `Logs`: Log files for debugging and tracking test execution.
  - `Screenshots`: Screenshots captured during test runs.
- `TestData`: Test data that might be used by tests.
- `TestSuites`: Test suite files that group and execute tests.
- `Utilities`: Utility modules and common functions for the framework.
- `.idea`: IDE-specific settings (created by the IDE).
- `venv`: Virtual environment directory.

## Getting Started

1. Clone this repository to your local machine.
2. Set up a virtual environment in the `venv` directory.
3. Install required dependencies using `pip install -r requirements.txt`.
4. Update configuration files in the `Configurations` directory as needed.
5. Define page locators in the `Locators` directory.
6. Create Page Object classes in the `Pages` directory.
7. Organize test data in the `TestData` directory.
8. Create test suite files in the `TestSuites` directory.
9. Run tests using `python -m unittest discover TestSuites`.

## _Tools & Technologies Used_
_Python_, _Selenium_, _unittest_, _Allure_.

## Running Tests

To run the tests, navigate to the project root directory and execute the following command:

```bash
python -m unittest discover test_suites
```
## Reporting
* HTML reports can be found in the Reporting/HtmlReports directory.
* Logs are stored in the Reporting/Logs directory.
* Screenshots from test runs are saved in the Reporting/Screenshots directory.

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

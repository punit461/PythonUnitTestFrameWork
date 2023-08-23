import functools
import logging
import os
import time
from test_suites import project_directory


def setup_custom_logger(name):
    log_dir = str(project_directory + r"\reporting\logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f'{name}.log')

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


def logmethod(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = setup_custom_logger(func.__name__)
        logger.info(f"Starting test: {func.__name__}")

        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully.")
            return result
        except Exception as e:
            logger.error(f"Test {func.__name__} FAILED")
            logger.exception(e)
            raise e
        finally:
            logger.info(f"Finished test: {func.__name__}")

    return wrapper


def take_screenshot(self, screenshot_name):
    timestamp = time.strftime('%Y%m%d%H%M%S')
    screenshot_path = f"reporting/screenshots/{screenshot_name}_{timestamp}.png"
    self.driver.save_screenshot(screenshot_path)
    return screenshot_path


def capture_screenshot(self, name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f'Test_execution_{timestamp}'
    screenshot_dir = project_directory + "\\reporting\screenshots\\" + folder_name
    # screenshot_dir = os.path.join(os.getcwd(), 'reporting', 'screenshots', folder_name)
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f'{name}.png')
    # print(screenshot_path)
    self.driver.save_screenshot(screenshot_path)

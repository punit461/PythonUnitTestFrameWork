from selenium.webdriver.common.by import By


class LPLocators:
    """
    In the Beginning define what type of element it is
    for Example -> lnk - Link, btn - button, txt - textbox,
    rd - radiobutton, lst - List, drpmgr - drop down manager
    """
    txt_username = (By.ID, 'Email')
    txt_password = (By.ID, 'Password')
    btn_login = (By.XPATH, "//button[text()='Log in']")

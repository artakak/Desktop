from selenium.webdriver.common.by import By
from base_page_object import BasePage


class LoginPage(BasePage):
    locator_dictionary = {
        "login_button": (By.XPATH, "//button[@type='submit']"),
        "username_field": (By.NAME, 'email'),
        "password_field": (By.NAME, 'password'),
        "required_field": (By.XPATH, "//span[contains(.,'This is a required field')]"),
        "wrong_field": (By.XPATH, "//span[contains(.,'Cannot login into the application"
                                  " (wrong login, password or missing user)')]"),
        "captcha_field": (By.XPATH, "//span[contains(.,'Access is temporarily disabled."
                                    " To unlock, enter a valid username, password, and characters from the image')]"),
        "forgot_link": (By.XPATH, "//span[contains(.,'Forgot password?')]"),
        "change_lng_link": (By.XPATH, "//span[contains(.,'Russian')]")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

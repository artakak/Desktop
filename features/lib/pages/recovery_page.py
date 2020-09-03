from selenium.webdriver.common.by import By
from base_page_object import BasePage


class RecoveryPage(BasePage):
    locator_dictionary = {
        "email_field": (By.NAME, 'email'),
        "password_field": (By.NAME, 'password'),
        "repeat_field": (By.NAME, 'repeat'),
        "send_button": (By.XPATH, "//button[@type='submit']"),
        "same_message": (By.XPATH, "//span[contains(.,'Entered password is the same')]")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    class SuccessMsg(BasePage):
        locator_dictionary = {
            "success_message": (By.XPATH, "//span[contains(.,'We have sent you a message to your personal email."
                                          " Please, click on the link in it and follow the further instructions"
                                          " to reset your password.')]")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

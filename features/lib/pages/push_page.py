from selenium.webdriver.common.by import By
from base_page_object import BasePage


class PushPage(BasePage):
    locator_dictionary = {
        "enable_button": (By.XPATH, "//button[@type='button' and span='Enable']")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

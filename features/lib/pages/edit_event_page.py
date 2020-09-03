from selenium.webdriver.common.by import By
from base_page_object import BasePage


class EditEventPage(BasePage):
    locator_dictionary = {
        "edit_event_header": (By.XPATH, 'new UiSelector().text("Edit event")'),
        "save_event_button": (By.XPATH, "//button[.='Save']")
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

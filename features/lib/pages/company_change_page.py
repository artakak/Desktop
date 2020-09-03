from appium.webdriver.common.mobileby import MobileBy as By
from base_page_object import BasePage


class CompanyChangePage(BasePage):
    locator_dictionary = {
        "company_field": (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("company")'),
        "next_button": (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NEXT")'),
        "support_button": (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SUPPORT")'),
        "compose_action": (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Compose")'),
        "company_text": (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type your Experium web address")')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def compose_to_support(self):
        self.find_element(*self.locator_dictionary['support_button']).click()
        self.find_element(*self.locator_dictionary['compose_action'])

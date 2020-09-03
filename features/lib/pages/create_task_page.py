import time
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from nose.tools import assert_equal, assert_true


class CreateTaskPage(BasePage):
    locator_dictionary = {
        "create_task_header": (By.XPATH, "//span[.='Set a task']"),
        "task_name_field": (By.XPATH, "//input[@name='description']"),
        "low_field": (By.XPATH, "//input[@value='3']"),
        "medium_field": (By.XPATH, "//input[@value='2']"),
        "high_field": (By.XPATH, "//input[@value='1']"),
        "select_done": (By.XPATH, "//div[@class='ant-modal-body']//button[@role='switch']"),
        "save_button": (By.XPATH, "//button[contains(.,'Save')]")
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def create_task(self, value):
        time.sleep(5)
        self.task_name_field.send_keys("Task_%s" % value)
        if value == "low":
            self.low_field.click()
        elif value == "medium":
            self.medium_field.click()
        elif value == "high":
            self.high_field.click()
            self.select_done.click()
        self.save_button.click()
        time.sleep(5)
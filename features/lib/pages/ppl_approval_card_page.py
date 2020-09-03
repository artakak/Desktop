#!-*-coding:utf-8-*-
import time
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from conf import new_request_conf as request
from nose.tools import assert_equal, assert_true


class PplApprovalCardPage(BasePage):
    locator_dictionary = {
        "approval_header": (By.XPATH, "//span[@class='title' and .='First People Incompany']"),
        "citizenship_field": (By.XPATH, "//dt[.='Citizenship']"),
        "citizenship_value": (By.XPATH, u"//dd[.='Бельгия']"),
        "age_field": (By.XPATH, "//dt[.='Age']"),
        "age_value": (By.XPATH, "//dd[contains(.,'19') and contains(.,'12.12.1999')]"),
        "last_empl_field": (By.XPATH, "//dt[.='Last Employer']"),
        "last_empl_value": (By.XPATH, "//dd[contains(.,'AutotestCo (Tdol), 07.2018') and contains(.,'till now.')]"),
        "languafe_field": (By.XPATH, "//dt[.='Foreign languages']"),
        "language_value": (By.XPATH, u"//dd[contains(.,'английский') and contains(.,'Базовый')]"),
        "status_field": (By.XPATH, "//div[contains(.,'Status') and contains(.,'On approval')]"),
        "type_field": (By.XPATH, "//span[.='Interview with line manager']"),
        "sender_field": (By.XPATH, "//span[.='First People Incompany']"),
        "approve_button": (By.XPATH, "//button[.='Approve' and not(@disabled)]"),
        "reject_button": (By.XPATH, "//button[.='Reject' and not(@disabled)]")
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    class ApprovePage(BasePage):
        locator_dictionary = {
            "approve_header": (By.XPATH, "//div/span[.='Approve']"),
            "comment": (By.XPATH, "//textarea[@name='comment']"),
            "submit": (By.XPATH, "//button[@type='submit' and .='Approve']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

    class RejectPage(BasePage):
        locator_dictionary = {
            "reject_header": (By.XPATH, "//div/span[.='Reject']"),
            "comment": (By.XPATH, "//textarea[@name='comment']"),
            "submit": (By.XPATH, "//button[@type='submit' and .='Reject']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

    def validate_approval(self):
        for t in self.locator_dictionary.keys():
            assert_true(self.__getattr__(t))


#!-*-coding:utf-8-*-
import time
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from conf import new_request_conf as request
from nose.tools import assert_equal, assert_true


class PrjApprovalCardPage(BasePage):
    locator_dictionary = {
        "approval_header": (By.XPATH, "//span[@class='title' and .='Recrutment2']"),
        "company_field": (By.XPATH, "//dt[.='Company']"),
        "company_value": (By.XPATH, "//dd[.='AutotestCo']"),
        "department_field": (By.XPATH, "//dt[.='Department']"),
        "department_value": (By.XPATH, "//dd[.='Office1']"),
        "reason_field": (By.XPATH, "//dt[.='Reason of Opening']"),
        "reason_value": (By.XPATH, u"//dd[.='замена (Second People Incompany)']"),
        "salary_field": (By.XPATH, "//dt[.='Reason of Opening']"),
        "salary_value": (By.XPATH, u"//dd[.='10000 - 20000 EUR (После вычета налогов)']"),
        "close_field": (By.XPATH, "//dt[.='Close before']"),
        "close_value": (By.XPATH, "//dd[.='22.02.2022']"),
        "bonuses_field": (By.XPATH, "//dt[.='Bonuses']"),
        "bonuses_value": (By.XPATH, u"//dd[.='Бонусы']"),
        "probation_field": (By.XPATH, "//dt[.='Probation']"),
        "probation_value": (By.XPATH, "//dd[.='10']"),
        "status_field": (By.XPATH, "//div[contains(.,'Status') and contains(.,'On approval')]"),
        "type_field": (By.XPATH, "//span[.='The presence in the staff list']"),
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


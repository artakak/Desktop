from selenium.webdriver.common.by import By
from base_page_object import BasePage
from conf import new_request_conf as request
import datetime


class PeopleApprovalPage(BasePage):
    locator_dictionary = {
        "ppl_approval_header": (By.XPATH, "//div/span[contains(.,'People approval')]"),
        "first_page": (By.XPATH, "//a[.='1']"),
        "second_page": (By.XPATH, "//a[.='2']"),
        "approval_title": (By.XPATH, "//a/span[contains(.,'First People Incompany')]"),
        "approve_title": (By.XPATH, "//span[contains(.,'Approve People')]"),
        "reject_title": (By.XPATH, "//span[contains(.,'Reject People')]"),
        "last_approval_title": (By.XPATH, "//span[contains(.,'Second People Incompany')]"),
        "last_approval_date": (By.XPATH, "//span[contains(.,'27.07.2018')]"),
        "on_approval_button": (By.XPATH, "//a[contains(.,'On approval')]"),
        "approved_button": (By.XPATH, "//a[contains(.,'Approved')]"),
        "rejected_button": (By.XPATH, "//a[contains(.,'Rejected by approver')]"),
        "canceled_button": (By.XPATH, "//a[contains(.,'Canceled by the sender')]"),
        "cross_button": (By.XPATH, "//i[@class='anticon anticon-close trigger']"),
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

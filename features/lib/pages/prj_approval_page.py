from selenium.webdriver.common.by import By
from base_page_object import BasePage
from conf import new_request_conf as request
import datetime


class ProjectApprovalPage(BasePage):
    locator_dictionary = {
        "prj_approval_header": (By.XPATH, "//div/span[contains(.,'Vacancies approval')]"),
        "approval_title": (By.XPATH, "//a/span[contains(.,'Recrutment1')]"),
        "approve_title": (By.XPATH, "//a/span[contains(.,'Recrutment_approve')]"),
        "reject_title": (By.XPATH, "//a/span[contains(.,'Recrutment_reject')]"),
        "cancel_title": (By.XPATH, "//a/span[contains(.,'Recrutment_canceled')]"),
        "last_approval_title": (By.XPATH, "//a/span[contains(.,'Recrutment2')]"),
        "last_approval_date": (By.XPATH, "//span[contains(.,'30.07.2018')]"),
        "last_approval_type": (By.XPATH, "//span[contains(.,'The presence in the staff list')]"),
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

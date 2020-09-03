from selenium.webdriver.common.by import By
from base_page_object import BasePage
from nose.tools import assert_equal, assert_true
from conf import new_request_conf as request
import datetime


class PortfolioPage(BasePage):
    locator_dictionary = {
        "portfolio_header": (By.XPATH, "//div[@class='title']/span[.='Project REC portfolio']"),
        "portfolio_mass_header": (By.XPATH, "//div[@class='title']/span[.='Project MASS portfolio']"),
        "last_project_title": (By.XPATH, "//span[.='Recrutment_archive']"),
        "filter_button": (By.XPATH, "//a[@class='ant-dropdown-trigger']"),
        "settings_button": (By.XPATH, "//i[@class='anticon anticon-settings']"),
        "request_title": (By.XPATH, "//span[.='Recrutment_reject']"),
        "mass_request_title": (By.XPATH, "//span[.='Mass_request']"),
        "mass_inwork_title": (By.XPATH, "//span[.='Mass_inwork']"),
        "mass_frozen_title": (By.XPATH, "//span[.='Mass_freeze']"),
        "mass_complete_title": (By.XPATH, "//span[.='Mass_complete']"),
        "mass_cancelled_title": (By.XPATH, "//span[.='Mass_annulate']"),
        "mass_archived_title": (By.XPATH, "//span[.='Mass_archive']"),
        "inwork_title": (By.XPATH, "//span[.='Recrutment1']"),
        "frozen_title": (By.XPATH, "//span[.='Recrutment_freeze']"),
        "complete_title": (By.XPATH, "//span[.='Recrutment_complete']"),
        "cancelled_title": (By.XPATH, "//span[.='Recrutment_annulate']"),
        "archived_title": (By.XPATH, "//span[.='Recrutment_archive']"),
        "go_to_project_button": (By.XPATH, "//a[@class='sidebar-link']/i[@class='anticon anticon-briefcase']"),
        "user_field": (By.XPATH, "//div[@class='antd-select-container user-filter']//input"),
        "second_resp_project": (By.XPATH, "//span[.='Position2']"),
        "second_resp_mass_project": (By.XPATH, "//span[.='Mass_Second_User']")
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def validate_project_list(self, type):
        if type == "request":
            assert_true(self.request_title)
        elif type == "inwork":
            assert_true(self.inwork_title)
            assert_true(self.find_element(By.XPATH, "//span[.='10']"))
            assert_true(self.find_element(By.XPATH, "//span[.='25.04.2025']"))
        elif type == "frozen":
            assert_true(self.frozen_title)
            assert_true(self.find_element(By.XPATH, "//span[.='10']"))
            assert_true(self.find_element(By.XPATH, "//span[.='22.02.2022']"))
        elif type == "complete":
            assert_true(self.complete_title)
            assert_true(self.find_element(By.XPATH, "//span[.='2']"))
            assert_true(self.find_element(By.XPATH, "//span[.='22.02.2022']"))
        elif type == "cancelled":
            assert_true(self.cancelled_title)
            assert_true(self.find_element(By.XPATH, "//span[.='10']"))
            assert_true(self.find_element(By.XPATH, "//span[.='22.02.2022']"))
        elif type == "archived":
            assert_true(self.archived_title)
            assert_true(self.find_element(By.XPATH, "//span[.='1']"))
            assert_true(self.find_element(By.XPATH, "//span[.='22.02.2022']"))
        elif type == "mass request":
            assert_true(self.mass_request_title)
            assert_true(self.find_element(By.XPATH, "//span[.='10']"))
        elif type == "mass inwork":
            assert_true(self.mass_inwork_title)
            assert_true(self.find_element(By.XPATH, "//span[.='25']"))
            assert_true(self.find_element(By.XPATH, "//span[.='22.02.2022']"))
        elif type == "mass frozen":
            assert_true(self.mass_frozen_title)
            assert_true(self.find_element(By.XPATH, "//span[.='35']"))
        elif type == "mass complete":
            assert_true(self.mass_complete_title)
            assert_true(self.find_element(By.XPATH, "//span[.='1']"))
        elif type == "mass cancelled":
            assert_true(self.mass_cancelled_title)
            assert_true(self.find_element(By.XPATH, "//span[.='65']"))
        elif type == "mass archived":
            assert_true(self.mass_archived_title)
            assert_true(self.find_element(By.XPATH, "//span[.='45']"))
            assert_true(self.find_element(By.XPATH, "//span[.='25.10.2025']"))

    class FilterPage(BasePage):
        locator_dictionary = {
            "filter_header": (By.XPATH, "//span[.=Filter]"),
            "all_field": (By.XPATH, "//a[.='All']"),
            "request_field": (By.XPATH, "//a[.='Request']"),
            "inprogress_field": (By.XPATH, "//a[.='In progress']"),
            "frozen_field": (By.XPATH, "//a[.='Frozen']"),
            "completed_field": (By.XPATH, "//a[.='Completed']"),
            "cancelled_field": (By.XPATH, "//a[.='Canceled']"),
            "archive_field": (By.XPATH, "//a[.='Archive']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

    class NotWorksheetPage(BasePage):
        locator_dictionary = {
            "not_worksheet_header": (By.XPATH, "//span[.='Project SearchWorksheet']"),
            "ok_button": (By.XPATH, "//button[@aria-label='Close']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

    class PortfolioSettingsPage(BasePage):
        locator_dictionary = {
            "settings_header": (By.XPATH, "//span[.='Projects Portfolio REC settings']"),
            "ok_button": (By.XPATH, "//button[@aria-label='Close']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

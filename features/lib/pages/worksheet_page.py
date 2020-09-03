from selenium.webdriver.common.by import By
from base_page_object import BasePage
from nose.tools import assert_equal, assert_true
from conf import new_request_conf as request
import datetime


class WorkSheetPage(BasePage):
    locator_dictionary = {
        "worksheet_header": (By.XPATH, "//div[@class='title' and contains(.,'Recrutment_complete (AutotestCo) 31/07/2018')]"),
        "worksheet_mass_header": (By.XPATH, "//div[@class='title' and contains(.,'Mass_inwork 02/11/2018')]"),
        "last_people_title": (By.XPATH, "//span[.='People1 People1 People1']"),
        "filter_button": (By.XPATH, "//a[@class='ant-dropdown-trigger']"),
        "refresh_button": (By.XPATH, "//i[@class='anticon anticon-refresh']"),
        "finalist_title": (By.XPATH, "//span[.='First People Incompany']"),
        "finalist_dol": (By.XPATH, "//span[.='Tdol']"),
        "finalist_work": (By.XPATH, "//span[.='AutotestCo 07.2018 -  till now.']"),
        "candidate_title": (By.XPATH, "//span[.='Second People Incompany']"),
        "applicant_title": (By.XPATH, "//span[.='People In Worksheet']"),
        "out_applicant_title": (By.XPATH, "//span[.='People1 People1 People1']"),
        "employed_title": (By.XPATH, "//span[.='Approve People']"),
        "employed_dol": (By.XPATH, "//span[.='Recrutment_complete']"),
        "employed_work": (By.XPATH, "//span[.='AutotestCo 07.2018 -  till now.']"),
        "new_event_button": (By.XPATH, "//button[.='Schedule an event']"),
        "stage_button": (By.XPATH, "//button[.='Change stage']"),
        "settings_button": (By.XPATH, "//i[@class='anticon anticon-settings']"),
        "phone_tab": (By.XPATH, "//div[.='Phone interview']"),
        "mass_people_title_tab": (By.XPATH, "//span[.='Mass1 People1 Project1']"),
        "conversation_title": (By.XPATH, "//a[contains(.,'Conversation')]"),
        "reference_title": (By.XPATH, "//a[contains(.,'Reference check')]"),
        "interview_title": (By.XPATH, "//a[contains(.,'Interview (supervisor)')]"),
        "interview_recruter_title": (By.XPATH, "//a[contains(.,'Interview (recruiter)')]"),
        "custom_title": (By.XPATH, "//a[contains(.,'Project_Event')]"),

        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def validate_worksheet_list(self, type):
        if type == "finalist":
            assert_true(self.finalist_title)
            assert_true(self.finalist_dol)
            assert_true(self.finalist_work)
        elif type == "candidate":
            assert_true(self.candidate_title)
        elif type == "applicant":
            assert_true(self.applicant_title)
        elif type == "out_applicant":
            assert_true(self.out_applicant_title)
        elif type == "employed":
            assert_true(self.employed_title)
            assert_true(self.employed_dol)
            assert_true(self.employed_work)

    class FilterPage(BasePage):
        locator_dictionary = {
            "filter_header": (By.XPATH, "//span[.='Filter']"),
            "all_field": (By.XPATH, "//a[.='All']"),
            "finalist_field": (By.XPATH, "//a[.='Finalists']"),
            "candidate_field": (By.XPATH, "//a[.='Candidates']"),
            "applicant_field": (By.XPATH, "//a[.='Pre-candidates']"),
            "out_applicant_field": (By.XPATH, "//a[.='Removed from pre-candidates']"),
            "employed_field": (By.XPATH, "//a[.='Employed']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

    class StagePage(BasePage):
        locator_dictionary = {
            "stage_header": (By.XPATH, "//span[.='Change stage']"),
            "save_button": (By.XPATH, "//button[.='Save']"),
            "stage_field": (By.XPATH, "//span[contains(.,'Choose stage ...')]//input"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

    class SettingsPage(BasePage):
        locator_dictionary = {
            "settings_header": (By.XPATH, "//span[.='Project SearchWorksheet MAP settings']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)
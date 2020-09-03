from selenium.webdriver.common.by import By
from base_page_object import BasePage


class NotDonePage(BasePage):
    locator_dictionary = {
        "notdone_header": (By.XPATH, "//div/span[contains(.,'Not done')]"),
        "first_event_time": (By.XPATH, "//span[contains(.,'10:00 - 11:00 ')]"),
        "last_event_time": (By.XPATH, "//span[contains(.,'22:00 - 23:00 ')]"),
        "last_event_title": (By.XPATH, "//span[contains(.,'Interview (recruiter)')]"),
        "last_event_date": (By.XPATH, "//span[contains(.,'12.12.2017')]"),
        "prj_title": (By.XPATH, "//span[contains(.,'Recrutment1 (AutotestCo) 12/07/2018')]"),
        "person_title": (By.XPATH, "//span[contains(.,'People1 P.P.')]"),
        "enter_result_button": (By.XPATH, "//button[@type='button' and contains(.,'Enter event')]"),
        "check_box": (By.XPATH, "//input[@type='checkbox']"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

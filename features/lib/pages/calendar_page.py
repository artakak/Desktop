#!-*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from nose.tools import assert_equal, assert_true
from conf import events_conf as event
import time
import datetime


class CalendarPage(BasePage):
    locator_dictionary = {
        "calendar_header": (By.XPATH, "//div[@class='title']/span[.='Calendar']"),
        "select_user_field": (By.XPATH, "//span[contains(.,'First People Incompany')]//input"),
        "select_user_title": (By.XPATH, 'new UiSelector().text("First People Incompany")'),
        "create_event_button": (By.XPATH, "//button[.='Schedule an event']"),
        "create_task_button": (By.XPATH, "//button[.='Set a task']"),
        "complete_task_button": (By.XPATH, "//button[@role='switch']"),
        "private_filter_button": (By.XPATH, "//input[@value='private']"),
        "contact_filter_button": (By.XPATH, "//input[@value='telcnt']"),
        "meeting_filter_button": (By.XPATH, "//input[@value='meetings']"),
        "planer_filter_button": (By.XPATH, 'new UiSelector().description("filter-planer")'),
        "calendar_title": (By.XPATH, "//span[.='Calendar_event']"),
        "calendar_time": (By.XPATH, "//div[div[.='1']]/div[contains(@class,'calendar-time')]/span"),
        "reference_title": (By.XPATH, "//a[.='Reference check']"),
        "reference_time": (By.XPATH, "//div[div[.='2']]/div[contains(@class,'calendar-time')]/span"),
        "interview_recruter_time": (By.XPATH, "//div[div[.='3']]/div[contains(@class,'calendar-time')]/span"),
        "interview_recruter_title": (By.XPATH, "//a[.='Interview (recruiter)']"),
        "conversation_time": (By.XPATH, "//div[div[.='4']]/div[contains(@class,'calendar-time')]/span"),
        "conversation_title": (By.XPATH, "//a[.='Conversation']"),
        "interview_title": (By.XPATH, "//a[.='Interview (supervisor)']"),
        "interview_time": (By.XPATH, "//div[div[.='5']]/div[contains(@class,'calendar-time')]/span"),
        "custom_title": (By.XPATH, "//a[.='Project_Event']"),
        "custom_time": (By.XPATH, "//div[div[.='6']]/div[contains(@class,'calendar-time')]/span"),
        "task1_title": (By.XPATH, "//a[.='Task_high']"),
        "task1_date": (By.XPATH, "//div[div[.='1']]/div[contains(@class,'task-date')]/span"),
        "task1_prior": (By.XPATH, "//p[@class='current' and .='1']"),
        "task1_done": (By.XPATH, "//div[contains(@class,'task-done')]/i"),
        "task2_title": (By.XPATH, "//a[.='Task_medium']"),
        "task2_date": (By.XPATH, "//div[div[.='2']]/div[contains(@class,'task-date')]/span"),
        "task2_prior": (By.XPATH, "//p[@class='current' and .='2']"),
        "task3_title": (By.XPATH, "//a[.='Task_low']"),
        "task3_date": (By.XPATH, "//div[div[.='3']]/div[contains(@class,'task-date')]/span"),
        "task3_prior": (By.XPATH, "//p[@class='current' and .='3']"),

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def validate_date(self, type, num):
        time_element = self.find_element(By.XPATH, "//div[div[.='%s']]/div[contains(@class,'calendar-time')]/span" % num)
        if not event.whole_day[type]:
            assert_equal(time_element.text, "%s - %s" % (event.start[type], event.stop[type]))
        else:
            assert_equal(time_element.text, "whole day")

    def validate_planer_list(self):
        assert_true(self.calendar_title)
        assert_equal(self.calendar_time.text, "whole day")

        assert_true(self.reference_title)
        self.validate_date("reference", "2")

        assert_true(self.interview_recruter_title)
        self.validate_date("interview_recr", "3")

        assert_true(self.conversation_title)
        self.validate_date("conversation", "4")

        assert_true(self.interview_title)
        self.validate_date("interview", "5")

        assert_true(self.custom_title)
        self.validate_date("custom", "6")

    def validate_contact_list(self):
        assert_true(self.reference_title)
        self.validate_date("reference", "1")

        assert_true(self.conversation_title)
        self.validate_date("conversation", "2")

    def validate_meeting_list(self):
        assert_true(self.interview_recruter_title)
        self.validate_date("interview_recr", "1")

        assert_true(self.interview_title)
        self.validate_date("interview", "2")

        assert_true(self.custom_title)
        self.validate_date("custom", "3")

    def validate_private_list(self):
        assert_true(self.calendar_title)
        assert_equal(self.calendar_time.text, "whole day")

    def validate_tasks(self):
        self.complete_task_button.click()
        assert_true(self.task1_title)
        assert_equal(self.task1_date.text, datetime.date.today().strftime("%d.%m.%Y"))
        assert_true(self.task1_prior)
        assert_true(self.task1_done)

        assert_true(self.task2_title)
        assert_equal(self.task2_date.text, datetime.date.today().strftime("%d.%m.%Y"))
        assert_true(self.task2_prior)

        assert_true(self.task3_title)
        assert_equal(self.task3_date.text, datetime.date.today().strftime("%d.%m.%Y"))
        assert_true(self.task3_prior)









import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page_object import BasePage
from conf import events_conf as event
from nose.tools import assert_equal, assert_true


class CreateEventPage(BasePage):
    locator_dictionary = {
        "create_event_header": (By.XPATH, "//span[contains(.,'Schedule an event with the person:')]"),
        "create_calendar_event_header": (By.XPATH, "//span[contains(.,'Plan an event')]"),
        "person_name_field": (By.XPATH, "//span[contains(.,'Approve People')]"),
        "event_name_field": (By.XPATH, "//span[contains(.,'Conversation')]//input"),
        "calendar_name_field": (By.XPATH, "//input[@class='ant-input undefined input form-control']"),
        "calendar_button": (By.XPATH, "//i[@class='anticon anticon-calendar ant-calendar-picker-icon']"),
        "responsible_field": (By.XPATH, "//span[contains(.,'First People Incompany')]//input"),
        "select_whole_day": (By.XPATH, "//button[@role='switch']"),
        "select_start": (By.XPATH, "//input[@name='details.time.from']"),
        "select_end": (By.XPATH, "//input[@name='details.time.to']"),
        "this_time_field": (By.XPATH, 'new UiSelector().text("Events on this time")'),
        "select_drop_down": (By.XPATH, "//div[@class='ant-form-item-control']//input"),
        "comment": (By.XPATH, "//textarea[@placeholder='Enter comment ...']"),
        "save_button": (By.XPATH, "//button[contains(.,'Save')]")
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    class DayPickerPage(BasePage):
        locator_dictionary = {
            "today_button": (By.XPATH, "//a[.='Today']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

    def whole_day(self, on_off=False, start=None, stop=None):
        if not on_off:
            self.select_whole_day.click()
            self.select_start.send_keys(start, Keys.ENTER)
            self.select_end.send_keys(stop, Keys.ENTER)

    def fill_conversation(self):
        assert_true(self.person_name_field)

        self.event_name_field.send_keys("Conversation", Keys.ENTER)

        self.whole_day(event.whole_day['conversation'], event.start['conversation'], event.stop['conversation'])

        self.find_elements(*self.locator_dictionary['select_drop_down'])[8].send_keys(event.participant, Keys.ENTER)

        self.comment.send_keys(event.comment['conversation'], Keys.ENTER)

        self.save_button.click()

    def fill_reference(self):
        assert_true(self.person_name_field)

        self.event_name_field.send_keys("Reference check", Keys.ENTER)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[4].send_keys(event.company, Keys.ENTER)
        time.sleep(2)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[5].send_keys(event.employee, Keys.ENTER)

        self.whole_day(event.whole_day['reference'], event.start['reference'], event.stop['reference'])

        self.comment.send_keys(event.comment['reference'], Keys.ENTER)

        self.save_button.click()

    def fill_interview(self):
        assert_true(self.person_name_field)

        self.event_name_field.send_keys("Interview with a line manager", Keys.ENTER)

        self.whole_day(event.whole_day['interview'], event.start['interview'], event.stop['interview'])

        self.find_elements(*self.locator_dictionary['select_drop_down'])[8].send_keys(event.manager, Keys.ENTER)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[9].send_keys(event.participant, Keys.ENTER)

        self.comment.send_keys(event.comment['interview'], Keys.ENTER)

        self.save_button.click()

    def fill_interview_recruter(self):
        assert_true(self.person_name_field)

        self.event_name_field.send_keys("Interview with a recruiter", Keys.ENTER)

        self.whole_day(event.whole_day['interview_recr'], event.start['interview_recr'], event.stop['interview_recr'])

        self.find_elements(*self.locator_dictionary['select_drop_down'])[4].send_keys(event.participant, Keys.ENTER)

        self.comment.send_keys(event.comment['interview_recr'], Keys.ENTER)

        self.save_button.click()

    def fill_custom(self):
        assert_true(self.person_name_field)

        self.event_name_field.send_keys("Project_Event", Keys.ENTER)

        self.calendar_button.click()
        self.DayPickerPage(self).today_button.click()

        self.whole_day(event.whole_day['custom'], event.start['custom'], event.stop['custom'])

        self.find_elements(*self.locator_dictionary['select_drop_down'])[8].send_keys(event.company, Keys.ENTER)
        time.sleep(2)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[9].send_keys(event.employee, Keys.ENTER)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[10].send_keys(event.participant, Keys.ENTER)

        self.comment.send_keys(event.comment['custom'])

        self.save_button.click()

    def fill_calendar(self):
        self.calendar_name_field.send_keys("Calendar_event", Keys.ENTER)

        self.find_elements(*self.locator_dictionary['select_whole_day'])[1].click()

        self.find_elements(*self.locator_dictionary['select_whole_day'])[3].click()

        self.save_button.click()

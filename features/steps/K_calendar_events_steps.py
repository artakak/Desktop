from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I click on events menu point")
def step_impl(context):
    page = MainMenu(context)
    page.calendar_point.click()


@step("I stay on events page")
def step_impl(context):
    page = CalendarPage(context)
    assert_true(page.calendar_header)


@when("I click on create event button on calendar page")
def step_impl(context):
    page = CalendarPage(context)
    page.create_event_button.click()


@when("I click select user button on calendar page")
def step_impl(context):
    page = CalendarPage(context)
    page.select_user_field.send_keys("First People Incompany", Keys.ENTER)


@then("I can select user")
def step_impl(context):
    page = CalendarPage(context)
    assert_true(page.select_user_field)


@when("I select (?P<type>.+) filter")
def step_impl(context, type):
    page = CalendarPage(context)
    if type == "planer":
        page.planer_filter_button.click()
    elif type == "contact":
        page.contact_filter_button.click()
    elif type == "meeting":
        page.meeting_filter_button.click()
        page.contact_filter_button.click()
    elif type == "private":
        page.private_filter_button.click()
        page.meeting_filter_button.click()
    time.sleep(5)


@then("I see correct list of (?P<type>.+) events")
def step_impl(context, type):
    page = CalendarPage(context)
    if type == "planer":
        page.validate_planer_list()
    elif type == "contact":
        page.validate_contact_list()
    elif type == "meeting":
        page.validate_meeting_list()
    elif type == "private":
        page.validate_private_list()


@step("I click on tasks menu point")
def step_impl(context):
    page = MainMenu(context)
    page.tasks_point.click()


@step("I stay on tasks page")
def step_impl(context):
    page = CalendarPage(context)
    assert_true(page.tasks_header)


@when("I click create task button on tasks page")
def step_impl(context):
    page = CalendarPage(context)
    page.create_task_button.click()


@then("I stay on create task dialog page")
def step_impl(context):
    page = CreateTaskPage(context)
    assert_true(page.create_task_header)


@step("I can create new (?P<value>.+) priority task")
def step_impl(context, value):
    page = CreateTaskPage(context)
    page.create_task(value)


@then("I see correct list of tasks")
def step_impl(context):
    page = CalendarPage(context)
    page.validate_tasks()
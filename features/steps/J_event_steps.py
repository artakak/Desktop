from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I can create new (?P<type>.+) event")
def step_impl(context, type):
    time.sleep(5)
    page = CreateEventPage(context)
    if type == "conversation":
        page.fill_conversation()
    elif type == "reference check":
        page.fill_reference()
    elif type == "interview":
        page.fill_interview()
    elif type == "interview with recruter":
        page.fill_interview_recruter()
    elif type == "custom":
        page.fill_custom()
    elif type == "calendar":
        page.fill_calendar()
    time.sleep(5)


@step("I stay on create event dialog page")
def step_impl(context):
    page = CreateEventPage(context)
    assert_true(page.create_event_header)


@step("I click on (?P<type>.+) event title")
def step_impl(context, type):
    page = WorkSheetPage(context)
    time.sleep(5)
    if type == "conversation":
        page.conversation_title.click()
    elif type == "reference check":
        page.reference_title.click()
    elif type == "interview":
        page.interview_title.click()
    elif type == "interview with recruter":
        page.interview_recruter_title.click()
    elif type == "custom":
        page.custom_title.click()


@step("I can edit this event")
def step_impl(context):
    page = EventPage(context)
    page.edit_button.click()
    page = EditEventPage(context)
    page.save_event_button.click()
    time.sleep(5)
    page = EventPage(context)
    page.close_button.click()


@step("I stay on (?P<type>.+) event page")
def step_impl(context, type):
    page = EventPage(context)
    if type == "conversation":
        assert_true(page.conversation_header)
    elif type == "reference check":
        assert_true(page.reference_header)
    elif type == "interview":
        assert_true(page.interview_header)
    elif type == "interview with recruter":
        assert_true(page.interview_recruter_header)
    elif type == "custom":
        assert_true(page.custom_header)


@then("I see all correct data on (?P<type>.+) event page")
def step_impl(context, type):
    page = EventPage(context)
    time.sleep(5)
    if type == "conversation":
        page.validate_conversation()
    elif type == "reference check":
        page.validate_reference()
    elif type == "interview":
        page.validate_interview()
    elif type == "interview with recruter":
        page.validate_interview_recruter()
    elif type == "custom":
        page.validate_custom()
    page.close_button.click()


@when("I enter (?P<type>.+) result")
def step_impl(context, type):
    page = EventPage(context)
    if type == "conversation":
        page.enter_conversation()
    elif type == "reference check":
        page.enter_reference()
    elif type == "interview":
        page.enter_interview()
    elif type == "interview with recruter":
        page.enter_interview_recruter()
    elif type == "custom":
        page.enter_custom()


@step("I click new event button")
def step_impl(context):
    page = WorkSheetPage(context)
    page.new_event_button.click()


@step("I click on enter result button")
def step_impl(context):
    time.sleep(5)
    page = EventPage(context)
    page.result_button.click()


@then("I stay on create calendar event dialog page")
def step_impl(context):
    page = CreateEventPage(context)
    assert_true(page.create_calendar_event_header)
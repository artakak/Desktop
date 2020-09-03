from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@then("I see last event with all attributes on Not done page")
def step_impl(context):
    page = NotDonePage(context)
    assert_true(page.last_event_time)
    assert_true(page.last_event_date)
    assert_true(page.last_event_title)


@step("I click enter result button")
def step_impl(context):
    page = NotDonePage(context)
    page.enter_result_button.click()


@then("I stay on edit page")
def step_impl(context):
    page = EditEventPage(context)
    assert_true(page.edit_event_header)


@then("I stay on project page")
def step_impl(context):
    assert_true(context.browser.find_element(By.XPATH, "//dt[.='Position']"))
    assert_true(context.browser.find_element(By.XPATH, "//dd[.='Recrutment1']"))
    page = ProjectPage(context)
    page.close_button.click()
    time.sleep(2)


@then("I stay on person page")
def step_impl(context):
    page = PersonPage(context)
    assert_true(page.PersonInfoPage(context).person_sex)
    page.close_button.click()
    time.sleep(2)


@then("I see main menu page")
def step_impl(context):
    page = MainMenu(context)
    assert_true(page.not_done_point)


@when("I check box with event")
def step_impl(context):
    page = NotDonePage(context)
    page.check_box.click()


@then("I stay on event page")
def step_impl(context):
    page = EventPage(context)
    assert_true(page.conversation_header)
    page.close_button.click()
    time.sleep(2)


@when("I click on event title")
def step_impl(context):
    page = NotDonePage(context)
    page.last_event_title.click()


@when("I click on project title")
def step_impl(context):
    page = NotDonePage(context)
    page.prj_title.click()


@when("I click on person title")
def step_impl(context):
    page = NotDonePage(context)
    page.person_title.click()


@step("I click on main menu button")
def step_impl(context):
    page = MainMenu(context)
    page.menu_button.click()
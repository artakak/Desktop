# coding=utf-8
from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I click on target project title")
def step_impl(context):
    page = PortfolioPage(context)
    page.complete_title.click()


@then("I see last people on worksheet page")
def step_impl(context):
    page = WorkSheetPage(context)
    assert_true(page.last_people_title)


@when("I click on filter button on worksheet page")
def step_impl(context):
    page = WorkSheetPage(context)
    page.filter_button.click()


@then("I can change (?P<type>.+) filter in list on worksheet page")
def step_impl(context, type):
    page = WorkSheetPage(context)
    if type == "finalist":
        page.FilterPage(context).finalist_field.click()
    elif type == "candidate":
        page.FilterPage(context).candidate_field.click()
    elif type == "applicant":
        page.FilterPage(context).applicant_field.click()
    elif type == "out applicant":
        page.FilterPage(context).out_applicant_field.click()
    elif type == "employed":
        page.FilterPage(context).employed_field.click()
    time.sleep(5)


@step("I see (?P<type>.+) people in list")
def step_impl(context, type):
    page = WorkSheetPage(context)
    page.validate_worksheet_list(type)


@step("I click (?P<button>.+) button on worksheet page")
def step_impl(context, button):
    page = WorkSheetPage(context)
    if button == "new event":
        page.new_event_button.click()
    elif button == "work with person":
        page.work_with_person_button.click()
    elif button == "document":
        page.document_button.click()
    elif button == "on stage":
        page.stage_button.click()


@then("I stay on create event page")
def step_impl(context):
    page = CreateEventPage(context)
    assert_true(page.create_event_header)
    context.browser.press_keycode(4)


@then("I stay on work with person page")
def step_impl(context):
    page = PersonPage(context)
    assert_true(page.PersonWorkPage(context).prj_title)
    context.browser.press_keycode(4)


@then("I stay on person's document page")
def step_impl(context):
    page = PersonPage(context)
    assert_true(page.PersonDocumentPage(context).document_title)
    context.browser.press_keycode(4)


@step("I click on target mass project title")
def step_impl(context):
    page = PortfolioPage(context)
    page.mass_inwork_title.click()


@step("I stay on mass worksheet page")
def step_impl(context):
    page = WorkSheetPage(context)
    assert_true(page.worksheet_mass_header)


@then("I can fill change stage dialog")
def step_impl(context):
    page = WorkSheetPage(context)
    page.StagePage(context).stage_field.send_keys(u"Телефонное интервью", Keys.ENTER)
    page.StagePage(context).save_button.click()


@step("I see mass people on next stage")
def step_impl(context):
    time.sleep(2)
    page = WorkSheetPage(context)
    page.phone_tab.click()
    assert_true(page.mass_people_title_tab)


@then("I stay on worksheet settings page")
def step_impl(context):
    page = WorkSheetPage(context)
    assert_true(page.SettingsPage(context).settings_header)
    page.StagePage(context).save_button.click()
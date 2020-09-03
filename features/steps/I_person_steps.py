from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I click on target person title")
def step_impl(context):
    page = WorkSheetPage(context)
    page.finalist_title.click()
    page = PersonPage(context)
    page.go_to_person_button.click()


@step("I stay on information person page")
def step_impl(context):
    page = PersonPage(context)
    assert_true(page.page_header)
    assert_true(page.PersonInfoPage(context).photo)
    assert_true(page.modal_title)


@then("I see correct (?P<pages>.+) person page")
def step_impl(context, pages):
    page = PersonPage(context)
    if pages == "information":
        page.PersonInfoPage(context).validate_information()
    elif pages == "documents":
        page.PersonDocumentPage(context).validate_docs()
    elif pages == "history":
        page.PersonHistoryPage(context).validate_history()
        page.close_button.click()


@given("I stay on person page")
def step_impl(context):
    page = PersonPage(context)
    assert_true(page.page_header)


@when("I click on (?P<button>.+) button on person page")
def step_impl(context, button):
    page = PersonPage(context)
    if button == "documents":
        page.documents_button.click()
    elif button == "history":
        page.history_button.click()

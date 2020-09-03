from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I stay on information project page")
def step_impl(context):
    page = ProjectPage(context)
    assert_true(page.modal_title)
    assert_true(page.page_header)


@when("I choose target project from list")
def step_impl(context):
    page = PortfolioPage(context)
    page.go_to_project_button.click()
    page = ProjectPage(context)
    page.go_to_project_button.click()


@then("I see correct (?P<pages>.+) project page")
def step_impl(context, pages):
    page = ProjectPage(context)
    if pages == "information":
        page.InformationPage(context).validate_information()
    elif pages == "documents":
        page.DocumentsPage(context).validate_document()
        page.close_button.click()
        page.close_button.click()
    elif pages == "mass documents":
        page.DocumentsMassPage(context).validate_document()
        page.close_button.click()
        page.close_button.click()
    elif pages == "mass information":
        page.InformationMassPage(context).validate_information()


@given("I stay on project page")
def step_impl(context):
    page = ProjectPage(context)
    assert_true(page.page_header)


@when("I click on documents button on project page")
def step_impl(context):
    elements = context.browser.find_elements(By.XPATH, "//span[@class='doc-tab-header' and contains(.,'Documents')]")
    elements[1].click()


@step("I stay on worksheet page")
def step_impl(context):
    page = WorkSheetPage(context)
    assert_true(page.worksheet_header)


@step("I stay on mass information project page")
def step_impl(context):
    page = ProjectPage(context)
    assert_true(page.mass_modal_title)
    assert_true(page.page_mass_header)


@given("I stay on mass project page")
def step_impl(context):
    page = ProjectPage(context)
    assert_true(page.page_mass_header)
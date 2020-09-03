from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I click on portfolio menu point")
def step_impl(context):
    page = MainMenu(context)
    page.portfolio_point.click()


@step("I stay on portfolio page")
def step_impl(context):
    page = PortfolioPage(context)
    assert_true(page.portfolio_header)


@then("I see last project on portfolio page")
def step_impl(context):
    page = PortfolioPage(context)
    assert_true(page.last_project_title)


@when("I change user in list")
def step_impl(context):
    page = PortfolioPage(context)
    page.user_field.send_keys("Second People Incompany", Keys.ENTER)


@then("I see project of this user in list")
def step_impl(context):
    page = PortfolioPage(context)
    assert_true(page.second_resp_project)
    page.user_field.send_keys("First People Incompany", Keys.ENTER)


@when("I click on filter button on portfolio page")
def step_impl(context):
    page = PortfolioPage(context)
    page.filter_button.click()


@step("I can change (?P<type>.+) filter in list")
def step_impl(context, type):
    page = PortfolioPage(context)
    if type == "request":
        page.FilterPage(context).request_field.click()
    elif type == "inwork":
        page.FilterPage(context).inprogress_field.click()
    elif type == "frozen":
        page.FilterPage(context).frozen_field.click()
    elif type == "complete":
        page.FilterPage(context).completed_field.click()
    elif type == "cancelled":
        page.FilterPage(context).cancelled_field.click()
    elif type == "archived":
        page.FilterPage(context).archive_field.click()
    time.sleep(5)


@step("I see (?P<type>.+) projects in list")
def step_impl(context, type):
    page = PortfolioPage(context)
    page.validate_project_list(type)


@when("I click on request project title")
def step_impl(context):
    page = PortfolioPage(context)
    page.request_title.click()


@then("I see haven't worksheet message")
def step_impl(context):
    page = PortfolioPage(context)
    assert_true(page.NotWorksheetPage(context).not_worksheet_header)
    page.NotWorksheetPage(context).ok_button.click()


@when("I click on settings button on portfolio page")
def step_impl(context):
    page = PortfolioPage(context)
    page.settings_button.click()


@then("I stay on portfolio settings page")
def step_impl(context):
    page = PortfolioPage(context)
    assert_true(page.PortfolioSettingsPage(context).settings_header)
    page.PortfolioSettingsPage(context).ok_button.click()
    time.sleep(2)


@step("I click on mass portfolio menu point")
def step_impl(context):
    page = MainMenu(context)
    page.portfolio_mass_point.click()


@step("I stay on mass portfolio page")
def step_impl(context):
    page = PortfolioPage(context)
    assert_true(page.portfolio_mass_header)


@when("I click on mass request project title")
def step_impl(context):
    page = PortfolioPage(context)
    page.mass_request_title.click()


@then("I see project of this user in mass list")
def step_impl(context):
    page = PortfolioPage(context)
    assert_true(page.second_resp_mass_project)
    page.user_field.send_keys("First People Incompany", Keys.ENTER)
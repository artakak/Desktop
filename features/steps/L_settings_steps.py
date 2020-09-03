from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I click on settings menu point")
def step_impl(context):
    page = MainMenu(context)
    page.settings_point.click()


@then("I see all points of settings")
def step_impl(context):
    page = MainMenu(context)
    assert_true(page.SettingsPage(context).en_header)
    assert_true(page.SettingsPage(context).ru_language_select)
    assert_true(page.SettingsPage(context).en_language_select)


@then("I see all counts are correct")
def step_impl(context):
    page = MainMenu(context)
    assert_true(page.not_done_count)
    assert_true(page.ppl_count)
    assert_true(page.prj_count)
    assert_true(page.all_count)


@when("I stay on settings page")
def step_impl(context):
    page = MainMenu(context)
    assert_true(page.SettingsPage(context).en_header)


@step("I click on change language point")
def step_impl(context):
    page = MainMenu(context)
    page.SettingsPage(context).ru_language_select.click()


@then("I see russian menu")
def step_impl(context):
    page = MainMenu(context)
    assert_true(page.SettingsPage(context).ru_header)
    page.SettingsPage(context).en_language_select.click()
    assert_true(page.SettingsPage(context).en_header)
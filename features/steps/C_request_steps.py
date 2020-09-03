from behave import *
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from features.lib.pages import *


use_step_matcher("re")


@step("I click on requests menu point")
def step_impl(context):
    page = MainMenu(context)
    page.requests_point.click()


@step("I stay on requests page")
def step_impl(context):
    page = RequestsPage(context)
    assert_true(page.requests_header)


@then("I see last event with all attrubutes on Requests page")
def step_impl(context):
    page = RequestsPage(context)
    assert_true(page.last_request_title)


@when("I click on (?P<button>.+) button on Requests page")
def step_impl(context, button):
    page = RequestsPage(context)
    if button == "approved":
        page.approved_button.click()
    elif button == "rejected":
        page.rejected_button.click()
    elif button == "canceled":
        page.canceled_button.click()


@then("I see (?P<type>.+) requests")
def step_impl(context, type):
    page = RequestsPage(context)
    if type == "approved":
        assert_true(page.approved_request_title)
    elif type == "rejected":
        assert_true(page.rejected_request_title)
    elif type == "canceled":
        assert_true(page.new_request_title)
        assert_true(page.new_request_date)


@step("I stay on create request page")
def step_impl(context):
    page = CreateRequestPage(context)
    assert_true(page.create_request_header)


@when("I fill all fields on create request page")
def step_impl(context):
    page = CreateRequestPage(context)
    page.fill_request()


@step("I click send request button on create request page")
def step_impl(context):
    page = CreateRequestPage(context)
    page.send_button.click()
    time.sleep(10)


@step("I see my new request in list")
def step_impl(context):
    page = RequestsPage(context)
    assert_true(page.new_request_title)
    assert_true(page.new_request_date)


@step("I open my new request")
def step_impl(context):
    page = RequestsPage(context)
    page.new_request_title.click()


@step("I stay on my request page")
def step_impl(context):
    page = NewRequestPage(context)
    assert_true(page.request_header)


@step("All fields are correct")
def step_impl(context):
    page = NewRequestPage(context)
    page.validate_request()


@step("I click on delete button on request page")
def step_impl(context):
    page = NewRequestPage(context)
    page.delete_button.click()


@then("I can fill delete request dialog")
def step_impl(context):
    page = NewRequestPage(context)
    page.CancelRequestPage(context).comment.send_keys("Delete")
    page.CancelRequestPage(context).submit.click()
    time.sleep(10)


@when("I scroll down list")
def step_impl(context):
    page = RequestsPage(context)
    action = ActionChains(context.browser)
    action.move_to_element(page.y_scroll_bar)
    action.click_and_hold().move_by_offset(0, 100).release().perform()


@when("I scroll right list")
def step_impl(context):
    page = RequestsPage(context)
    action = ActionChains(context.browser)
    action.move_to_element(page.x_scroll_bar)
    action.click_and_hold().move_by_offset(50, 0).release().perform()


@step("I click on send requests menu point")
def step_impl(context):
    page = MainMenu(context)
    page.send_request_point.click()
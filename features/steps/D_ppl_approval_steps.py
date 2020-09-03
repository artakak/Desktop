from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I click on people approval menu point")
def step_impl(context):
    page = MainMenu(context)
    page.ppl_approv_point.click()
    time.sleep(2)


@step("I stay on people approval page")
def step_impl(context):
    page = PeopleApprovalPage(context)
    assert_true(page.ppl_approval_header)


@then("I see last event with all attributes on people approval page")
def step_impl(context):
    page = PeopleApprovalPage(context)
    assert_true(page.last_approval_title)
    assert_true(page.last_approval_date)
    page.first_page.click()
    time.sleep(5)


@when("I click on (?P<button>.+) button on people approval page")
def step_impl(context, button):
    page = PeopleApprovalPage(context)
    if button == "approved":
        page.approved_button.click()
    elif button == "rejected":
        page.rejected_button.click()
    else:
        page.canceled_button.click()
    time.sleep(2)


@when("I click on people approval")
def step_impl(context):
    page = PeopleApprovalPage(context)
    page.approval_title.click()


@then("I see people approval card with correct data")
def step_impl(context):
    page = PplApprovalCardPage(context)
    page.validate_approval()


@step("I click on (?P<button>.+) button on people approval card")
def step_impl(context, button):
    page = PplApprovalCardPage(context)
    if button == "approve":
        page.approve_button.click()
    else:
        page.reject_button.click()


@then("I can fill (?P<type>.+) people dialog")
def step_impl(context, type):
    page = PplApprovalCardPage(context)
    if type == "approve":
        assert_true(page.ApprovePage(context).approve_header)
        page.ApprovePage(context).comment.send_keys("Approved")
        page.ApprovePage(context).submit.click()
    else:
        assert_true(page.RejectPage(context).reject_header)
        page.ApprovePage(context).comment.send_keys("Rejected")
        page.RejectPage(context).submit.click()
    time.sleep(5)


@then("I see (?P<type>.+) people")
def step_impl(context, type):
    page = PeopleApprovalPage(context)
    if type == "approved":
        page.approve_title.click()
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'Status') and contains(.,'Approved')]"))
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'First P.I.') and contains(.,'Approved')]"))
    elif type == "rejected":
        page.reject_title.click()
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'Status') and contains(.,'Rejected by approver')]"))
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'First P.I.') and contains(.,'Rejected')]"))
    else:
        page.approval_title.click()
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'Status') and contains(.,'Cancelled by the sender')]"))
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'First P.I.') and contains(.,'Annulate')]"))
    page.cross_button.click()


@when("I click on people card for approving")
def step_impl(context):
    page = PeopleApprovalPage(context)
    page.approve_title.click()


@when("I click on people card for rejecting")
def step_impl(context):
    page = PeopleApprovalPage(context)
    page.reject_title.click()


@when("I click second pagination page")
def step_impl(context):
    context.execute_steps(u'When I scroll down list')
    context.execute_steps(u'When I scroll down list')
    page = PeopleApprovalPage(context)
    page.second_page.click()
    time.sleep(5)
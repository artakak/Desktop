from behave import *
from nose.tools import assert_equal, assert_true
from features.lib.pages import *


use_step_matcher("re")


@step("I click on project approval menu point")
def step_impl(context):
    page = MainMenu(context)
    page.prj_approv_point.click()


@step("I stay on project approval page")
def step_impl(context):
    page = ProjectApprovalPage(context)
    assert_true(page.prj_approval_header)
    time.sleep(2)


@then("I see last event with all attributes on project approval page")
def step_impl(context):
    page = ProjectApprovalPage(context)
    assert_true(page.last_approval_title)
    assert_true(page.last_approval_date)
    assert_true(page.last_approval_type)


@when("I click on (?P<button>.+) button on project approval page")
def step_impl(context, button):
    page = ProjectApprovalPage(context)
    if button == "approved":
        page.approved_button.click()
    elif button == "rejected":
        page.rejected_button.click()
    else:
        page.canceled_button.click()
    time.sleep(2)


@when("I click on project approval")
def step_impl(context):
    page = ProjectApprovalPage(context)
    page.last_approval_title.click()


@then("I see project approval card with correct data")
def step_impl(context):
    page = PrjApprovalCardPage(context)
    page.validate_approval()
    context.browser.refresh()


@step("I click on (?P<button>.+) button on project approval card")
def step_impl(context, button):
    page = PrjApprovalCardPage(context)
    if button == "approve":
        page.approve_button.click()
    else:
        page.reject_button.click()


@then("I can fill (?P<type>.+) project dialog")
def step_impl(context, type):
    page = PrjApprovalCardPage(context)
    if type == "approve":
        assert_true(page.ApprovePage(context).approve_header)
        page.ApprovePage(context).comment.send_keys("Approved")
        page.ApprovePage(context).submit.click()
    else:
        assert_true(page.RejectPage(context).reject_header)
        page.ApprovePage(context).comment.send_keys("Rejected")
        page.RejectPage(context).submit.click()
    time.sleep(5)


@then("I see (?P<type>.+) project")
def step_impl(context, type):
    page = ProjectApprovalPage(context)
    if type == "approved":
        page.approve_title.click()
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'Status') and contains(.,'Approved')]"))
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'First P.I.') and contains(.,'Approved')]"))
    elif type == "rejected":
        page.reject_title.click()
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'Status') and contains(.,'Rejected by approver')]"))
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'First P.I.') and contains(.,'Rejected')]"))
    else:
        page.cancel_title.click()
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'Status') and contains(.,'Cancelled by the sender')]"))
        assert_true(page.find_element(By.XPATH, "//div[contains(.,'First P.I.') and contains(.,'canceled')]"))
    page.cross_button.click()


@when("I click on project card for approving")
def step_impl(context):
    page = ProjectApprovalPage(context)
    page.approve_title.click()


@when("I click on project card for rejecting")
def step_impl(context):
    page = ProjectApprovalPage(context)
    page.reject_title.click()
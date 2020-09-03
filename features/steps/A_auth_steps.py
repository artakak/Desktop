# -*- coding: utf-8 -*-
from nose.tools import assert_equal, assert_true
from behave import *
from features.lib.pages import *
from conf import user_conf as user
from utils.get_mail import get_link
import datetime

use_step_matcher("re")


@step("I stay on login screen")
def step_impl(context):
    context.browser.get("https://%s-test.experium.me/#/login" % user.company_name)
    page = LoginPage(context)
    assert_true(page.login_button)


@when('I fill (?P<correct>.+) "Username" and "Password"')
def step_impl(context, correct):
    page = LoginPage(context)
    if correct == "incorrect":
        page.username_field.send_keys("user_wrong_%s" % str(datetime.datetime.today().strftime("%d-%m-%y-%H-%M-%S")))
        page.password_field.send_keys("pass_wrong")
    else:
        page.username_field.send_keys(user.username)
        page.password_field.send_keys(user.password)


@step('I click on "Login" button')
def step_impl(context):
    page = LoginPage(context)
    page.login_button.click()


@then('I see "(?P<message>.+)" message')
def step_impl(context, message):
    page = LoginPage(context)
    if message == "Incorrect":
        assert_true(page.wrong_field)
    elif message == "Captcha":
        assert_true(page.captcha_field)
        context.browser.refresh()
    else:
        assert_true(page.required_field)


@when("I click on forgot link")
def step_impl(context):
    page = LoginPage(context)
    page.forgot_link.click()


@step("I stay on recovery screen")
def step_impl(context):
    page = RecoveryPage(context)
    assert_true(page.send_button)


@when("I fill email field")
def step_impl(context):
    page = RecoveryPage(context)
    page.email_field.send_keys(user.user_mail)


@step("I click reset button")
def step_impl(context):
    page = RecoveryPage(context)
    page.send_button.click()


@then("I see success message")
def step_impl(context):
    page = RecoveryPage(context).SuccessMsg(context)
    assert_true(page.success_message)


@when('I fill "Username" without "Password"')
def step_impl(context):
    page = LoginPage(context)
    page.username_field.send_keys(user.username)


@step('I stay on "Not done" page')
def step_impl(context):
    page = NotDonePage(context)
    assert_true(page.notdone_header)


@given("I open recovery link")
def step_impl(context):
    time.sleep(30)
    context.browser.get(get_link("reset_password"))


@when("I enter same password")
def step_impl(context):
    page = RecoveryPage(context)
    page.password_field.send_keys(user.password)
    page.repeat_field.send_keys(user.password)


@then("I see same password message")
def step_impl(context):
    page = RecoveryPage(context)
    assert_true(page.same_message)


@when('I click on "Login" button 5 times')
def step_impl(context):
    page = LoginPage(context)
    for _ in range(5):
        time.sleep(2)
        page.login_button.click()


@step("I enable push option")
def step_impl(context):
    page = PushPage(context)
    try:
        page.enable_button.click()
    except: pass


@given("I open main page")
def step_impl(context):
    context.browser.get("https://%s-test.experium.me/#/" % user.company_name)
    if context.feature.name in ["Project page", "Person page"]:
        try:
            context.browser.find_element(By.XPATH, "//button[.='Yes']").click()
            context.browser.find_element(By.XPATH, "//button[.='Yes']").click()
        except:
            pass
    time.sleep(5)
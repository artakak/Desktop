from selenium import webdriver
from colorama import init
import os
import shutil
import time
import subprocess
import urllib2
from lib.pagefactory import on
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from utils.get_manifest import get_manifest_info
import utils.exp_srv_update as server_upd

init()


def before_all(context):
    print("Executing before all")
    server_upd.reset()
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("start-maximized")
    #chrome_options.add_argument("headless")
    #chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("window-size=1920,1080")
    #chrome_options.add_argument('user-data-dir=C:\Users\steblin\PycharmProjects\Desktop')
    #chrome_options.add_argument("disable-features=VizDisplayCompositor")
    context.browser = webdriver.Chrome(executable_path='C:\Users\steblin\PycharmProjects\Desktop\chromedriver.exe',
                                       chrome_options=chrome_options, service_args=["--verbose", "--log-path=C:\Users\steblin\PycharmProjects\Desktop\log.log"])
    context.browser.implicitly_wait(10)
    context.browser.set_page_load_timeout(10)
    context.reset_lnk = ""
    manifest = {}
    manifest['Browser.Name'] = 'Chrome'
    manifest['Browser.Version'] = 'version'
    with open(r"C:\Users\steblin\PycharmProjects\Desktop\allure-results\environment.properties", "wb") as output:
        for t in manifest:
            output.writelines("%s=%s\r\n" % (t, manifest[t]))
    output.close()
    print context.browser.desired_capabilities


def before_feature(context, feature):
    print("Before feature\n")


def before_scenario(context, scenario):
    print("Before scenario\n")
    #print("User data:", context.config.userdata)
    # behave -D BROWSER=chrome


def after_scenario(context, scenario):
    print("scenario '%s' - %s" % (scenario.name, scenario.status))
    if scenario.status == "failed":
        #context.browser.save_screenshot(scenario.name + "_failed.png")
        attach(context.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def after_feature(context, feature):
    print("\nAfter Feature")
    if feature.name == "Auth" and feature.status == "failed":
        pass
        #context.browser.quit()


def after_all(context):
    print("Executing after all")
    context.browser.quit()




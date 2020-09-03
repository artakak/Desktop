from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import time
import catcher


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 10

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def find_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def swipe_menu(self, direction):
        if direction == "right":
            self.browser.swipe(533, 1800, 928, 1800, 5000)
        else:
            self.browser.swipe(928, 1800, 533, 1800, 5000)

    def swipe_vertical(self, direction):
        time.sleep(1)
        if direction == "up":
            self.browser.swipe(520, 500, 520, 1700, 5000)
        else:
            self.browser.swipe(520, 1700, 520, 500, 5000)

    def visit(self, url):
        self.browser.get(url)

    def hover(self, element):
            ActionChains(self.browser).move_to_element(element).perform()
            # I don't like this but hover is sensitive and needs some sleep time
            time.sleep(5)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.element_to_be_clickable(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    print (what, "clickable_problems")
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    print (what, "presence_problems")
                    #traceback.print_exc()
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    print (what, "visibility_problems")
                    #traceback.print_exc()

                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print "No %s here!"%what
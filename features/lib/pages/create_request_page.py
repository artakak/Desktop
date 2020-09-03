import datetime
import time
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from conf import new_request_conf as request
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.keys import Keys


class CreateRequestPage(BasePage):
    locator_dictionary = {
        "select_manager": (By.XPATH, "//span[contains(.,'Choose an HR-manager')]//input"),
        "create_request_header": (By.XPATH, "//div/span[contains(.,'Send Request')]"),
        "select_department": (By.XPATH, "//span[contains(.,'Choose department')]//input"),
        "select_position": (By.XPATH, "//input[@name='position']"),
        "select_town": (By.XPATH, "//span[contains(.,'Enter city')]//input"),
        "select_quantity": (By.XPATH, "//input[@placeholder='10 for example']"),
        "select_deadline": (By.XPATH, "//input[@name='deadline']"),
        "select_budget_presence": (By.XPATH, "//span[.='%s']" % request.budget),
        "select_reason": (By.XPATH, "//span[.='%s']" % request.reason),
        "select_empoyee": (By.XPATH, "//span[contains(.,'Choose employee')]//input"),
        "select_salary_from": (By.XPATH, "//input[@name='salary.amount.from']"),
        "select_salary_to": (By.XPATH, "//input[@name='salary.amount.to']"),
        "select_currency": (By.XPATH, "//span[.='Currency']/div/input"),
        "select_salary_type": (By.XPATH, "//span[.='%s']" % request.salary_type),
        "select_bonuses": (By.XPATH, "//textarea[@name='bonuses']"),
        "select_probation": (By.XPATH, "//input[@name='probation']"),
        "select_workplace": (By.XPATH, "//span[contains(text(),'%s')]" % request.workplace),
        "select_shedule": (By.XPATH, "//span[contains(.,'Choose schedule')]//input"),
        "select_worktype": (By.XPATH, "//span[contains(.,'Choose employment type')]//input"),
        "select_requirements": (By.XPATH, "//textarea[@name='requirement']"),
        "select_responsibilities": (By.XPATH, "//textarea[@name='responsibilities']"),
        "select_education": (By.XPATH, "//span[contains(.,'Choose education')]//input"),
        "select_education_comment": (By.XPATH, "//textarea[@name='education.comment']"),
        "select_personality": (By.XPATH, "//textarea[@name='personality']"),
        "select_language": (By.XPATH, "//span[contains(.,'Choose language')]/div/input"),
        "select_language_level": (By.XPATH, "//span[contains(.,'Proficiency')]/div/input"),
        "select_sex": (By.XPATH, "//span[.='%s']" % request.sex),
        "select_age_from": (By.XPATH, "//input[@name='age.from']"),
        "select_age_to": (By.XPATH, "//input[@name='age.to']"),
        "select_experience": (By.XPATH, "//span[contains(.,'Choose experience')]//input"),
        "select_comment": (By.XPATH, "//textarea[@name='comment']"),
        "send_button": (By.XPATH, "//button[@type='submit' and contains(.,'Send Request')]"),
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def fill_request(self):
        time.sleep(10)
        self.select_position.send_keys(request.position)

        self.select_manager.send_keys(request.manager, Keys.ENTER)

        self.select_department.send_keys(request.department, Keys.ENTER)

        town = self.select_town
        town.send_keys(request.town)
        time.sleep(2)
        town.send_keys(Keys.ENTER)

        self.select_quantity.send_keys(request.quantity)

        self.select_deadline.send_keys(datetime.date.today().strftime("%d%m%Y"))

        element = self.select_budget_presence
        #self.browser.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        self.select_reason.click()

        if request.reason == "replacement":
            self.select_empoyee.send_keys(request.employee, Keys.ENTER)

        self.select_salary_from.send_keys(request.salary_from)

        self.select_salary_to.send_keys(request.salary_to)

        self.select_currency.send_keys(request.currency, Keys.ENTER)

        self.select_salary_type.click()

        self.select_bonuses.send_keys(request.bonuses)

        self.select_probation.send_keys(request.probation)

        self.select_workplace.click()

        self.select_shedule.send_keys(request.shedule, Keys.ENTER)

        self.select_worktype.send_keys(request.worktype, Keys.ENTER)

        self.select_requirements.send_keys(request.requirements)

        element = self.select_responsibilities
        #self.browser.execute_script("arguments[0].scrollIntoView();", element)
        element.send_keys(request.responsibilities)

        self.select_education.send_keys(request.education, Keys.ENTER)

        self.select_education_comment.send_keys(request.education_comment)

        self.select_personality.send_keys(request.personality)

        self.select_language.send_keys(request.language_1, Keys.ENTER)
        self.select_language_level.send_keys(request.language_level_1, Keys.ENTER)

        self.select_language.send_keys(request.language_2, Keys.ENTER)
        self.select_language_level.send_keys(request.language_level_2, Keys.ENTER)

        self.select_sex.click()

        element = self.select_age_from
        #self.browser.execute_script("arguments[0].scrollIntoView();", element)
        element.send_keys(request.age_from)

        self.select_age_to.send_keys(request.age_to)

        self.select_experience.send_keys(request.experience, Keys.ENTER)

        self.select_comment.send_keys(request.comment)


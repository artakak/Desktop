import datetime
import time
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from conf import new_request_conf as request
from nose.tools import assert_equal, assert_true


class NewRequestPage(BasePage):
    locator_dictionary = {
        "request_header": (By.XPATH, "//span[@class='title' and contains(.,'%s')]" % request.position),
        "company_field": (By.XPATH, "//dt[.='Company']"),
        "company_value": (By.XPATH, "//dd[.='%s']" % request.company),
        "departament_field": (By.XPATH, "//dt[.='Department']"),
        "departament_value": (By.XPATH, "//dd[.='%s']" % request.department),
        "quant_field": (By.XPATH, "//dt[.='Quantity']"),
        "quant_value": (By.XPATH, "//dd[.='%s']" % request.quantity),
        "reason_field": (By.XPATH, "//dt[.='Reason of Opening']"),
        "reason_value": (By.XPATH, "//dd[.='%s']" % request.reason),
        "replaced_field": (By.XPATH, "//dt[.='Replaced Employee']"),
        "replaced_value": (By.XPATH, "//dd[.='%s']" % request.employee),
        "budget_field": (By.XPATH, "//dt[.='Presence in the Budget']"),
        "budget_value": (By.XPATH, "//dd[contains(.,'%s')]" % request.budget),
        "close_before_field": (By.XPATH, "//dt[.='Close Before']"),
        "close_before_value": (By.XPATH, "//dd[.='%s']" % datetime.date.today().strftime("%d.%m.%Y")),
        "salary_field": (By.XPATH, "//dt[.='Salary min-max']"),
        "salary_value": (By.XPATH, "//dd[contains(.,'%s - %s') and contains(.,'%s') and contains(.,'%s')]" %
                         (request.salary_from, request.salary_to, request.currency, request.salary_type)),
        "bonuses_field": (By.XPATH, "//dt[.='Compensations and Benefits']"),
        "bonuses_value": (By.XPATH, "//dd[.='%s']" % request.bonuses),
        "probation_field": (By.XPATH, "//dt[.='Probation, days']"),
        "probation_value": (By.XPATH, "//dd[.='%s']" % request.probation),
        "workplace_field": (By.XPATH, "//dt[.='Employer']"),
        "workplace_value": (By.XPATH, "//dd[contains(.,'%s')]" % request.workplace),
        "shedule_field": (By.XPATH, "//dt[.='Work Schedule']"),
        "shedule_value": (By.XPATH, "//dd[.='%s']" % request.shedule),
        "worktype_field": (By.XPATH, "//dt[.='Employment Type']"),
        "worktype_value": (By.XPATH, "//dd[.='%s']" % request.worktype),
        "requirements_field": (By.XPATH, "//dt[.='Experience Requirements']"),
        "requirements_value": (By.XPATH, "//dd[.='%s']" % request.requirements),
        "responsibilities_field": (By.XPATH, "//dt[.='Responsibilities']"),
        "responsibilities_value": (By.XPATH, "//dd[.='%s']" % request.responsibilities),
        "education_field": (By.XPATH, "//dt[.='Education']"),
        "education_value": (By.XPATH, "//dd[.='%s (%s)']" % (request.education, request.education_comment)),
        "language_field": (By.XPATH, "//dt[.='Foreign languages']"),
        "language_value": (By.XPATH, "//dd[contains(.,'%s') and contains(.,'%s')]" %
                           (request.language_1, request.language_2)),
        "sex_field": (By.XPATH, "//dt[.='Sex']"),
        "sex_value": (By.XPATH, "//dd[.='%s']" % request.sex),
        "age_field": (By.XPATH, "//dt[.='Age']"),
        "age_value": (By.XPATH, "//dd[contains(.,'%s - %s')]" % (request.age_from, request.age_to)),
        "exp_field": (By.XPATH, "//dt[.='Yrs of Exp.']"),
        "exp_value": (By.XPATH, "//dd[.='%s']" % request.experience),
        "personality_value": (By.XPATH, "//div[.='%s']" % request.personality),
        "comment_value": (By.XPATH, "//div[.='%s']" % request.comment),
        "delete_button": (By.XPATH, "//button[.='Cancel' and not(@disabled)]"),
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    class CancelRequestPage(BasePage):
        locator_dictionary = {
            "comment": (By.XPATH, "//textarea[@name='comment']"),
            "submit": (By.XPATH, "//button[@type='submit' and .='Cancel']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

    def validate_request(self):
        for t in self.locator_dictionary.keys():
            assert_true(self.__getattr__(t))




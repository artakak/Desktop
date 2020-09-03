#!-*-coding:utf-8-*-
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page_object import BasePage
from nose.tools import assert_equal, assert_true
from conf import events_conf as event
import time


class EventPage(BasePage):
    locator_dictionary = {
        "conversation_header": (By.XPATH, "//span[.='Conversation']"),
        "interview_header": (By.XPATH, 'new UiSelector().text("Interview (supervisor)")'),
        "interview_recruter_header": (By.XPATH, 'new UiSelector().text("Interview (recruiter)")'),
        "reference_header": (By.XPATH, 'new UiSelector().text("Reference check")'),
        "custom_header": (By.XPATH, 'new UiSelector().text("Project_Event")'),
        "edit_button": (By.XPATH, "//button[.='Edit']"),
        "close_button": (By.XPATH, "//button[.='Close']"),
        "file_button": (By.XPATH, "//button[.='File']"),
        "file_input": (By.XPATH, "//input[@type='file']"),
        "result_button": (By.XPATH, "//button[contains(.,'Enter event')]"),
        "date_field": (By.XPATH, "//dt[.='Date']"),
        "time_field": (By.XPATH, "//dt[.='Time']"),
        "responsible_field": (By.XPATH, "//dt[.='Employee']"),
        "sheduled_field": (By.XPATH, "//dt[.='Sheduled']"),
        "related_person_field": (By.XPATH, "//dt[.='Related to person']"),
        "related_prj_field": (By.XPATH, "//dt[.='Related to project']"),
        "contact_person_field": (By.XPATH, "//dt[.='Referrer']"),
        "contact_manager_field": (By.XPATH, "//dt[.='Line manager']"),
        "company_field": (By.XPATH, "//dt[.='Company where referrer works']"),
        "company2_field": (By.XPATH, "//dt[.='Company from the base']"),
        "company_value": (By.XPATH, "//dd[.='%s']" % event.company),
        "particip_value": (By.XPATH, '//android.view.ViewGroup[@content-desc="onGoToParticipant"]/android.widget.TextView[1]'),
        "took_place_button": (By.XPATH, "//span[.='Took place']"),
        "not_took_plase_button": (By.XPATH, "//span[contains(.,'t take place')]"),
        "good_icon": (By.XPATH, "//input[@value='good']"),
        "medium_icon": (By.XPATH, "//input[@value='neutral']"),
        "bad_icon": (By.XPATH, "//input[@value='bad']"),
        "conformance_select": (By.XPATH, 'new UiSelector().description("shortResultBlock.percent")'),
        "short_comment_select": (By.XPATH, "//textarea[@name='shortResultBlock.comment']"),
        "free_form_select": (By.XPATH, "//textarea[@name='result.body']"),
        "zak_info_select": (By.XPATH, "//textarea[@name='result.xmlbody.MainData.ZAKINFO']"),
        "cand_info_select": (By.XPATH, "//textarea[@name='result.xmlbody.MainData.CANDINFO']"),
        "save_short_button": (By.XPATH, "//button[.='Save short result']"),
        "save_event_button": (By.XPATH, "//button[.='Save event result']"),
        "free_form_button": (By.XPATH, "//button[.='Free form']"),
        "fill_form_button": (By.XPATH, "//button[.='Fill form']"),
        "took_place_field": (By.XPATH, "//dt[.='Did event happened?']"),
        "score_field": (By.XPATH, "//dt[.='Appreciate the person']"),
        "short_result_field": (By.XPATH, "//dt[.='Short result']"),
        "conformance_field": (By.XPATH, "//dt[.='% of conformity']"),
        "reason_field": (By.XPATH, "//dt[.='Reason']"),
        "edit_document_button": (By.XPATH, "//button[.='Edit document']"),
        "download_document_button": (By.XPATH, "//button[.='Download']"),
        "select_drop_down": (By.XPATH, "//div[@class='ant-form-item-control']//input"),
        "form_title": (By.XPATH, "//h1[.='Form1']"),
        "q_select": (By.XPATH, "//input[@class='sc-chPdSV dIUKAe']"),
        "q3_day": (By.XPATH, "//input[@placeholder='dd']"),
        "q3_month": (By.XPATH, "//span[.='Month']"),
        "q3_year": (By.XPATH, "//input[@placeholder='yyyy']"),
        "save_button": (By.XPATH, "//button[.='Save']")

        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def validate_date(self, type):
        if not event.whole_day[type]:
            assert_true(self.find_element(By.XPATH, "//dd[.='%s - %s ']" % (event.start[type], event.stop[type])))

    def enter_conversation(self):
        self.took_place_button.click()

        self.good_icon.click()

        self.find_elements(*self.locator_dictionary['select_drop_down'])[5].send_keys('Fully meets the requirements', Keys.ENTER)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[6].send_keys('50', Keys.ENTER)

        self.short_comment_select.send_keys(event.comment['conversation'])

        self.save_short_button.click()

    def validate_conversation(self):
        assert_true(self.date_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='%s']" % datetime.date.today().strftime("%d.%m.%Y")))

        assert_true(self.time_field)
        self.validate_date('conversation')

        assert_true(self.responsible_field)
        resp_short = event.responsible.split(" ")
        assert_true(self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (resp_short[0], resp_short[1][0], resp_short[2][0])))

        particip_short = event.participant.split(" ")
        assert_true(self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (particip_short[0], particip_short[1][0], particip_short[2][0])))

        assert_true(self.sheduled_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='First P.I.']"))

        assert_true(self.related_person_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Approve P.']"))

        assert_true(self.related_prj_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Recrutment_complete (AutotestCo) 31/07/2018']"))

        assert_equal(len(self.find_elements(By.XPATH, "//dd[.='%s']" % event.comment['conversation'])), 2)

        assert_true(self.took_place_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Yes']"))

        assert_true(self.score_field)
        assert_true(self.find_element(By.XPATH, u"//dd[.='положительная']"))

        assert_true(self.short_result_field)
        assert_true(self.find_element(By.XPATH, u"//dd[.='Полностью соответствует требованиям']"))

        assert_true(self.conformance_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='50']"))

    def enter_reference(self):
        self.not_took_plase_button.click()

        time.sleep(2)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[2].send_keys('Force majeure circumstances',
                                                                                      Keys.ENTER)
        self.short_comment_select.send_keys(event.comment['reference'])

        self.free_form_button.click()

        self.free_form_select.send_keys("reference_result")

        self.save_event_button.click()

    def validate_reference(self):
        assert_true(self.date_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='%s']" % datetime.date.today().strftime("%d.%m.%Y")))

        self.validate_date('reference')

        assert_true(self.responsible_field)
        resp_short = event.responsible.split(" ")
        assert_true(self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (resp_short[0], resp_short[1][0], resp_short[2][0])))

        assert_true(self.sheduled_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='First P.I.']"))

        assert_true(self.related_person_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Approve P.']"))

        assert_true(self.related_prj_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Recrutment_complete (AutotestCo) 31/07/2018']"))

        assert_true(self.company_field)
        assert_true(self.company_value)

        assert_true(self.contact_person_field)
        empl_short = event.employee.split(" ")
        assert_true(self.find_element(By.XPATH, "//dd['%s %s.%s.']" % (empl_short[0], empl_short[1][0], empl_short[2][0])))

        assert_equal(len(self.find_elements(By.XPATH, "//dd[.='%s']" % event.comment['reference'])), 2)

        assert_true(self.took_place_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='No']"))

        assert_true(self.reason_field)
        assert_true(self.find_element(By.XPATH, u"//dd[.='Форс-мажор']"))

        assert_true(self.find_element(By.XPATH, "//div[.='reference_result']"))

        self.edit_document_button.click()
        self.save_button.click()

        assert_true(self.download_document_button)

    def enter_interview(self):
        self.not_took_plase_button.click()

        time.sleep(2)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[2].send_keys('The applicant asked to reschedule a meeting',
                                                                                      Keys.ENTER)

        self.short_comment_select.send_keys(event.comment['interview'])

        self.fill_form_button.click()

        self.cand_info_select.send_keys("candidate_info")

        self.zak_info_select.send_keys("contact_info")

        self.save_event_button.click()

    def validate_interview(self):
        assert_true(self.date_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='%s']" % datetime.date.today().strftime("%d.%m.%Y")))

        assert_true(self.time_field)
        self.validate_date('interview')

        assert_true(self.responsible_field)
        resp_short = event.responsible.split(" ")
        assert_true(
            self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (resp_short[0], resp_short[1][0], resp_short[2][0])))

        particip_short = event.participant.split(" ")
        assert_true(self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (
        particip_short[0], particip_short[1][0], particip_short[2][0])))

        assert_true(self.sheduled_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='First P.I.']"))

        assert_true(self.related_person_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Approve P.']"))

        assert_true(self.related_prj_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Recrutment_complete (AutotestCo) 31/07/2018']"))

        assert_true(self.contact_manager_field)
        empl_short = event.manager.split(" ")
        assert_true(self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (empl_short[0], empl_short[1][0], empl_short[2][0])))

        assert_equal(len(self.find_elements(By.XPATH, "//dd[.='%s']" % event.comment['interview'])), 2)

        assert_true(self.took_place_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='No']"))

        assert_true(self.reason_field)
        assert_true(self.find_element(By.XPATH, u"//dd[.='Соискатель попросил перенести встречу']"))

        assert_true(self.find_element(By.XPATH, "//span[.='contact_info']"))

        assert_true(self.find_element(By.XPATH, "//span[.='candidate_info']"))

        assert_true(self.edit_document_button)

    def enter_interview_recruter(self):
        self.not_took_plase_button.click()

        time.sleep(2)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[2].send_keys('We cancelled a meeting', Keys.ENTER)

        self.short_comment_select.send_keys(event.comment['interview_recr'])

        self.file_button.click()

        self.file_input.send_keys(r"C:\Program Files (x86)\Experium\doc-doc.txt")

        self.save_event_button.click()

    def validate_interview_recruter(self):
        assert_true(self.date_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='%s']" % datetime.date.today().strftime("%d.%m.%Y")))

        self.validate_date('interview_recr')

        assert_true(self.responsible_field)
        resp_short = event.responsible.split(" ")
        assert_true(
            self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (resp_short[0], resp_short[1][0], resp_short[2][0])))

        particip_short = event.participant.split(" ")
        assert_true(self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (
        particip_short[0], particip_short[1][0], particip_short[2][0])))

        assert_true(self.sheduled_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='First P.I.']"))

        assert_true(self.related_person_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Approve P.']"))

        assert_true(self.related_prj_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Recrutment_complete (AutotestCo) 31/07/2018']"))

        assert_equal(len(self.find_elements(By.XPATH, "//dd[.='%s']" % event.comment['interview_recr'])), 2)

        assert_true(self.took_place_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='No']"))

        assert_true(self.reason_field)
        assert_true(self.find_element(By.XPATH, u"//dd[.='Мы отменили встречу']"))

        assert_true(self.find_element(By.XPATH, "//div[.='TextOfDocument']"))

        assert_true(self.edit_document_button)
        assert_true(self.download_document_button)

    def enter_custom(self):
        self.took_place_button.click()

        self.bad_icon.click()

        self.find_elements(*self.locator_dictionary['select_drop_down'])[5].send_keys('Left the meeting', Keys.ENTER)

        self.find_elements(*self.locator_dictionary['select_drop_down'])[6].send_keys('10', Keys.ENTER)

        self.short_comment_select.send_keys(event.comment['custom'])

        self.fill_form_button.click()

        time.sleep(5)

        assert_true(self.form_title)

        self.find_elements(*self.locator_dictionary['q_select'])[0].send_keys("Text")

        self.find_elements(*self.locator_dictionary['q_select'])[1].send_keys("1212")

        self.q3_day.send_keys("12")
        self.q3_month.click()
        self.find_element(By.XPATH, "//div[.='January']").click()
        self.q3_year.send_keys("1988")

        self.save_button.click()

    def validate_custom(self):
        assert_true(self.date_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='%s']" % datetime.date.today().strftime("%d.%m.%Y")))

        assert_true(self.time_field)
        self.validate_date('custom')

        assert_true(self.responsible_field)
        resp_short = event.responsible.split(" ")
        assert_true(
            self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (resp_short[0], resp_short[1][0], resp_short[2][0])))

        particip_short = event.participant.split(" ")
        assert_true(self.find_element(By.XPATH, "//dd[.='%s %s.%s.']" % (
        particip_short[0], particip_short[1][0], particip_short[2][0])))

        assert_true(self.sheduled_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='First P.I.']"))

        assert_true(self.related_person_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Approve P.']"))

        assert_true(self.related_prj_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Recrutment_complete (AutotestCo) 31/07/2018']"))

        assert_true(self.company2_field)
        assert_true(self.company_value)

        empl_short = event.employee.split(" ")
        assert_true(
            self.find_element(By.XPATH, "//dd['%s %s.%s.']" % (empl_short[0], empl_short[1][0], empl_short[2][0])))

        assert_equal(len(self.find_elements(By.XPATH, "//dd[.='%s']" % event.comment['custom'])), 2)

        assert_true(self.took_place_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='Yes']"))

        assert_true(self.score_field)
        assert_true(self.find_element(By.XPATH, u"//dd[.='отрицательная']"))

        assert_true(self.short_result_field)
        assert_true(self.find_element(By.XPATH, u"//dd[.='Ушел со встречи']"))

        assert_true(self.conformance_field)
        assert_true(self.find_element(By.XPATH, "//dd[.='10']"))

        assert_true(self.form_title)
        assert_true(self.find_element(By.XPATH, "//input[@value='Text']"))
        assert_true(self.find_element(By.XPATH, "//input[@value='1212']"))
        assert_true(self.find_element(By.XPATH, "//input[@value='12']"))
        assert_true(self.find_element(By.XPATH, "//span[.='January']"))
        assert_true(self.find_element(By.XPATH, "//input[@value='1988']"))
        assert_true(self.edit_document_button)








#!-*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from nose.tools import assert_equal, assert_true


class PersonPage(BasePage):
    locator_dictionary = {
        "page_header": (By.XPATH, "//div[@class='ant-modal-title' and .='First People Incompany']"),
        "information_button": (By.XPATH, "//div[@class='collapsible-modal-body ']//span[.='Information']"),
        "documents_button": (By.XPATH, "//div[@class='collapsible-modal-body ']//span[.='Documents']"),
        "history_button": (By.XPATH, "//div[@class='collapsible-modal-body ']//span[.='History']"),
        "go_to_person_button": (By.XPATH, "//div[@class='right-sidebar-header']/i[@class='anticon anticon-user-man']"),
        "close_button": (By.XPATH, "//button[@aria-label='Close']"),
        "cross_button": (By.XPATH, "//i[@class='anticon anticon-close trigger']"),
        "modal_title": (By.XPATH, "//div[@class='ant-modal-title' and .='First People Incompany']"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    class PersonInfoPage(BasePage):
        locator_dictionary = {
            "photo": (By.XPATH, "//div[@class='person-mask']/img"),
            "name_field": (By.XPATH, "//span[.='First People Incompany']"),
            "birthday_field": (By.XPATH, "//span[.='12.12.1999']"),
            "person_sex": (By.XPATH, "//span[.='Male']"),
            "phone_field": (By.XPATH, u"//a[.='(+7925) 12-3456 (моб)']"),
            "phone_comment_field": (By.XPATH, "//small[.='Comments']"),
            "mail_field": (By.XPATH, u"//a[.='golubkin@experium.ru (раб)']"),
            "messenger_field": (By.XPATH, "//dd[contains(.,'123987')]"),
            "site_field": (By.XPATH, "//a[.='www.bla-bla.ru']"),
            "organization_field": (By.XPATH, "//td[.='AutotestCo']"),
            "position_field": (By.XPATH, "//td[.='Tdol']"),
            "exp_field": (By.XPATH, "//td[.='07.2018 - till now.']"),
            "inst_field": (By.XPATH, "//td[.='Edu_place']"),
            "spec_field": (By.XPATH, "//td[.='Spec1']"),
            "grad_field": (By.XPATH, "//td[.='1957']"),
            "lang_field": (By.XPATH, u"//span[.='английский (Базовый)']"),
            "adress_field": (By.XPATH, u"//div[.='Россия, 125445, Алтайский край, Metro, Барнаул, Street, dom 1, str. 2, korp. 3, kv. 4']"),
            "citizenship_field": (By.XPATH, "//dt[.='Citizenship']"),
            "citizenship_value": (By.XPATH, u"//dd[.='Бельгия']"),
            "source_field": (By.XPATH, "//dt[.='Source of appearance in system']"),
            "source_value": (By.XPATH, "//dd[.='07/08/2018 Job site - reply (HeadHunter) - Comments']"),
            "class1_field": (By.XPATH, "//b[.='Industry']"),
            "class1_1_field": (By.XPATH, "//li[.='Banks']"),
            "class2_field": (By.XPATH, "//b[.='Function']"),
            "class2_1_field": (By.XPATH, "//li[.='Mining']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

        def validate_information(self):
            for t in self.locator_dictionary.keys():
                assert_true(self.__getattr__(t))

    class PersonDocumentPage(BasePage):
        locator_dictionary = {
            "doc1_name": (By.XPATH, u"//div[@class='collapsible-modal-body ']//a[contains(.,'Предложение о работе First P.I.')]"),
            "doc1_date": (By.XPATH, "//div[@class='collapsible-modal-body ']//span[.='31.07.2018']"),
            "doc1_type": (By.XPATH, u"//div[@class='collapsible-modal-body ']//a[contains(.,'Предложение о работе First P.I.')]/div[.='txt']"),
            "doc2_name": (By.XPATH, "//div[@class='collapsible-modal-body ']//a[contains(.,'289597-frederika.')]"),
            "doc2_date": (By.XPATH, "//div[@class='collapsible-modal-body ']//span[.='07.08.2018']"),
            "doc2_type": (By.XPATH, "//div[@class='collapsible-modal-body ']//a[contains(.,'289597-frederika.')]/div[.='jpeg']"),
            "doc3_name": (By.XPATH, "//div[@class='collapsible-modal-body ']//a[contains(.,'Document First P.I.')]"),
            "doc3_date": (By.XPATH, "//div[@class='collapsible-modal-body ']//span[.='07.08.2018']"),
            "doc3_type": (By.XPATH, "//div[@class='collapsible-modal-body ']//a[contains(.,'Document First P.I.')]//div[.='txt']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

        def validate_docs(self):
            for t in self.locator_dictionary.keys():
                assert_true(self.__getattr__(t))

    class PersonHistoryPage(BasePage):
        locator_dictionary = {
            "work_with_name_field": (By.XPATH, "//a[.='First P.I. from ']"),
            "work_with_date_field": (By.XPATH, "//span[.=' 31.07.2018 ']"),
            "contact_with_name_field": (By.XPATH, "//a[.='First P.I. ']"),
            "contact_with_date_field": (By.XPATH, "//span[.=' 31.07.2018 ']"),
            "event_name_field": (By.XPATH, "//a[.='Job offer']"),
            "event_prj_field": (By.XPATH, "//div[.='Recrutment_complete (AutotestCo) 31/07/2018) - see document']"),
            "event_date_field": (By.XPATH, "//span[.=' 31.07.2018 ']"),
            "prj_name_field": (By.XPATH, "//b[.='Internal recruitment']"),
            "prj_resp_field": (By.XPATH, "//a[.='Finalist - Recrutment_complete (AutotestCo) 31/07/2018 (resp.First P.I.)']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

        def validate_history(self):
            for t in self.locator_dictionary.keys():
                assert_true(self.__getattr__(t))


#!-*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from nose.tools import assert_equal, assert_true
import datetime


class ProjectPage(BasePage):
    locator_dictionary = {
        "page_header": (By.XPATH, "//span[@class='title' and .='Recrutment_complete']"),
        "page_mass_header": (By.XPATH, "//span[@class='title' and .='Mass_inwork']"),
        "information_button": (By.XPATH, "/span[@class='doc-tab-header' and .='Project card']"),
        "documents_button": (By.XPATH, "//span[@class='doc-tab-header' and .='Documents']"),
        "go_to_project_button": (By.XPATH, "//div[@class='right-sidebar-header']/i[@class='anticon anticon-briefcase']"),
        "close_button": (By.XPATH, "//button[@aria-label='Close']"),
        "modal_title": (By.XPATH, "//div[@class='ant-modal-title']//div[.='Recrutment_complete']"),
        "mass_modal_title": (By.XPATH, "//div[@class='ant-modal-title']//div[.='Mass_inwork']"),
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    class InformationPage(BasePage):
        locator_dictionary = {
            "position_field": (By.XPATH, "//dt[.='Position']"),
            "position_value": (By.XPATH, "//dd[.='Recrutment_complete']"),
            "positions_total_field": (By.XPATH, "//dt[contains (.,'total')]"),
            "positions_total_value": (By.XPATH, "//dd[.='2']"),
            "positions_rest_field": (By.XPATH, "//dt[contains (.,'rest')]"),
            "positions_rest_value": (By.XPATH, "//dd[.='1']"),
            "city_field": (By.XPATH, "//dt[.='City']"),
            "city_value": (By.XPATH, "//dd[.='Abakan']"),
            "department_field": (By.XPATH, "//dt[.='Department']"),
            "department_value": (By.XPATH, "//dd[.='Office1']"),
            "presence_field": (By.XPATH, "//dt[.='Presence in the Budget']"),
            "presence_value": (By.XPATH, u"//dd[.='да']"),
            "reason_field": (By.XPATH, "//dt[.='Reason of Opening']"),
            "reason_value": (By.XPATH, u"//dd[.='замена']"),
            "project_status_field": (By.XPATH, "//dt[.='Project status']"),
            "project_status_value": (By.XPATH, "//dd[.='High activity. In progress']"),
            "in_work_since_field": (By.XPATH, "//dt[.='In Work since']"),
            "in_work_since_value": (By.XPATH, "//dd[.='31.07.2018']"),
            "duration_field": (By.XPATH, "//dt[.='Duration']"),
            "duration_value": (By.XPATH, "//dd[.='%s']" % str((datetime.datetime.now() - datetime.datetime(2018, 7, 31)).days)),
            "close_before_field": (By.XPATH, "//dt[.='Close before']"),
            "close_before_value": (By.XPATH, "//dd[.='22.02.2022']"),
            "fee_field": (By.XPATH, "//dt[.='Position Fee']"),
            "fee_value": (By.XPATH, "//dd[.='10500 USD; 10%, advance payment 1 USD, payment 2 USD, post payment 3 USD, other payment 4 USD']"),
            "responsible_value": (By.XPATH, "//a[.='Resp. - First People Incompany']"),
            "confirmer_value": (By.XPATH, "//a[.='Conf. - First P.I. (Approved: The presence in the staff list)']"),
            "client_value": (By.XPATH, "//a[.='Client - First People Incompany']"),
            "requirements_field": (By.XPATH, "//dt[.='Requirements']"),
            "requirements_value": (By.XPATH, u"//dd[.='Требования к опыту']"),
            "education_field": (By.XPATH, "//dt[.='Education']"),
            "education_value": (By.XPATH, u"//dd[.='высшее (коммент к образованию)']"),
            "foreign_languages_field": (By.XPATH, "//dt[.='Foreign languages']"),
            "foreign_languages_value": (By.XPATH, u"//dd[.='английский (Базовый)\nнемецкий (Читаю проф. лит.)']"),
            "sex_field": (By.XPATH, "//dt[.='Sex']"),
            "sex_value": (By.XPATH, u"//dd[.='муж']"),
            "age_field": (By.XPATH, "//dt[.='Age']"),
            "age_value": (By.XPATH, "//dd[.='from 25 before 27']"),
            "terms_of_empl_field": (By.XPATH, "//dt[.='Terms of Empl.']"),
            "terms_of_empl_value": (By.XPATH, u"//dd[.='5 лет']"),
            "personal_qualities_value": (By.XPATH, u"//div[.='Личные качества']"),
            "responsibilities_value": (By.XPATH, u"//div[.='Обязанности']"),
            "salary_field": (By.XPATH, "//dt[.='Salary']"),
            "salary_value": (By.XPATH, "//dd[.='10 000 - 20 000  EUR (After taxation)']"),
            "bonuses_field": (By.XPATH, "//dt[.='Bonuses']"),
            "bonuses_value": (By.XPATH, u"//dd[.='Бонусы']"),
            "probation_field": (By.XPATH, "//dt[.='Probation']"),
            "probation_value": (By.XPATH, "//dd[.='10 days']"),
            "employer_field": (By.XPATH, "//dt[.='Employer']"),
            "employer_value": (By.XPATH, u"//dd[.='У работодателя']"),
            "schedule_field": (By.XPATH, "//dt[.='Work Schedule']"),
            "schedule_value": (By.XPATH, u"//dd[.='Неполный день']"),
            "type_field": (By.XPATH, "//dt[.='Employment Type']"),
            "type_value": (By.XPATH, u"//dd[.='Полная']"),
            "approval_value": (By.XPATH, "//li[.='01/08/2018 Approved (The presence in the staff list) (First P.I.)']"),
            "comments_value": (By.XPATH, u"//div[.='31/07/2018 First P.I.: Комментарий']"),
            "class1_field": (By.XPATH, "//span[.='Industry']"),
            "class1_value": (By.XPATH, "//span[.='/Logistics']"),
            "class2_field": (By.XPATH, "//span[.='Function']"),
            "class2_value": (By.XPATH, "//span[.='/Science']"),
            "class3_field": (By.XPATH, "//span[.='Level']"),
            "class3_value": (By.XPATH, "//span[.='/Top Manager']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

        def validate_information(self):
            for t in self.locator_dictionary.keys():
                assert_true(self.__getattr__(t))

    class InformationMassPage(BasePage):
        locator_dictionary = {
            "position_field": (By.XPATH, "//dt[.='Position']"),
            "position_value": (By.XPATH, "//dd[.='Mass_inwork']"),
            "position_mass_value": (By.XPATH, "//dd[.='Mass_inwork']"),
            "positions_total_field": (By.XPATH, "//dt[contains (.,'total')]"),
            "positions_total_value": (By.XPATH, "//dd[.='25']"),
            "positions_rest_field": (By.XPATH, "//dt[contains (.,'rest')]"),
            "positions_rest_value": (By.XPATH, "//dd[.='25']"),
            "city_field": (By.XPATH, "//dt[.='City']"),
            "city_value": (By.XPATH, "//dd[.='Abadan']"),
            "department_field": (By.XPATH, "//dt[.='Department']"),
            "department_value": (By.XPATH, "//dd[.='Office1']"),
            "presence_field": (By.XPATH, "//dt[.='Presence in the Budget']"),
            "presence_value": (By.XPATH, u"//dd[.='да']"),
            "project_status_field": (By.XPATH, "//dt[.='Project status']"),
            "project_status_value": (By.XPATH, "//dd[.='High activity. In progress']"),
            "in_work_since_field": (By.XPATH, "//dt[.='In Work since']"),
            "in_work_since_value": (By.XPATH, "//dd[.='02.11.2018']"),
            "duration_field": (By.XPATH, "//dt[.='Duration']"),
            "duration_value": (By.XPATH, "//dd[.='%s']" % str((datetime.datetime.now() - datetime.datetime(2018, 11, 2)).days)),
            "close_before_field": (By.XPATH, "//dt[.='Close before']"),
            "close_before_value": (By.XPATH, "//dd[.='22.02.2022']"),
            "fee_field": (By.XPATH, "//dt[.='Position Fee']"),
            "fee_value": (By.XPATH, "//dd[.='15000 EUR; 10%, advance payment 16 EUR, payment 17 EUR, post payment 18 EUR, other payment 19 EUR']"),
            "scenario_field": (By.XPATH, "//dt[.='Scenario']"),
            "scenario_value": (By.XPATH, "//dd[.='Basic scenario']"),
            "responsible_value": (By.XPATH, "//a[.='Resp. - First People Incompany']"),
            "client_value": (By.XPATH, "//a[.='Client - First People Incompany']"),
            "requirements_field": (By.XPATH, "//dt[.='Requirements']"),
            "requirements_value": (By.XPATH, u"//dd[.='Требования']"),
            "education_field": (By.XPATH, "//dt[.='Education']"),
            "education_value": (By.XPATH, u"//dd[.='высшее (Инженер)']"),
            "foreign_languages_field": (By.XPATH, "//dt[.='Foreign languages']"),
            "foreign_languages_value": (By.XPATH, u"//dd[.='английский (Средний)']"),
            "sex_field": (By.XPATH, "//dt[.='Sex']"),
            "sex_value": (By.XPATH, u"//dd[.='муж']"),
            "age_field": (By.XPATH, "//dt[.='Age']"),
            "age_value": (By.XPATH, "//dd[.='from 25 before 30']"),
            "terms_of_empl_field": (By.XPATH, "//dt[.='Terms of Empl.']"),
            "terms_of_empl_value": (By.XPATH, u"//dd[.='4 года']"),
            "personal_qualities_value": (By.XPATH, u"//div[.='Личные качества']"),
            "responsibilities_value": (By.XPATH, u"//div[.='Обязанности']"),
            "salary_field": (By.XPATH, "//dt[.='Salary']"),
            "salary_value": (By.XPATH, "//dd[.='10 000 - 20 000  EUR (After taxation)']"),
            "bonuses_field": (By.XPATH, "//dt[.='Bonuses']"),
            "bonuses_value": (By.XPATH, u"//dd[.='Бонусы']"),
            "probation_field": (By.XPATH, "//dt[.='Probation']"),
            "probation_value": (By.XPATH, "//dd[.='15 days']"),
            "employer_field": (By.XPATH, "//dt[.='Employer']"),
            "employer_value": (By.XPATH, u"//dd[.='У работодателя']"),
            "schedule_field": (By.XPATH, "//dt[.='Work Schedule']"),
            "schedule_value": (By.XPATH, u"//dd[.='Гибкий график']"),
            "type_field": (By.XPATH, "//dt[.='Employment Type']"),
            "type_value": (By.XPATH, u"//dd[.='Волонтерство']"),
            "comments_value": (By.XPATH, u"//div[.='02/11/2018 First P.I.: Комментс']"),
            "class1_field": (By.XPATH, "//span[.='Industry']"),
            "class1_value": (By.XPATH, "//span[.='/Agriculture']"),
            "class2_field": (By.XPATH, "//span[.='Function']"),
            "class2_value": (By.XPATH, "//span[.='/Security']"),
            "class3_field": (By.XPATH, "//span[.='Level']"),
            "class3_value": (By.XPATH, "//span[.='/Entry level']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

        def validate_information(self):
            for t in self.locator_dictionary.keys():
                assert_true(self.__getattr__(t))

    class DocumentsPage(BasePage):
        locator_dictionary = {
            "doc_name_value": (By.XPATH, u"//a[contains(.,'Предложение о работе Approve P.')]"),
            "doc_date_value": (By.XPATH, "//span[.='31.07.2018']"),
            "doc_type_value": (By.XPATH, "//div[.='txt']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

        class DocumentPage(BasePage):
            locator_dictionary = {
                "doc_text": (By.XPATH, "//div[.='Document1']"),
                "doc_edit_button": (By.XPATH, "//button[.='Edit document']")
            }

            def __init__(self, context):
                BasePage.__init__(
                    self,
                    context.browser)

        def validate_document(self):
            for t in self.locator_dictionary.keys():
                assert_true(self.__getattr__(t))

            self.doc_name_value.click()

            for t in self.DocumentPage(self).locator_dictionary.keys():
                assert_true(self.DocumentPage(self).__getattr__(t))

    class DocumentsMassPage(BasePage):
        locator_dictionary = {
            "doc_name_value": (By.XPATH, u"//a[contains(.,'Переговоры с КА Mass_inwork 02/11/2018')]"),
            "doc_date_value": (By.XPATH, "//span[.='02.11.2018']"),
            "doc_type_value": (By.XPATH, "//div[.='txt']")
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)

        class DocumentPage(BasePage):
            locator_dictionary = {
                "doc_text": (By.XPATH, "//div[.='Doc_Doc']"),
                "doc_edit_button": (By.XPATH, "//button[.='Edit document']")
            }

            def __init__(self, context):
                BasePage.__init__(
                    self,
                    context.browser)

        def validate_document(self):
            for t in self.locator_dictionary.keys():
                assert_true(self.__getattr__(t))

            self.doc_name_value.click()

            for t in self.DocumentPage(self).locator_dictionary.keys():
                assert_true(self.DocumentPage(self).__getattr__(t))





#!-*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from base_page_object import BasePage
from nose.tools import assert_equal, assert_true


class MainMenu(BasePage):
    locator_dictionary = {
        "menu_button": (By.XPATH, "//div[@class='logo']"),
        "company_header": (By.XPATH, 'new UiSelector().text("AutotestCo")'),
        "not_done_point": (By.XPATH, "//a[contains(.,'Not done')]"),
        "send_request_point": (By.XPATH, "//a[contains(.,'Send Request')]"),
        "requests_point": (By.XPATH, "//a[contains(.,'Requests')]"),
        "ppl_approv_point": (By.XPATH, "//a[contains(.,'People approval')]"),
        "prj_approv_point": (By.XPATH, "//a[contains(.,'Vacancies approval')]"),
        "portfolio_point": (By.XPATH, "//a[contains(.,'Project REC portfolio')]"),
        "portfolio_mass_point": (By.XPATH, "//a[contains(.,'Project MASS portfolio')]"),
        "calendar_point": (By.XPATH, "//a[contains(.,'Calendar')]"),
        "settings_point": (By.XPATH, "//li[@class='ant-menu-item extended-click-area-item settings-item']"),
        "not_done_count": (By.XPATH, "//span[contains(.,'Not done')]/sup[@title='10']"),
        "ppl_count": (By.XPATH, "//span[contains(.,'People approval')]/sup[@title='10']"),
        "prj_count": (By.XPATH, "//span[contains(.,'Vacancies approval')]/sup[@title='8']"),
        "all_count": (By.XPATH, "//sup[@title='28']")
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    class SettingsPage(BasePage):
        locator_dictionary = {
            "en_header": (By.XPATH, "//span[@class='title' and .='Settings']"),
            "ru_header": (By.XPATH, u"//span[@class='title' and .='Настройки']"),
            "ru_language_select": (By.XPATH, u"//span[.='Русский']"),
            "en_language_select": (By.XPATH, "//span[.='English']"),
        }

        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser)


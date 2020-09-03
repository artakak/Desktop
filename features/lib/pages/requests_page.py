from selenium.webdriver.common.by import By
from base_page_object import BasePage
from conf import new_request_conf as request
import datetime


class RequestsPage(BasePage):
    locator_dictionary = {
        "y_scroll_bar": (By.ID, 'y-scrollbar'),
        "x_scroll_bar": (By.ID, 'x-scrollbar'),
        "requests_header": (By.XPATH, "//div/span[contains(.,'Requests')]"),
        "last_request_title": (By.XPATH, "//span[contains(.,'Position2')]"),
        "on_approval_button": (By.XPATH, "//a[contains(.,'On approval')]"),
        "approved_button": (By.XPATH, "//a[contains(.,'Approved')]"),
        "rejected_button": (By.XPATH, "//a[contains(.,'Rejected by approver')]"),
        "canceled_button": (By.XPATH, "//a[contains(.,'Canceled by the sender')]"),
        "approved_request_title": (By.XPATH, "//span[contains(.,'Position_approve')]"),
        "rejected_request_title": (By.XPATH, "//span[contains(.,'Position_reject')]"),
        "new_request_title": (By.XPATH, "//span[contains(text(),'%s')]" % request.position),
        "new_request_date": (By.XPATH, "//span[contains(text(),'%s')]" % datetime.date.today().strftime("%d.%m.%Y"))
        }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

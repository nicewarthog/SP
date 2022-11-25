import logging

from pages.base_page import BasePage


class OrderPage(BasePage):
    log = logging.getLogger("[OrderPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.order_page import OrderPageConst
        self.order_page_constants = OrderPageConst
        from constants.header import HeaderConst
        self.header_constants = HeaderConst

    # Sign In

    # def verify_success_sign_in(self, login):
    #     """Verify correct Sign In"""
    #     assert self.get_element_text(self.header_constants.ACCOUNT_USERNAME_XPATH.format(login_option=login)) == login, \
    #         f"Actual message: {self.get_element_text(self.header_constants.ACCOUNT_USERNAME_XPATH)}"

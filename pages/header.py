import logging

from pages.base_page import BasePage


class Header(BasePage):
    log = logging.getLogger("[Header]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.header import HeaderConst
        self.header_constants = HeaderConst

    # Sign In

    def verify_success_sign_in(self, login):
        """Verify correct Sign In"""
        assert self.get_element_text(self.header_constants.ACCOUNT_USERNAME_XPATH.format(login_option=login)) == login, \
            f"Actual message: {self.get_element_text(self.header_constants.ACCOUNT_USERNAME_XPATH)}"

    # Sign Out
    def click_account_logo(self):
        """Click account logo"""
        self.click(xpath=self.header_constants.ACCOUNT_LOGO_XPATH)

    def verify_sign_out_button_elements(self):
        """Verify the Sign-Out button has correct icon and title"""
        assert self.is_exist(xpath=self.header_constants.SIGN_OUT_ICON_XPATH)
        assert self.get_element_text(self.header_constants.SIGN_OUT_BUTTON_XPATH) == self.header_constants.SIGN_OUT_BUTTON_TEXT, \
            f"Actual message: {self.get_element_text(self.header_constants.SIGN_OUT_BUTTON_XPATH)}"

    def sign_out(self):
        """Sign Out from account"""
        # Open form with Sign Out button
        self.click(xpath=self.header_constants.ACCOUNT_LOGO_XPATH)
        # Click Sign Out button
        self.click(xpath=self.header_constants.SIGN_OUT_BUTTON_XPATH)
        from pages.start_page import StartPage
        return StartPage(self.driver)

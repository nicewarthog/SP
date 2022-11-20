import logging

from selenium.webdriver import Keys

from pages.base_page import BasePage


class StartPage(BasePage):
    log = logging.getLogger("[StartPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.start_page import StartPageConst
        self.start_page_constants = StartPageConst
        from constants.header import HeaderConst
        self.header_constants = HeaderConst

    # Start Page elements

    def verify_main_logo(self):
        """Verify the Start Page has Main Logo"""
        assert self.is_exist(xpath=self.start_page_constants.MAIN_LOGO_XPATH)

    def verify_h3(self):
        """Verify the Start Page h3 has correct text"""
        assert self.get_element_text(self.start_page_constants.H3_XPATH) == self.start_page_constants.H3_TEXT, \
            f"Actual message: {self.get_element_text(self.start_page_constants.H3_XPATH)}"

    def verify_login_field_title(self):
        """Verify the Login field title has correct text"""
        assert self.get_element_text(self.start_page_constants.LOGIN_FIELD_TITLE_XPATH) == self.start_page_constants.LOGIN_FIELD_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.start_page_constants.LOGIN_FIELD_TITLE_XPATH)}"

    def verify_password_field_title(self):
        """Verify the Password field title has correct text"""
        assert self.get_element_text(self.start_page_constants.PASSWORD_FIELD_TITLE_XPATH) == self.start_page_constants.PASSWORD_FIELD_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.start_page_constants.PASSWORD_FIELD_TITLE_XPATH)}"

    def verify_sign_in_button_title(self):
        """Verify the Sign-In button has correct title"""
        assert self.get_element_text(self.start_page_constants.SIGN_IN_BUTTON_XPATH) == self.start_page_constants.SIGN_IN_BUTTON_TEXT.lower(), \
            f"Actual message: {self.get_element_text(self.start_page_constants.SIGN_IN_BUTTON_XPATH)}"

    # Correct Sign In

    def sign_in_with_button(self, basic_user):
        """Sign in as the correct user and verify that you are inside"""
        # Fill username
        self.fill_field(xpath=self.start_page_constants.SIGN_IN_LOGIN_FIELD_XPATH, value=basic_user.login)
        # Fill password
        self.fill_field(xpath=self.start_page_constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=basic_user.password)
        # Click Sign In button
        self.click(xpath=self.start_page_constants.SIGN_IN_BUTTON_XPATH)
        from pages.order_page import OrderPage
        return OrderPage(self.driver)

    def sign_in_with_enter(self, basic_user):
        """Sign in as the correct user with Enter key and verify that you are inside"""
        # Fill username
        self.fill_field(xpath=self.start_page_constants.SIGN_IN_LOGIN_FIELD_XPATH, value=basic_user.login)
        # Fill password, press Enter
        self.fill_field(xpath=self.start_page_constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=basic_user.password + Keys.ENTER)
        from pages.order_page import OrderPage
        return OrderPage(self.driver)

    # Incorrect Sign In

    def incorrect_sign_in(self, basic_user):
        """Sign in with incorrect login or password"""
        # Fill username
        self.fill_field(xpath=self.start_page_constants.SIGN_IN_LOGIN_FIELD_XPATH, value=basic_user.login)
        # Fill password
        self.fill_field(xpath=self.start_page_constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=basic_user.password)
        # Click Sign In button
        self.click(xpath=self.start_page_constants.H3_XPATH)

    def verify_empty_login_message(self):
        """Verify the error message for empty login appears and has correct text"""
        assert self.get_element_text(self.start_page_constants.EMPTY_LOGIN_MESSAGE_XPATH) == self.start_page_constants.EMPTY_LOGIN_PASSWORD_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.start_page_constants.EMPTY_LOGIN_MESSAGE_XPATH)}"

    def verify_empty_password_message(self):
        """Verify the error message for empty password appears and has correct text"""
        assert self.get_element_text(self.start_page_constants.EMPTY_PASSWORD_MESSAGE_XPATH) == self.start_page_constants.EMPTY_LOGIN_PASSWORD_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.start_page_constants.EMPTY_PASSWORD_MESSAGE_XPATH)}"

    def verify_incorrect_credentials_message(self):
        """Verify the error message for incorrect login or password appears and has correct text"""
        assert self.get_element_text(
            self.start_page_constants.INCORRECT_CREDENTIALS_MESSAGE_XPATH) == self.start_page_constants.INCORRECT_CREDENTIALS_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.start_page_constants.INCORRECT_CREDENTIALS_MESSAGE_XPATH)}"

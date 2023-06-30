import logging

from selenium.webdriver import Keys

from pages.base_page import BasePage


class StartPageSignIn(BasePage):
    log = logging.getLogger("[StartPageSignIn]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.start_page.sp_elements import StPgElementsConst
        self.st_pg_elements_const = StPgElementsConst
        from constants.start_page.sp_sign_in import StPgSignInConst
        self.st_pg_sign_in_const = StPgSignInConst

    # Correct Sign In

    def sign_in_with_button(self, basic_user):
        """Sign in as the correct user and verify that you are inside"""
        # Fill username
        self.fill_field(xpath=self.st_pg_sign_in_const.SIGN_IN_LOGIN_FIELD_XPATH, value=basic_user.login)
        # Fill password
        self.fill_field(xpath=self.st_pg_sign_in_const.SIGN_IN_PASSWORD_FIELD_XPATH, value=basic_user.password)
        # Click Sign In button
        self.click(xpath=self.st_pg_sign_in_const.SIGN_IN_BUTTON_XPATH)

    def sign_in_with_enter(self, basic_user):
        """Sign in as the correct user with Enter key and verify that you are inside"""
        # Fill username
        self.fill_field(xpath=self.st_pg_sign_in_const.SIGN_IN_LOGIN_FIELD_XPATH, value=basic_user.login)
        # Fill password, press Enter
        self.fill_field(xpath=self.st_pg_sign_in_const.SIGN_IN_PASSWORD_FIELD_XPATH, value=basic_user.password + Keys.ENTER)

    # Incorrect Sign In

    def incorrect_sign_in(self, basic_user):
        """Sign in with incorrect login or password"""
        # Fill username
        self.fill_field(xpath=self.st_pg_sign_in_const.SIGN_IN_LOGIN_FIELD_XPATH, value=basic_user.login)
        # Fill password
        self.fill_field(xpath=self.st_pg_sign_in_const.SIGN_IN_PASSWORD_FIELD_XPATH, value=basic_user.password)
        # Click Sign In button
        self.click(xpath=self.st_pg_elements_const.H3_XPATH)

    def verify_empty_login_message(self):
        """Verify the error message for empty login appears and has correct text"""
        assert self.get_element_text(self.st_pg_sign_in_const.EMPTY_LOGIN_MESSAGE_XPATH) == self.st_pg_sign_in_const.EMPTY_LOGIN_PASSWORD_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.st_pg_sign_in_const.EMPTY_LOGIN_MESSAGE_XPATH)}"

    def verify_empty_password_message(self):
        """Verify the error message for empty password appears and has correct text"""
        assert self.get_element_text(self.st_pg_sign_in_const.EMPTY_PASSWORD_MESSAGE_XPATH) == self.st_pg_sign_in_const.EMPTY_LOGIN_PASSWORD_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.st_pg_sign_in_const.EMPTY_PASSWORD_MESSAGE_XPATH)}"

    def verify_incorrect_credentials_message(self):
        """Verify the error message for incorrect login or password appears and has correct text"""
        assert self.get_element_text(
            self.st_pg_sign_in_const.INCORRECT_CREDENTIALS_MESSAGE_XPATH) == self.st_pg_sign_in_const.INCORRECT_CREDENTIALS_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.st_pg_sign_in_const.INCORRECT_CREDENTIALS_MESSAGE_XPATH)}"

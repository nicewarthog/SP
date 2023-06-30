import logging

from pages.base_page import BasePage


class StartPageElements(BasePage):
    log = logging.getLogger("[StartPageElements]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.start_page.sp_elements import StPgElementsConst
        self.st_pg_elements_const = StPgElementsConst
        from constants.start_page.sp_sign_in import StPgSignInConst
        self.st_pg_sign_in_const = StPgSignInConst

    def verify_main_logo(self):
        """Verify the Start Page has Main Logo"""
        assert self.is_exist(xpath=self.st_pg_elements_const.MAIN_LOGO_XPATH)

    def verify_h3(self):
        """Verify the Start Page h3 has correct text"""
        assert self.get_element_text(self.st_pg_elements_const.H3_XPATH) == self.st_pg_elements_const.H3_TEXT, \
            f"Actual message: {self.get_element_text(self.st_pg_elements_const.H3_XPATH)}"

    def verify_login_field_title(self):
        """Verify the Login field title has correct text"""
        assert self.get_element_text(self.st_pg_elements_const.LOGIN_FIELD_TITLE_XPATH) == self.st_pg_elements_const.LOGIN_FIELD_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.st_pg_elements_const.LOGIN_FIELD_TITLE_XPATH)}"

    def verify_password_field_title(self):
        """Verify the Password field title has correct text"""
        assert self.get_element_text(self.st_pg_elements_const.PASSWORD_FIELD_TITLE_XPATH) == self.st_pg_elements_const.PASSWORD_FIELD_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.st_pg_elements_const.PASSWORD_FIELD_TITLE_XPATH)}"

    def verify_sign_in_button_title(self):
        """Verify the Sign-In button has correct title"""
        assert self.get_element_text(self.st_pg_sign_in_const.SIGN_IN_BUTTON_XPATH) == self.st_pg_sign_in_const.SIGN_IN_BUTTON_TEXT, \
            f"Actual message: {self.get_element_text(self.st_pg_sign_in_const.SIGN_IN_BUTTON_XPATH)}"

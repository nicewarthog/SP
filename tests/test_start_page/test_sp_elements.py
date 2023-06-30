import logging


class TestStPgElements:
    log = logging.getLogger("StartPageElements")

    def test_main_logo(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify Main Logo
        """

        open_start_page.st_pg_elements.verify_main_logo()
        self.log.info(f"Main Logo is exist")

    def test_h3(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify the Start Page h3 has correct text
        """

        open_start_page.st_pg_elements.verify_h3()
        self.log.info("H3 text is correct")

    def test_login_field_title(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify the Login field title has correct text
        """

        open_start_page.st_pg_elements.verify_login_field_title()
        self.log.info("Login field title is correct")

    def test_password_field_title(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify the Password field title has correct text
        """

        open_start_page.st_pg_elements.verify_password_field_title()
        self.log.info("Password field title is correct")

    def test_sign_in_button_title(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify the Sign-In button has correct title
        """

        open_start_page.st_pg_elements.verify_sign_in_button_title()
        self.log.info("Sign-In button title is correct")

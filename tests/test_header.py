import logging


class TestHeader:
    log = logging.getLogger("Header")

    # Log Out
    def test_sign_out(self, sign_in_with_basic_user, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with basic user

        Steps:
        - Open form with Sign Out button
        - Click Sign Out button
        - Verify successful Sign Out
        """

        # Log Out from account
        open_start_page = open_start_page.header.sign_out()

        # Verify the h3 in authorisation form of StartPage
        open_start_page.verify_h3()
        self.log.info("Sign Out is successfully")

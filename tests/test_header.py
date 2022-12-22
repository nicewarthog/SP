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

    def test_sign_out_after_refresh(self, sign_in_with_basic_user, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with basic user

        Steps:
        - Open form with Sign Out button
        - Click Sign Out button
        - Verify successful Sign Out
        - Refresh page and verify successful Sign Out again
        """

        # Log Out from account
        open_start_page = open_start_page.header.sign_out()

        # Verify the h3 in authorisation form of StartPage
        open_start_page.verify_h3()
        self.log.info("Sign Out is successfully")

        # Refresh page
        open_start_page.refresh_page()

        # Verify the h3 in authorisation form of StartPage
        open_start_page.verify_h3()
        self.log.info("Sign Out is successfully")

    def test_sign_out_and_sign_in_with_new_user(self, sign_in_with_basic_user, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with basic user

        Steps:
        - Open form with Sign Out button
        - Click Sign Out button
        - Verify successful Sign Out from account
        - Sign In with another user credentials and verify success
        """

        # Log Out from account
        open_start_page = open_start_page.header.sign_out()

        # Verify the h3 in authorisation form of StartPage and refresh page
        open_start_page.verify_h3()
        self.log.info("Sign Out is successfully")
        open_start_page.refresh_page()

        basic_user = User(login="seopay-qa-analyst", password="seopay-qa-analyst")
        open_header = open_start_page.sign_in_with_button(basic_user)
        self.log.info(f"Order page is opened")

        # Verify the username in header
        open_header.verify_success_sign_in(basic_user.login)
        self.log.info(f"Account name {basic_user.login} was verified, Sign In is successfully")

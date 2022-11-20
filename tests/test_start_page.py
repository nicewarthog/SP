import logging

from pages.utils import User


class TestStartPage:
    log = logging.getLogger("StartPage")

    # Start Page elements

    def test_main_logo(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify Main Logo
        """

        # Verify Main Logo
        open_start_page.verify_main_logo()
        self.log.info(f"Main Logo is exist")

    def test_h3(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify the Start Page h3 has correct text
        """

        # Verify H3 text
        open_start_page.verify_h3()
        self.log.info("H3 text is correct")

    def test_login_field_title(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify the Login field title has correct text
        """

        # Verify Login field title
        open_start_page.verify_login_field_title()
        self.log.info("Login field title is correct")

    def test_password_field_title(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify the Password field title has correct text
        """

        # Verify Password field title
        open_start_page.verify_password_field_title()
        self.log.info("Password field title is correct")

    def test_sign_in_button_title(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Verify the Sign-In button has correct title
        """

        # Verify Sign-In button title
        open_start_page.verify_sign_in_button_title()
        self.log.info("Sign-In button title is correct")

    # Correct Sign In

    def test_correct_sign_in_with_button(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill Login, password
        - Click Sign In button
        - Verify successful Sign In
        """

        # Log in as user
        basic_user = User(login="seopay-qa-ceo", password="uGwql6dqvC9fAFwC")
        open_order_page = open_start_page.sign_in_with_button(basic_user)
        self.log.info(f"Order page is opened")

        # Verify the username in header
        open_order_page.verify_success_sign_in(basic_user.login)
        self.log.info(f"Account name {basic_user.login} was verified, Sign In is successfully")

    def test_correct_sign_in_with_enter(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill Login, password
        - Press Enter key
        - Verify successful Sign In
        """

        # Log in as user
        basic_user = User(login="seopay-qa-ceo", password="uGwql6dqvC9fAFwC")
        open_order_page = open_start_page.sign_in_with_enter(basic_user)
        self.log.info(f"Order page is opened")

        # Verify the username in header
        open_order_page.verify_success_sign_in(basic_user.login)
        self.log.info(f"Account name {basic_user.login} was verified, Sign In is successfully")

    def test_sign_in_with_spaces(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill Login with spaces before and after it
        - Fill Password with spaces before and after it
        - Click Sign In button
        - Verify successful Sign In
        """

        # Fill Login and Password with spaces before and after them
        basic_user = User(login=" seopay-qa-ceo ", password=" uGwql6dqvC9fAFwC ")
        open_order_page = open_start_page.sign_in_with_button(basic_user)
        self.log.info(f"Order page is opened")

        # Verify the username in header
        open_order_page.verify_success_sign_in(basic_user.login.replace(" ", ""))
        self.log.info(f"Account name {basic_user.login} was verified, Sign In is successfully")

        # Incorrect Sign In

    def test_empty_login_with_focus(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct password
        - Change focus
        - Verify error message
        """

        # Log in with empty login and click H3
        basic_user = User(password="uGwql6dqvC9fAFwC")
        open_start_page.incorrect_sign_in(basic_user)

        # Verify error message for login
        open_start_page.verify_empty_login_message()
        self.log.info("Login field is empty. Error message appears")

    def test_empty_login_with_button(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct password
        - Click Sign In button
        - Verify error message
        """

        # Log in with empty login and click Sign In button
        basic_user = User(password="uGwql6dqvC9fAFwC")
        open_start_page.sign_in_with_button(basic_user)

        # Verify error message for login
        open_start_page.verify_empty_login_message()
        self.log.info("Login field is empty. Error message appears")

    def test_empty_password_with_focus(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login
        - Change focus
        - Verify error message
        """

        # Log in with empty password and click H3
        basic_user = User(login="seopay-qa-ceo")
        open_start_page.incorrect_sign_in(basic_user)

        # Verify error message for password
        open_start_page.verify_empty_password_message()
        self.log.info("Password field is empty. Error message appears")

    def test_empty_password_with_button(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login
        - Click Sign In button
        - Verify error message
        """

        # Log in with empty password and click Sign In button
        basic_user = User(login="seopay-qa-ceo")
        open_start_page.sign_in_with_button(basic_user)

        # Verify error message for password
        open_start_page.verify_empty_password_message()
        self.log.info("Password field is empty. Error message appears")

    def test_incorrect_login(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill incorrect login, correct password
        - Click Sign In button
        - Verify error message
        """

        # Log in with incorrect login
        basic_user = User()
        basic_user.random_user_data(login=basic_user.login, password="uGwql6dqvC9fAFwC")
        open_start_page.sign_in_with_button(basic_user)

        # Verify message for incorrect credentials
        open_start_page.verify_incorrect_credentials_message()
        self.log.info(f"Login {basic_user.login} is incorrect. Error message appears")

    def test_incorrect_password(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login, incorrect password
        - Click Sign In button
        - Verify error message
        """

        # Log in with incorrect password
        basic_user = User()
        basic_user.random_user_data(login="seopay-qa-ceo", password=basic_user.password)
        open_start_page.sign_in_with_button(basic_user)

        # Verify message for incorrect credentials
        open_start_page.verify_incorrect_credentials_message()
        self.log.info(f"Password {basic_user.password} is incorrect. Error message appears")

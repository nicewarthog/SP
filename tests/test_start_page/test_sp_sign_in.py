import logging

from pages.utils import User


class TestStartPage:
    log = logging.getLogger("StartPageSignIn")

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
        basic_user = User()
        basic_user.random_correct_user(login=basic_user.login, password=basic_user.password)
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Move to the Header
        open_header = open_start_page.from_start_page_to_header()
        self.log.info(f"Header is opened")

        # Verify the username in header
        open_header.verify_success_sign_in(basic_user.login)
        self.log.info(f"Account name {basic_user.login} was verified, Sign In with button is successfully")

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
        basic_user = User()
        basic_user.random_correct_user(login=basic_user.login, password=basic_user.password)
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Move to the Header
        open_header = open_start_page.from_start_page_to_header()
        self.log.info(f"Header is opened")

        # Verify the username in header
        open_header.verify_success_sign_in(basic_user.login)
        self.log.info(f"Account name {basic_user.login} was verified, Sign In with Enter key is successfully")

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
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Move to the Header
        open_header = open_start_page.from_start_page_to_header()
        self.log.info(f"Header is opened")

        # Verify the username in header
        open_header.verify_success_sign_in(basic_user.login.replace(" ", ""))
        self.log.info(f"Spaces disappear. Account name {basic_user.login} was verified, Sign In is successfully")

    def test_sign_in_login_uppercase(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill Login with uppercase
        - Fill Password with lowercase, click Sign In button
        - Verify successful Sign In
        """

        # Fill Login and Password with spaces before and after them
        basic_user = User(login="SEOPAY-QA-CEO", password="uGwql6dqvC9fAFwC")
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Move to the Header
        open_header = open_start_page.from_start_page_to_header()
        self.log.info(f"Header is opened")

        # Verify the username in header
        open_header.verify_success_sign_in(basic_user.login.lower())
        self.log.info(f"Account name {basic_user.login.lower()} was verified, Sign In with login in uppercase order is successfully")

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
        open_start_page.st_pg_sign_in.incorrect_sign_in(basic_user)

        # Verify error message for login
        open_start_page.st_pg_sign_in.verify_empty_login_message()
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
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Verify error message for login
        open_start_page.st_pg_sign_in.verify_empty_login_message()
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
        open_start_page.st_pg_sign_in.incorrect_sign_in(basic_user)

        # Verify error message for password
        open_start_page.st_pg_sign_in.verify_empty_password_message()
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
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Verify error message for password
        open_start_page.st_pg_sign_in.verify_empty_password_message()
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
        basic_user.random_incorrect_user(login=basic_user.login, password="uGwql6dqvC9fAFwC")
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Verify message for incorrect credentials
        open_start_page.st_pg_sign_in.verify_incorrect_credentials_message()
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
        basic_user.random_incorrect_user(login="seopay-qa-ceo", password=basic_user.password)
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Verify message for incorrect credentials
        open_start_page.st_pg_sign_in.verify_incorrect_credentials_message()
        self.log.info(f"Password {basic_user.password} is incorrect. Error message appears")

    def test_incorrect_password_uppercase(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login, correct password with uppercase order
        - Click Sign In button, verify error message
        """

        # Log in with incorrect login
        basic_user = User()
        basic_user.random_incorrect_user(login="seopay-qa-ceo", password="UGWQL6DQVC9FAFWC")
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Verify message for incorrect credentials
        open_start_page.st_pg_sign_in.verify_incorrect_credentials_message()
        self.log.info(f" Correct password in uppercase order {basic_user.password} is incorrect. Error message appears")

    def test_incorrect_password_lowercase(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login, correct password with lowercase order
        - Click Sign In button, verify error message
        """

        # Log in with incorrect login
        basic_user = User()
        basic_user.random_incorrect_user(login="seopay-qa-ceo", password="ugwql6dqvc9fafwc")
        open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)

        # Verify message for incorrect credentials
        open_start_page.st_pg_sign_in.verify_incorrect_credentials_message()
        self.log.info(f" Correct password in lowercase order {basic_user.password} is incorrect. Error message appears")

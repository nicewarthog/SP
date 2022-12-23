import logging


class TestSidebar:
    log = logging.getLogger("Sidebar")

    # Teams button

    def test_teams_customer(self, sign_in_customer, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Customer

        Steps:
        - Verify Teams button does not display
        """

        # Open sidebar
        open_sidebar = open_start_page.from_start_page_to_sidebar()

        # Verify Teams button does not display on sidebar
        open_sidebar.verify_teams_button_is_not_exist()
        self.log.info("Teams button does not display on sidebar")

    def test_teams_team_lead(self, sign_in_team_lead, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Team Lead

        Steps:
        - Verify Teams button does not display
        """

        # Open sidebar
        open_sidebar = open_start_page.from_start_page_to_sidebar()

        # Verify Teams button does not display on sidebar
        open_sidebar.verify_teams_button_is_not_exist()
        self.log.info("Teams button does not display on sidebar")

    def test_teams_moderator(self, sign_in_moderator, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Moderator

        Steps:
        - Verify Teams button does not display
        """

        # Open sidebar
        open_sidebar = open_start_page.from_start_page_to_sidebar()

        # Verify Teams button does not display on sidebar
        open_sidebar.verify_teams_button_is_not_exist()
        self.log.info("Teams button does not display on sidebar")

    def test_teams_head_department(self, sign_in_head_dep, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Head of department

        Steps:
        - Verify Teams button does not display
        """

        # Open sidebar
        open_sidebar = open_start_page.from_start_page_to_sidebar()

        # Verify Teams button does not display on sidebar
        open_sidebar.verify_teams_button_is_not_exist()
        self.log.info("Teams button does not display on sidebar")

    def test_teams_analyst(self, sign_in_analyst, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Analyst

        Steps:
        - Verify Teams button icon and title
        """

        # Log Out from account
        open_sidebar = open_start_page.from_start_page_to_sidebar()

        # Verify the h3 in authorisation form of StartPage
        open_sidebar.verify_teams_button_elements()
        self.log.info("Teams button icon and title are correct")

    def test_teams_admin(self, sign_in_admin, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Admin

        Steps:
        - Verify Teams button icon and title
        """

        # Log Out from account
        open_sidebar = open_start_page.from_start_page_to_sidebar()

        # Verify the h3 in authorisation form of StartPage
        open_sidebar.verify_teams_button_elements()
        self.log.info("Teams button icon and title are correct")

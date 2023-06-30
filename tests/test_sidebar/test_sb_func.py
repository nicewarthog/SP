import logging


class TestSidebarFunc:
    log = logging.getLogger("Sidebar")

    # Teams button

    def test_customer_buttons(self, sign_in_customer, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Customer

        Steps:
        - Go to Sidebar
        - Verify Order create, My orders, Donors buttons are exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_order_create_button()
        self.log.info("Order create button is exist on Sidebar")

        open_sidebar.verify_my_orders_button()
        self.log.info("My order button is exist on Sidebar")

        open_sidebar.verify_donors_button()
        self.log.info("Donors button is exist on Sidebar")

    def test_not_customer_buttons(self, sign_in_customer, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Customer

        Steps:
        - Go to Sidebar
        - Verify Team orders, Dep orders, All orders, Export, Currency, GEO, Users, Teams buttons are exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_team_orders_button_not_exist()
        self.log.info("Team orders button is not exist on Sidebar")

        open_sidebar.verify_dep_orders_button_not_exist()
        self.log.info("Departments order button is not exist on Sidebar")

        open_sidebar.verify_all_orders_button_not_exist()
        self.log.info("All order button is not exist on Sidebar")

        open_sidebar.verify_export_button_not_exist()
        self.log.info("Export button is not exist on Sidebar")

        open_sidebar.verify_currency_button_not_exist()
        self.log.info("Currency button is not exist on Sidebar")

        open_sidebar.verify_geo_button_not_exist()
        self.log.info("GEO button is not exist on Sidebar")

        open_sidebar.verify_users_button_not_exist()
        self.log.info("Users button is not exist on Sidebar")

        open_sidebar.verify_teams_button_not_exist()
        self.log.info("Teams button is not exist on Sidebar")

    def test_team_lead_buttons(self, sign_in_team_lead, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Team lead

        Steps:
        - Go to Sidebar
        - Verify Order create, My orders, Team orders, Donors buttons are exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_order_create_button()
        self.log.info("Order create button is exist on Sidebar")

        open_sidebar.verify_my_orders_button()
        self.log.info("My orders button is exist on Sidebar")

        open_sidebar.verify_team_orders_button()
        self.log.info("Team orders button is exist on Sidebar")

        open_sidebar.verify_donors_button()
        self.log.info("Donors button is exist on Sidebar")

    def test_not_team_lead_buttons(self, sign_in_team_lead, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Team lead

        Steps:
        - Go to Sidebar
        - Verify Dep orders, All orders, Export, Currency, GEO, Users, Teams buttons are not exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_dep_orders_button_not_exist()
        self.log.info("Departments order button is not exist on Sidebar")

        open_sidebar.verify_all_orders_button_not_exist()
        self.log.info("All order button is not exist on Sidebar")

        open_sidebar.verify_export_button_not_exist()
        self.log.info("Export button is not exist on Sidebar")

        open_sidebar.verify_currency_button_not_exist()
        self.log.info("Currency button is not exist on Sidebar")

        open_sidebar.verify_geo_button_not_exist()
        self.log.info("GEO button is not exist on Sidebar")

        open_sidebar.verify_users_button_not_exist()
        self.log.info("Users button is not exist on Sidebar")

        open_sidebar.verify_teams_button_not_exist()
        self.log.info("Teams button is not exist on Sidebar")

    def test_moderator_buttons(self, sign_in_moderator, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Moderator

        Steps:
        - Go to Sidebar
        - Verify Order create, My orders, Department orders, Donors, GEO buttons are exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_order_create_button()
        self.log.info("Order create button is exist on Sidebar")

        open_sidebar.verify_my_orders_button()
        self.log.info("My order button is exist on Sidebar")

        open_sidebar.verify_dep_orders_button()
        self.log.info("Departments order button is exist on Sidebar")

        open_sidebar.verify_donors_button()
        self.log.info("Donors button is exist on Sidebar")

        open_sidebar.verify_geo_button()
        self.log.info("GEO button is exist on Sidebar")

    def test_not_moderator_buttons(self, sign_in_moderator, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Moderator

        Steps:
        - Go to Sidebar
        - Verify Team orders, All orders, Export, Currency, Users, Teams buttons are not exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_team_orders_button_not_exist()
        self.log.info("Team orders button is not exist on Sidebar")

        open_sidebar.verify_all_orders_button_not_exist()
        self.log.info("All order button is not exist on Sidebar")

        open_sidebar.verify_export_button_not_exist()
        self.log.info("Export button is not exist on Sidebar")

        open_sidebar.verify_currency_button_not_exist()
        self.log.info("Currency button is not exist on Sidebar")

        open_sidebar.verify_users_button_not_exist()
        self.log.info("Users button is not exist on Sidebar")

        open_sidebar.verify_teams_button_not_exist()
        self.log.info("Teams button is not exist on Sidebar")

    def test_analyst_buttons(self, sign_in_analyst, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Analyst

        Steps:
        - Go to Sidebar
        - Verify Order create, My orders, All orders, Export, Currency, Donors, Users, Teams buttons are exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_order_create_button()
        self.log.info("Order create button is exist on Sidebar")

        open_sidebar.verify_my_orders_button()
        self.log.info("My order button is exist on Sidebar")

        open_sidebar.verify_all_orders_button()
        self.log.info("All order button is exist on Sidebar")

        open_sidebar.verify_export_button()
        self.log.info("Export button is exist on Sidebar")

        open_sidebar.verify_currency_button()
        self.log.info("Currency button is exist on Sidebar")

        open_sidebar.verify_donors_button()
        self.log.info("Donors button is exist on Sidebar")

        open_sidebar.verify_users_button()
        self.log.info("Users button is exist on Sidebar")

        open_sidebar.verify_teams_button()
        self.log.info("Teams button is exist on Sidebar")

    def test_not_analyst_buttons(self, sign_in_analyst, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Analyst

        Steps:
        - Go to Sidebar
        - Verify Dep orders, Team orders, GEO buttons are not exist buttons are not exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_team_orders_button_not_exist()
        self.log.info("Team orders button is not exist on Sidebar")

        open_sidebar.verify_dep_orders_button_not_exist()
        self.log.info("Dep orders button is not exist on Sidebar")

        open_sidebar.verify_geo_button_not_exist()
        self.log.info("GEO button is exist on Sidebar")

    def test_head_dep_buttons(self, sign_in_head_dep, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Head of department

        Steps:
        - Go to Sidebar
        - Verify Order create, My orders, Department orders, Export, Donors buttons are exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_order_create_button()
        self.log.info("Order create button is exist on Sidebar")

        open_sidebar.verify_my_orders_button()
        self.log.info("My order button is exist on Sidebar")

        open_sidebar.verify_dep_orders_button()
        self.log.info("Departments order button is exist on Sidebar")

        open_sidebar.verify_export_button()
        self.log.info("Export button is exist on Sidebar")

        open_sidebar.verify_donors_button()
        self.log.info("Donors button is exist on Sidebar")

    def test_not_head_dep_buttons(self, sign_in_head_dep, open_start_page):
        """
        Fixture:
        - Open Start Page
        - Sign In with Head of department

        Steps:
        - Go to Sidebar
        - Verify Team orders, All orders, Currency, GEO, Users, Teams buttons are not exist on Sidebar
        """

        open_sidebar = open_start_page.from_start_page_to_sidebar()

        open_sidebar.verify_team_orders_button_not_exist()
        self.log.info("Team orders button is not exist on Sidebar")

        open_sidebar.verify_all_orders_button_not_exist()
        self.log.info("All order button is not exist on Sidebar")

        open_sidebar.verify_currency_button_not_exist()
        self.log.info("Currency button is not exist on Sidebar")

        open_sidebar.verify_geo_button_not_exist()
        self.log.info("GEO button is not exist on Sidebar")

        open_sidebar.verify_users_button_not_exist()
        self.log.info("Users button is not exist on Sidebar")

        open_sidebar.verify_teams_button_not_exist()
        self.log.info("Teams button is not exist on Sidebar")

import logging

import pytest


class TestOrdersAllPage:
    log = logging.getLogger("OrdersAllPage")

    @pytest.fixture(scope="function")
    def move_to_orders_all_page(self, open_start_page, sign_in_analyst):
        # Click OrdersAllPage button on sidebar
        open_start_page.sidebar.click_orders_all_button()
        return self.move_to_orders_all_page

    # Total Tables - sum in EUR

    def test_total_in_eur_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all EUR orders in EUR on the page
        - Verify that sum of all EUR orders in EUR equals the total EUR sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all EUR orders in EUR equals the total EUR sum in EUR
        open_orders_all_page.verify_sum_in_eur_eur()

    def test_total_in_eur_uah(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all UAH orders in EUR on the page
        - Verify that sum of all UAH orders in EUR equals the total UAH sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all UAH orders in EUR equals the total UAH sum in EUR
        open_orders_all_page.verify_sum_in_eur_uah()

    def test_total_in_eur_gbp(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all GBP orders in EUR on the page
        - Verify that sum of all GBP orders in EUR equals the total GBP sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all GBP orders in EUR equals the total GBP sum in EUR
        open_orders_all_page.verify_sum_in_eur_gbp()

    def test_total_in_eur_rub(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all RUB orders in EUR on the page
        - Verify that sum of all RUB orders in EUR equals the total RUB sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all RUB orders in EUR equals the total RUB sum in EUR
        open_orders_all_page.verify_sum_in_eur_rub()

    def test_total_in_eur_usd(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all USD orders in EUR on the page
        - Verify that sum of all USD orders in EUR equals the total USD sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all USD orders in EUR equals the total USD sum in EUR
        open_orders_all_page.verify_sum_in_eur_usd()

    def test_total_in_eur_usdt(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all USDT orders in EUR on the page
        - Verify that sum of all USDT orders in EUR equals the total USDT sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all USDT orders in EUR equals the total USDT sum in EUR
        open_orders_all_page.verify_sum_in_eur_usdt()

    def test_total_sum_in_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all orders sum in eur on the page
        - Verify that sum of all orders in eur equals the total sum in eur
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum in EUR of all orders equals the total sum in EUR
        open_orders_all_page.verify_total_sum_in_eur_for_list()

    def test_sum_of_totals_in_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all currency totals in EUR in the table Sum in EUR
        - Verify that sum of all currency totals in EUR equals the total sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all currency totals in EUR equals the total sum in EUR
        open_orders_all_page.verify_sum_all_totals_for_currency()

    # Total Tables - sum in currency

    def test_total_price_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all products price in EUR currency on the page
        - Verify that sum of all orders in EUR currency equals the total price in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all orders in EUR currency equals the total price in EUR
        open_orders_all_page.verify_price_sum_eur()

    def test_total_price_usd(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all products price in USD currency on the page
        - Verify that sum of all orders in USD currency equals the total price in USD
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all orders in USD currency equals the total price in USD
        open_orders_all_page.verify_price_sum_usd()

    def test_total_price_usdt(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all products price in USDT currency on the page
        - Verify that sum of all orders in USDT currency equals the total price in USDT
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all orders in USDT currency equals the total price in USDT
        open_orders_all_page.verify_price_sum_usdt()

    def test_total_price_uah(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all products price in UAH currency on the page
        - Verify that sum of all orders in UAH currency equals the total price in UAH
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all orders in UAH currency equals the total price in UAH
        open_orders_all_page.verify_price_sum_uah()

    def test_total_price_gbp(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all products price in GBP currency on the page
        - Verify that sum of all orders in GBP currency equals the total price in GBP
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all orders in GBP currency equals the total price in GBP
        open_orders_all_page.verify_price_sum_gbp()

    def test_total_price_rub(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all products price in RUB currency on the page
        - Verify that sum of all orders in RUB currency equals the total price in RUB
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all orders in RUB currency equals the total price in RUB
        open_orders_all_page.verify_price_sum_rub()

    # Total Tables - sum by teams
    def test_total_team_sum_in_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all orders sum in eur on the page
        - Verify that sum of all orders in eur equals the total sum in eur by teams
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all orders in eur equals the total sum in eur by order teams
        open_orders_all_page.verify_total_team_sum_for_list()

    def test_sum_of_team_totals_in_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all team totals in EUR in the table Sum by teams in EUR
        - Verify that sum of all team totals in EUR equals the total sum in the table Sum by teams in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all team totals in EUR equals the total sum in the table Sum by teams in EUR
        open_orders_all_page.verify_sum_all_totals_for_teams()

    # Total Tables - sum by order type
    def test_total_in_eur_content(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all content type orders in EUR on the page
        - Verify that sum of all content type orders in EUR equals the total content sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all content type orders in EUR equals the total content sum in EUR
        open_orders_all_page.verify_sum_type_content()

    def test_total_in_eur_link(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all link type orders in EUR on the page
        - Verify that sum of all link type orders in EUR equals the total link sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all link type orders in EUR equals the total link sum in EUR
        open_orders_all_page.verify_sum_type_link()

    def test_total_in_eur_other(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all other type orders in EUR on the page
        - Verify that sum of all other type other in EUR equals the total other sum in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all other type other in EUR equals the total other sum in EUR
        open_orders_all_page.verify_sum_type_other()

    def test_total_type_sum_in_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all orders sum in eur on the page
        - Verify that sum of all orders in eur equals the total sum in eur by order types
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all orders in eur equals the total sum in eur by order types
        open_orders_all_page.verify_total_type_sum_for_list()

    def test_sum_of_type_totals_in_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify sum of all type totals in EUR in the table Sum by types in EUR
        - Verify that sum of all type totals in EUR equals the total sum in the table Sum by types in EUR
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum of all type totals in EUR equals the total sum in the table Sum by types in EUR
        open_orders_all_page.verify_sum_all_totals_for_types()

    # Total tables - total sum in all tables
    def test_all_sum_equals(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify total sum in EUR of all tables
        - Verify that sum in EUR of all tables equals each other
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum in EUR of all tables equals each other
        open_orders_all_page.verify_all_sum_equals()

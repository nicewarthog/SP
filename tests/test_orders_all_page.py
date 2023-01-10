import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, ORDERS_ALL_URL
from pages.orders_all_page import OrdersAllPage
from pages.utils import User


class TestOrdersAllPage:
    log = logging.getLogger("OrdersAllPage")

    @pytest.fixture(scope="function")
    def open_orders_all_page(self):
        """Open start page"""
        # create driver
        driver = webdriver.Chrome(DRIVER_PATH)
        # open Orders All Page URL
        driver.get(ORDERS_ALL_URL)
        driver.maximize_window()
        driver.implicitly_wait(1)
        # Steps
        yield OrdersAllPage(driver)
        # Close driver
        driver.close()

    @pytest.fixture(scope="function")
    def sign_in_analyst_orders_all_page(self, open_orders_all_page):
        basic_user = User(login="seopay-qa-analyst", password="seopay-qa-analyst")
        open_orders_all_page.start_page.sign_in_with_button(basic_user)
        return self.sign_in_analyst_orders_all_page

    # Elements
    def test_move_to_orders_all_page(self, open_start_page, sign_in_analyst):
        """
        Fixtures:
        - Sign in with analyst role and open Start Page
        Steps:
        - Open Sidebar
        - Click Orders All button on Sidebar
        - Verify Orders All Page H1
        """

        # Open Start Page and click Orders All button on Sidebar
        open_start_page.sidebar.click_orders_all_button()
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify Orders All Page H1
        open_orders_all_page.verify_orders_all_page_h1()

    # Total Tables - sum in EUR

    def test_total_in_eur_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify the sum of all EUR orders in EUR equals the total EUR sum in EUR
        """

        open_orders_all_page.verify_sum_in_eur_eur()

    def test_total_in_eur_uah(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify the sum of all UAH orders in EUR equals the total UAH sum in EUR
        """

        open_orders_all_page.verify_sum_in_eur_uah()

    def test_total_in_eur_gbp(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all GBP orders in EUR equals the total GBP sum in EUR
        """

        open_orders_all_page.verify_sum_in_eur_gbp()

    def test_total_in_eur_rub(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all RUB orders in EUR equals the total RUB sum in EUR
        """

        open_orders_all_page.verify_sum_in_eur_rub()

    def test_total_in_eur_usd(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all USD orders in EUR equals the total USD sum in EUR
        """

        open_orders_all_page.verify_sum_in_eur_usd()

    def test_total_in_eur_usdt(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all USDT orders in EUR equals the total USDT sum in EUR
        """

        open_orders_all_page.verify_sum_in_eur_usdt()

    def test_total_sum_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in eur equals the total sum in eur
        """

        open_orders_all_page.verify_total_sum_in_eur_for_list()

    def test_sum_of_totals_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all currency totals in EUR equals the total sum in EUR
        """

        open_orders_all_page.verify_sum_all_totals_for_currency()

    # Total Tables - sum in currency

    def test_total_price_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in EUR currency equals the total price in EUR
        """

        open_orders_all_page.verify_price_sum_eur()

    def test_total_price_usd(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in USD currency equals the total price in USD
        """

        open_orders_all_page.verify_price_sum_usd()

    def test_total_price_usdt(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in USDT currency equals the total price in USDT
        """

        open_orders_all_page.verify_price_sum_usdt()

    def test_total_price_uah(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in UAH currency equals the total price in UAH
        """

        open_orders_all_page.verify_price_sum_uah()

    def test_total_price_gbp(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in GBP currency equals the total price in GBP
        """

        open_orders_all_page.verify_price_sum_gbp()

    def test_total_price_rub(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in RUB currency equals the total price in RUB
        """

        open_orders_all_page.verify_price_sum_rub()

    # Total Tables - sum by teams
    def test_total_team_sum_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in eur equals the total sum in eur by teams
        """

        open_orders_all_page.verify_total_team_sum_for_list()

    def test_sum_of_team_totals_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all team totals in EUR equals the total sum in the table Sum by teams in EUR
        """

        open_orders_all_page.verify_sum_all_totals_for_teams()

    # Total Tables - sum by order type
    def test_total_in_eur_content(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all content type orders in EUR equals the total content sum in EUR
        """

        open_orders_all_page.verify_sum_type_content()

    def test_total_in_eur_link(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all link type orders in EUR equals the total link sum in EUR
        """

        open_orders_all_page.verify_sum_type_link()

    def test_total_in_eur_other(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all other type other in EUR equals the total other sum in EUR
        """

        open_orders_all_page.verify_sum_type_other()

    def test_total_type_sum_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in eur equals the total sum in eur by order types
        """

        open_orders_all_page.verify_total_type_sum_for_list()

    def test_sum_of_type_totals_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all type totals in EUR equals the total sum in the table Sum by types in EUR
        """

        open_orders_all_page.verify_sum_all_totals_for_types()

    # Total tables - total sum in all tables
    def test_all_sum_equals(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum in EUR of all tables equals each other
        """

        open_orders_all_page.verify_all_sum_equals()

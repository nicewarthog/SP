import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, ORDERS_ALL_URL
from constants.orders_all_page import OrdersAllConst
from pages.orders_all_page import OrdersAllPage
from pages.utils import User

orders_all_const = OrdersAllConst


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

    # _________________________________Open page and Elements_________________________________
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
        self.log.info("Orders All Page H1 is exist and has correct text")

    # _________________________________Total Tables - sum in EUR_________________________________

    @pytest.mark.parametrize(["currency", "xpath_total", "xpath_list", "currency_log"],
                             [("uah", orders_all_const.TOTAL_IN_EUR_UAH_XPATH, orders_all_const.ORDERS_EUR_UAH_XPATH, "UAH"),
                              ("eur", orders_all_const.TOTAL_IN_EUR_EUR_XPATH, orders_all_const.ORDERS_EUR_EUR_XPATH, "EUR"),
                              ("gbp", orders_all_const.TOTAL_IN_EUR_GBP_XPATH, orders_all_const.ORDERS_EUR_GBP_XPATH, "GBP"),
                              ("usd", orders_all_const.TOTAL_IN_EUR_USD_XPATH, orders_all_const.ORDERS_EUR_USD_XPATH, "USD"),
                              ("usdt", orders_all_const.TOTAL_IN_EUR_USDT_XPATH, orders_all_const.ORDERS_EUR_USDT_XPATH, "USDT"),
                              ("rub", orders_all_const.TOTAL_IN_EUR_RUB_XPATH, orders_all_const.ORDERS_EUR_RUB_XPATH, "RUB"),
                              ("all_orders", orders_all_const.TOTAL_IN_EUR_ALL_XPATH, orders_all_const.ORDERS_EUR_ALL_XPATH, "all")])
    def test_total_in_eur_currency(self, open_orders_all_page, sign_in_analyst_orders_all_page, currency, xpath_total, xpath_list, currency_log):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum in EUR of all orders by one currency in the list equals the value in EUR for this currency in the table
        """

        open_orders_all_page.verify_sum_in_eur_currency_list(xpath_total, xpath_list, currency_log)

    def test_sum_of_currencies_total_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all currency totals in EUR in table equals the total sum in EUR in table
        """

        open_orders_all_page.verify_sum_in_eur_currency_totals()

    # _________________________________Total Tables - sum in currency_________________________________

    @pytest.mark.parametrize(["currency", "xpath_total", "xpath_list", "currency_log"],
                             [("eur", orders_all_const.TOTAL_IN_CURRENCY_EUR_XPATH, orders_all_const.ORDERS_PRICE_EUR_XPATH, "EUR"),
                              ("uah", orders_all_const.TOTAL_IN_CURRENCY_UAH_XPATH, orders_all_const.ORDERS_PRICE_UAH_XPATH, "UAH"),
                              ("gbp", orders_all_const.TOTAL_IN_CURRENCY_GBP_XPATH, orders_all_const.ORDERS_PRICE_GBP_XPATH, "GBP"),
                              ("usd", orders_all_const.TOTAL_IN_CURRENCY_USD_XPATH, orders_all_const.ORDERS_PRICE_USD_XPATH, "USD"),
                              ("rub", orders_all_const.TOTAL_IN_CURRENCY_RUB_XPATH, orders_all_const.ORDERS_PRICE_RUB_XPATH, "RUB")])
    def test_total_price(self, open_orders_all_page, sign_in_analyst_orders_all_page, currency, xpath_total, xpath_list, currency_log):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders by one currency in the list equals the value for this currency in the table
        """

        open_orders_all_page.verify_sum_price_list(xpath_total, xpath_list, currency_log)

    def test_total_price_usdt(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders in USDT currency equals the total price in USDT
        """

        open_orders_all_page.verify_sum_price_list_usdt()

    # _________________________________Total Tables - sum by teams_________________________________

    @pytest.mark.parametrize(["team", "xpath_total", "xpath_list", "team_log"],
                             [("all_int", orders_all_const.TOTAL_TEAMS_ALL_INT_XPATH, orders_all_const.ORDERS_TEAMS_ALL_INT_XPATH, "All INT"),
                              ("core_team", orders_all_const.TOTAL_TEAMS_CORE_TEAM_XPATH, orders_all_const.ORDERS_TEAMS_CORE_TEAM_XPATH, "Core Team"),
                              ("marketing", orders_all_const.TOTAL_TEAMS_MARKETING_XPATH, orders_all_const.ORDERS_TEAMS_MARKETING_XPATH, "Marketing"),
                              ("megadeph_int", orders_all_const.TOTAL_TEAMS_MEGADEPH_INT_XPATH, orders_all_const.ORDERS_TEAMS_MEGADEPH_INT_XPATH,
                               "MegaDeph INT"),
                              ("pl_team", orders_all_const.TOTAL_TEAMS_PL_TEAM_XPATH, orders_all_const.ORDERS_TEAMS_PL_TEAM_XPATH, "PL Team"),
                              ("slotozilla", orders_all_const.TOTAL_TEAMS_SLOTOZILLA_XPATH, orders_all_const.ORDERS_TEAMS_SLOTOZILLA_XPATH, "Slotozilla Team"),
                              ("the_first_int", orders_all_const.TOTAL_TEAMS_THE_FIRST_INT_XPATH, orders_all_const.ORDERS_TEAMS_THE_FIRST_INT_XPATH,
                               "The_First INT"),
                              ("x_team", orders_all_const.TOTAL_TEAMS_X_TEAM_XPATH, orders_all_const.ORDERS_TEAMS_X_TEAM_XPATH, "X-Team"),
                              ("product_team", orders_all_const.TOTAL_TEAMS_PRODUCT_TEAM_XPATH, orders_all_const.ORDERS_TEAMS_PRODUCT_TEAM_XPATH,
                               "Product Team"),
                              ("ys", orders_all_const.TOTAL_TEAMS_YS_XPATH, orders_all_const.ORDERS_TEAMS_YS_XPATH, "YS"),
                              ("satellites", orders_all_const.TOTAL_TEAMS_SATELLITES_XPATH, orders_all_const.ORDERS_TEAMS_SATELLITES_XPATH, "Satellites Team"),
                              ("ys_satellites", orders_all_const.TOTAL_TEAMS_YS_SATELLITES_XPATH, orders_all_const.ORDERS_TEAMS_YS_SATELLITES_XPATH,
                               "YS Satellites"),
                              ("megadeph_cis", orders_all_const.TOTAL_TEAMS_MEGADEPH_CIS_XPATH, orders_all_const.ORDERS_TEAMS_MEGADEPH_CIS_XPATH,
                               "MegaDeph CIS"),
                              ("other", orders_all_const.TOTAL_TEAMS_MEGADEPH_CIS_XPATH, orders_all_const.ORDERS_TEAMS_MEGADEPH_CIS_XPATH, "Other"),
                              ("pbn", orders_all_const.TOTAL_TEAMS_PBN_XPATH, orders_all_const.ORDERS_TEAMS_PBN_XPATH, "PBN"),
                              ("the_first_cis", orders_all_const.TOTAL_TEAMS_THE_FIRST_CIS_XPATH, orders_all_const.ORDERS_TEAMS_THE_FIRST_CIS_XPATH,
                               "The_First INT"),
                              ("top_seo", orders_all_const.TOTAL_TEAMS_TOP_SEO_XPATH, orders_all_const.ORDERS_TEAMS_TOP_SEO_XPATH, "TOP SEO"),
                              ("multi_seo", orders_all_const.TOTAL_TEAMS_MULTI_SEO_XPATH, orders_all_const.ORDERS_TEAMS_MULTI_SEO_XPATH, "Multi SEO"),
                              ("all_cis", orders_all_const.TOTAL_TEAMS_ALL_CIS_XPATH, orders_all_const.ORDERS_TEAMS_ALL_CIS_XPATH, "All CIS"),
                              ("dev_team", orders_all_const.TOTAL_TEAMS_DEV_TEAM_XPATH, orders_all_const.ORDERS_TEAMS_DEV_TEAM_XPATH, "Dev team"),
                              ("all_teams", orders_all_const.TOTAL_ALL_TEAMS_SUM_XPATH, orders_all_const.ORDERS_EUR_ALL_XPATH, "All teams")])
    def test_total_in_eur_teams(self, open_orders_all_page, sign_in_analyst_orders_all_page, team, xpath_total, xpath_list, team_log):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders by one team in the list equals the value for this team in the table
        """

        open_orders_all_page.verify_sum_teams_list(xpath_total, xpath_list, team_log)

    def test_sum_of_teams_total_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all team totals in EUR equals the total sum in the table Sum by teams in EUR
        """

        open_orders_all_page.verify_sum_all_totals_for_teams()

    # _________________________________Total Tables - sum by order type_________________________________

    @pytest.mark.parametrize(["type", "xpath_total", "xpath_list", "type_log"],
                             [("content", orders_all_const.TOTAL_TYPE_CONTENT_XPATH, orders_all_const.ORDERS_TYPE_CONTENT_XPATH, "Content type"),
                              ("link", orders_all_const.TOTAL_TYPE_LINK_XPATH, orders_all_const.ORDERS_TYPE_LINK_XPATH, "Link type"),
                              ("other", orders_all_const.TOTAL_TYPE_OTHER_XPATH, orders_all_const.ORDERS_TYPE_OTHER_XPATH, "Other type"),
                              ("all_types", orders_all_const.TOTAL_ALL_TYPES_SUM_XPATH, orders_all_const.ORDERS_EUR_ALL_XPATH, "All types")])
    def test_total_in_eur_types(self, open_orders_all_page, sign_in_analyst_orders_all_page, type, xpath_total, xpath_list, type_log):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all orders by one type in the list equals the value for this type in the table
        """

        open_orders_all_page.verify_sum_type(xpath_total, xpath_list, type_log)

    def test_sum_of_types_total_in_eur(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum of all type totals in EUR equals the total sum in the table Sum by types in EUR
        """

        open_orders_all_page.verify_sum_all_totals_for_types()

    # _________________________________Total tables - total sum in all tables_________________________________
    def test_all_sum_equals(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        - Fixtures: Sign in with analyst role and open Orders All Page
        - Steps: Verify that sum in EUR of all tables equals each other
        """

        open_orders_all_page.verify_all_sum_equals()

    # _________________________________Filters - Order type_________________________________

    def test_order_type_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Order type filter is exist and has correct title
        """

        open_orders_all_page.verify_order_type_filter()

    def test_order_type_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Order type filter is exist and has correct title
        """

        open_orders_all_page.verify_order_type_filter_values()

    @pytest.mark.parametrize(["type", "select_type", "type_text", "type_log"],
                             [("content", orders_all_const.FILTERS_ORDER_TYPE_CONTENT_XPATH, orders_all_const.FILTERS_ORDER_TYPE_CONTENT_TEXT, "Content"),
                              ("link", orders_all_const.FILTERS_ORDER_TYPE_LINK_XPATH, orders_all_const.FILTERS_ORDER_TYPE_LINK_TEXT, "Link"),
                              ("other", orders_all_const.FILTERS_ORDER_TYPE_OTHER_XPATH, orders_all_const.FILTERS_ORDER_TYPE_OTHER_TEXT, "Other")])
    def test_order_type_correct_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page, type, select_type, type_text, type_log):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Order type filter is exist and has correct title
        """

        open_orders_all_page.verify_order_type_filtration(select_type, type_text, type_log)

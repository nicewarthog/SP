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

    # @pytest.fixture(scope="function")
    # def paginator_select_300(self, open_orders_all_page):
    #     open_orders_all_page.click_paginator_300()
    #     return self.paginator_select_300

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

    # _________________________________FILTERS/FILTERS/FILTERS_________________________________

    # _________________________________Filters - Payment System Details_________________________________

    def test_account_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Account filter is exist and has correct title
        """

        open_orders_all_page.verify_account_filter()

    # _________________________________Filters - Service Name_________________________________

    def test_serv_name_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Service Name filter is exist and has correct title
        """

        open_orders_all_page.verify_serv_name_filter()

    def test_serv_name_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Get random Service Name from orders list
        - Input this Service Name to the Service Name filter
        - Verify there are only orders with selected Service Name on the page
        """

        open_orders_all_page.verify_serv_name_filtration()

    # _________________________________Filters - Payment System_________________________________

    def test_pay_sys_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Payment System filter is exist and has correct title
        """

        open_orders_all_page.verify_pay_sys_filter()

    def test_pay_sys_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Payment System filter has correct values - Card, Webmoney, Bitcoin, USDT TRC20, USDT ERC20, Skrill, Neteller, Paypal, Qiwi, Capitalist
        """

        open_orders_all_page.verify_pay_sys_filter_values()

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
        Steps: Verify Order type filter has correct values - Content, Link, Other
        """

        open_orders_all_page.verify_order_type_filter_values()

    @pytest.mark.parametrize(["type", "select_type", "type_text", "type_log"],
                             [("content", orders_all_const.FILTERS_ORDER_TYPE_CONTENT_XPATH, orders_all_const.FILTERS_ORDER_TYPE_CONTENT_TEXT, "Content"),
                              ("link", orders_all_const.FILTERS_ORDER_TYPE_LINK_XPATH, orders_all_const.FILTERS_ORDER_TYPE_LINK_TEXT, "Link"),
                              ("other", orders_all_const.FILTERS_ORDER_TYPE_OTHER_XPATH, orders_all_const.FILTERS_ORDER_TYPE_OTHER_TEXT, "Other")])
    def test_order_type_correct_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page, type, select_type, type_text, type_log):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Select Content, Link, Other values in Order type selector
        - Verify that all orders in the list have Content, Link or Other type
        """

        open_orders_all_page.verify_order_type_filtration(select_type, type_text, type_log)

    # _________________________________Filters - Departments_________________________________

    def test_departments_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Departments filter is exist and has correct title
        """

        open_orders_all_page.verify_departments_filter()

    def test_departments_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Departments filter has correct values - INT iGaming Media Project, INT Products, INT Satellites, CIS iGaming Media Project, CIS Products,
        CIS general
        """

        open_orders_all_page.open_departments_filter()
        open_orders_all_page.verify_departments_filter_values()

    # _________________________________Filters - Teams_________________________________

    def test_teams_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter is exist and has correct title
        """

        open_orders_all_page.verify_teams_filter()

    def test_teams_int_gmp_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for INT iGaming Media Project department has correct values - MegaDeph INT, The_First INT, All INT, Marketing, PL Team,
        X-Team, Core Team, Slotozilla Team
        """

        open_orders_all_page.open_departments_filter()
        open_orders_all_page.verify_teams_int_gmp_filter_values()

    def test_teams_int_prod_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for INT Products department has correct values - Product Team, YS
        """

        open_orders_all_page.open_departments_filter()
        open_orders_all_page.verify_teams_int_prod_filter_values()

    def test_teams_int_sat_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter INT Satellites department has correct values - YS Satellites, Satellites Team
        """

        open_orders_all_page.open_departments_filter()
        open_orders_all_page.verify_teams_int_sat_filter_values()

    def test_teams_cis_gmp_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for CIS iGaming Media Project department has correct values - The_First CIS, MegaDeph CIS, PBN, Other
        """

        open_orders_all_page.open_departments_filter()
        open_orders_all_page.verify_teams_cis_gmp_filter_values()

    def test_teams_cis_prod_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for CIS Products department has correct values - TOP SEO, Multi SEO
        """

        open_orders_all_page.open_departments_filter()
        open_orders_all_page.verify_teams_cis_prod_filter_values()

    def test_teams_cis_general_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for CIS General department has correct values - All CIS, Dev team
        """

        open_orders_all_page.open_departments_filter()
        open_orders_all_page.verify_teams_cis_general_filter_values()

    # _________________________________Filters - Updated by role_________________________________

    def test_updated_by_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Updated By filter is exist and has correct title
        """

        open_orders_all_page.verify_updated_by_filter()

    def test_updated_by_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Updated By filter has correct values - Заказчик, Руководитель команды, Модератор, Аналитик, Руководитель отдела, СОО/СЕО
        """

        open_orders_all_page.verify_updated_by_filter_values()

    @pytest.mark.parametrize(["role", "select_role", "role_text", "role_log"],
                             [("customer", orders_all_const.FILTERS_UPD_BY_CUSTOMER_XPATH, orders_all_const.FILTERS_UPD_BY_CUSTOMER_TEXT, "Заказчик"),
                              ("team_lead", orders_all_const.FILTERS_UPD_BY_TEAM_LEAD_XPATH, orders_all_const.FILTERS_UPD_BY_TEAM_LEAD_TEXT,
                               "Руководитель команды"),
                              ("moderator", orders_all_const.FILTERS_UPD_BY_MODERATOR_XPATH, orders_all_const.FILTERS_UPD_BY_MODERATOR_TEXT, "Модератор"),
                              ("analyst", orders_all_const.FILTERS_UPD_BY_ANALYST_XPATH, orders_all_const.FILTERS_UPD_BY_ANALYST_TEXT, "Аналитик"),
                              (
                              "head_dep", orders_all_const.FILTERS_UPD_BY_HEAD_DEP_XPATH, orders_all_const.FILTERS_UPD_BY_HEAD_DEP_TEXT, "Руководитель отдела"),
                              ("ceo_coo", orders_all_const.FILTERS_UPD_BY_CEO_COO_XPATH, orders_all_const.FILTERS_UPD_BY_CEO_COO_TEXT, "COO/CEO")])
    def test_updated_by_correct_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page, role, select_role, role_text, role_log):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Select value in Updated By selector
        - Verify that all orders in the list have Заказчик, Руководитель команды, Модератор, Аналитик, Руководитель отдела or СОО/СЕО value
        """

        open_orders_all_page.verify_updated_by_filtration(select_role, role_text, role_log)

    # _________________________________Filters - ID_________________________________

    def test_id_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify ID filter is exist and has correct title
        """

        open_orders_all_page.verify_id_filter()

    def test_id_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Get random ID from orders list
        - Input this ID to the ID filter
        - Verify there is only the order with selected ID on the page
        """

        open_orders_all_page.verify_filtration_id()

    # _________________________________Filters - Status_________________________________

    def test_status_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Verify Status filter is exist
        - Verify Status filter has default status - active
        """

        open_orders_all_page.verify_status_filter()

    def test_status_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Status filter has correct values - all, active, completed, declined, deleted, payment, prepayment
        """

        open_orders_all_page.verify_status_filter_values()

    @pytest.mark.parametrize(["status", "select_status", "status_value"],
                             [("Active", orders_all_const.FILTERS_STATUS_DEFAULT_XPATH, "Ожидает подтверждения"),
                              ("Completed", orders_all_const.FILTERS_STATUS_COMPLETED_XPATH, "Оплачен"),
                              ("Declined", orders_all_const.FILTERS_STATUS_DECLINED_XPATH, "Отклонен"),
                              ("Deleted", orders_all_const.FILTERS_STATUS_DELETED_XPATH, "Удален"),
                              ("Payment", orders_all_const.FILTERS_STATUS_PAYMENT_XPATH, "Ожидает оплаты")])
    def test_all_status_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page, status, select_status, status_value):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Select value in Status selector
        - Set 300 orders on the page via paginator
        - Verify that all orders in the list have active, completed, declined, deleted, payment status value
        """

        open_orders_all_page.status_filter_set_all(status, select_status)
        open_orders_all_page.paginator_300_orders()
        open_orders_all_page.verify_filtration_status_all(status_value)

    def test_prepayment_status_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Select value in Status selector
        - Set 300 orders on the page via paginator
        - Verify that all orders in the list have prepayment values
        """

        open_orders_all_page.status_filter_set_prepayment()
        open_orders_all_page.paginator_300_orders()
        open_orders_all_page.verify_filtration_status_prepayment()

import logging

import pytest

from constants.orders_all_page.all_pg_filters import OrdersAllFiltersConst

orders_all_filters_const = OrdersAllFiltersConst


class TestOrdersAllFilters:
    log = logging.getLogger("OrdersAllPageFilters")

    # @pytest.fixture(scope="function")
    # def paginator_select_300(self, open_orders_all_page):
    #     open_orders_all_page.click_paginator_300()
    #     return self.paginator_select_300

    # _________________________________Filters - Payment System Details_________________________________

    def test_account_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Account filter is exist and has correct title
        """

        open_orders_all_page.all_pg_filters.verify_account_filter()

    # _________________________________Filters - Service Name_________________________________

    def test_serv_name_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Service Name filter is exist and has correct title
        """

        open_orders_all_page.all_pg_filters.verify_serv_name_filter()

    def test_serv_name_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Get random Service Name from orders list
        - Input this Service Name to the Service Name filter
        - Verify there are only orders with selected Service Name on the page
        """

        open_orders_all_page.all_pg_filters.verify_serv_name_filtration()

    # _________________________________Filters - Payment System_________________________________

    def test_pay_sys_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Payment System filter is exist and has correct title
        """

        open_orders_all_page.all_pg_filters.verify_pay_sys_filter()

    def test_pay_sys_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        +++Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Payment System filter has correct values - Bank Transfer, Bitcoin, Capitalist, Card, Neteller, Paypal, Paypal Invoice, Qiwi, Skrill,
        USDT ERC20, USDT TRC20, Webmoney
        """

        open_orders_all_page.all_pg_filters.verify_pay_sys_filter_values()

    # _________________________________Filters - Order type_________________________________

    def test_order_type_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Order type filter is exist and has correct title
        """

        open_orders_all_page.all_pg_filters.verify_order_type_filter()

    def test_order_type_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Order type filter has correct values - Content, Link, Other
        """

        open_orders_all_page.all_pg_filters.verify_order_type_filter_values()

    @pytest.mark.parametrize(["type", "select_type", "type_text", "type_log"],
                             [("content", orders_all_filters_const.FILTERS_ORDER_TYPE_CONTENT_XPATH, orders_all_filters_const.FILTERS_ORDER_TYPE_CONTENT_TEXT,
                               "Content"),
                              ("link", orders_all_filters_const.FILTERS_ORDER_TYPE_LINK_XPATH, orders_all_filters_const.FILTERS_ORDER_TYPE_LINK_TEXT, "Link"),
                              ("other", orders_all_filters_const.FILTERS_ORDER_TYPE_OTHER_XPATH, orders_all_filters_const.FILTERS_ORDER_TYPE_OTHER_TEXT,
                               "Other")])
    def test_order_type_correct_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page, type, select_type, type_text, type_log):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Select Content, Link, Other values in Order type selector
        - Verify that all orders in the list have Content, Link or Other type
        """

        open_orders_all_page.all_pg_filters.verify_order_type_filtration(select_type, type_text, type_log)

    # _________________________________Filters - Departments_________________________________

    def test_departments_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Departments filter is exist and has correct title
        """

        open_orders_all_page.all_pg_filters.verify_departments_filter()

    def test_departments_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Departments filter has correct values - INT iGaming Media Project, INT Products, INT Satellites, CIS iGaming Media Project, CIS Products,
        CIS general
        """

        open_orders_all_page.all_pg_filters.open_departments_filter()
        open_orders_all_page.all_pg_filters.verify_departments_filter_values()

    # _________________________________Filters - Teams_________________________________

    def test_teams_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter is exist and has correct title
        """

        open_orders_all_page.all_pg_filters.verify_teams_filter()

    def test_teams_int_gmp_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for INT iGaming Media Project department has correct values - MegaDeph INT, The_First INT, All INT, Marketing, PL Team,
        X-Team, Core Team, Slotozilla Team
        """

        open_orders_all_page.all_pg_filters.open_departments_filter()
        open_orders_all_page.all_pg_filters.verify_teams_int_gmp_filter_values()

    def test_teams_int_prod_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for INT Products department has correct values - Product Team, YS
        """

        open_orders_all_page.all_pg_filters.open_departments_filter()
        open_orders_all_page.all_pg_filters.verify_teams_int_prod_filter_values()

    def test_teams_int_sat_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter INT Satellites department has correct values - YS Satellites, Satellites Team
        """

        open_orders_all_page.all_pg_filters.open_departments_filter()
        open_orders_all_page.all_pg_filters.verify_teams_int_sat_filter_values()

    def test_teams_cis_gmp_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for CIS iGaming Media Project department has correct values - The_First CIS, MegaDeph CIS, PBN, Other
        """

        open_orders_all_page.all_pg_filters.open_departments_filter()
        open_orders_all_page.all_pg_filters.verify_teams_cis_gmp_filter_values()

    def test_teams_cis_prod_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for CIS Products department has correct values - TOP SEO, Multi SEO
        """

        open_orders_all_page.all_pg_filters.open_departments_filter()
        open_orders_all_page.all_pg_filters.verify_teams_cis_prod_filter_values()

    def test_teams_cis_general_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Teams filter for CIS General department has correct values - All CIS, Dev team
        """

        open_orders_all_page.all_pg_filters.open_departments_filter()
        open_orders_all_page.all_pg_filters.verify_teams_cis_general_filter_values()

    # _________________________________Filters - Updated by role_________________________________

    def test_updated_by_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Updated By filter is exist and has correct title
        """

        open_orders_all_page.all_pg_filters.verify_updated_by_filter()

    def test_updated_by_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Updated By filter has correct values - Замовник, Керівник команди, Модератор, Аналітик, Керівник департаменту, COO/CEO
        """

        open_orders_all_page.all_pg_filters.verify_updated_by_filter_values()

    @pytest.mark.parametrize(["role", "select_role", "role_text", "role_log"],
                             [("customer", orders_all_filters_const.FILTERS_UPD_BY_CUSTOMER_XPATH, orders_all_filters_const.FILTERS_UPD_BY_CUSTOMER_TEXT,
                               "Замовник"),
                              ("team_lead", orders_all_filters_const.FILTERS_UPD_BY_TEAM_LEAD_XPATH, orders_all_filters_const.FILTERS_UPD_BY_TEAM_LEAD_TEXT,
                               "Керівник команди"),
                              ("moderator", orders_all_filters_const.FILTERS_UPD_BY_MODERATOR_XPATH, orders_all_filters_const.FILTERS_UPD_BY_MODERATOR_TEXT,
                               "Модератор"),
                              ("analyst", orders_all_filters_const.FILTERS_UPD_BY_ANALYST_XPATH, orders_all_filters_const.FILTERS_UPD_BY_ANALYST_TEXT,
                               "Аналітик"),
                              (
                                      "head_dep", orders_all_filters_const.FILTERS_UPD_BY_HEAD_DEP_XPATH, orders_all_filters_const.FILTERS_UPD_BY_HEAD_DEP_TEXT,
                                      "Керівник департаменту"),
                              ("ceo_coo", orders_all_filters_const.FILTERS_UPD_BY_CEO_COO_XPATH, orders_all_filters_const.FILTERS_UPD_BY_CEO_COO_TEXT,
                               "COO/CEO")])
    def test_updated_by_correct_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page, role, select_role, role_text, role_log):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Select value in Updated By selector
        - Verify that all orders in the list have Замовник, Керівник команди, Модератор, Аналітик, Керівник департаменту or COO/CEO value
        """

        open_orders_all_page.all_pg_filters.verify_updated_by_filtration(select_role, role_text, role_log)

    # _________________________________Filters - ID_________________________________

    def test_id_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify ID filter is exist and has correct title
        """

        open_orders_all_page.all_pg_filters.verify_id_filter()

    def test_id_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Get random ID from orders list
        - Input this ID to the ID filter
        - Verify there is only the order with selected ID on the page
        """

        open_orders_all_page.all_pg_filters.verify_filtration_id()

    # _________________________________Filters - Status_________________________________

    def test_status_filter(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Verify Status filter is exist
        - Verify Status filter has default status - active
        """

        open_orders_all_page.all_pg_filters.verify_status_filter()

    def test_status_filter_values(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps: Verify Status filter has correct values - all, active, completed, declined, deleted, payment, prepayment, checking_prepayment
        """

        open_orders_all_page.all_pg_filters.verify_status_filter_values()

    @pytest.mark.parametrize(["status", "select_status", "status_value"],
                             [("Active", orders_all_filters_const.FILTERS_STATUS_DEFAULT_XPATH, "Очікує підтвердження"),
                              ("Completed", orders_all_filters_const.FILTERS_STATUS_COMPLETED_XPATH, "Сплачено"),
                              ("Declined", orders_all_filters_const.FILTERS_STATUS_DECLINED_XPATH, "Відхилено"),
                              ("Deleted", orders_all_filters_const.FILTERS_STATUS_DELETED_XPATH, "Видалено"),
                              ("Payment", orders_all_filters_const.FILTERS_STATUS_PAYMENT_XPATH, "Очікує оплати"),
                              ("Checking Prepayment", orders_all_filters_const.FILTERS_STATUS_CH_PREPAYMENT_XPATH, "Очікує перевірки передоплати")])
    def test_all_status_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page, status, select_status, status_value):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Select value in Status selector
        - Set 300 orders on the page via paginator
        - Verify that all orders in the list have active, completed, declined, deleted, payment, checking_prepayment status value
        """

        open_orders_all_page.all_pg_filters.status_filter_set_all(status, select_status)
        open_orders_all_page.all_pg_elements.paginator_300_orders()
        open_orders_all_page.all_pg_filters.verify_filtration_status_all(status_value)

    def test_prepayment_status_filtration(self, open_orders_all_page, sign_in_analyst_orders_all_page):
        """
        Fixtures: Sign in with analyst role and open Order All page
        Steps:
        - Select value in Status selector
        - Set 300 orders on the page via paginator
        - Verify that all orders in the list have prepayment values
        """

        open_orders_all_page.all_pg_filters.status_filter_set_prepayment()
        open_orders_all_page.all_pg_elements.paginator_300_orders()
        open_orders_all_page.all_pg_filters.verify_filtration_status_prepayment()

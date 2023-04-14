import logging
import random
from decimal import *
from time import sleep

from pages.base_page import BasePage
from pages.utils import wait_until_ok


class OrdersAllPage(BasePage):
    log = logging.getLogger("[OrdersAllPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.orders_all_page import OrdersAllConst
        self.orders_all_constants = OrdersAllConst
        from pages.sidebar import Sidebar
        self.sidebar = Sidebar(self.driver)
        from pages.start_page import StartPage
        self.start_page = StartPage(self.driver)

    # _________________________________Open page and Elements_________________________________

    def verify_orders_all_page_h1(self):
        """Verify the Orders All Page h1 has correct text"""
        assert self.get_element_text(self.orders_all_constants.H1_XPATH) == self.orders_all_constants.H1_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.H1_XPATH)}"

    # _________________________________Paginator_________________________________
    def paginator_300_orders(self):
        """Open paginator, select value - 300 and click"""
        self.action_chains_move_and_click(self.orders_all_constants.PAGINATOR_XPATH)
        self.action_chains_move_and_click(self.orders_all_constants.PAGINATOR_SELECTOR_300_XPATH)

    # _________________________________Total tables - sum in EUR_________________________________

    def verify_sum_in_eur_currency_list(self, xpath_total, xpath_list, currency_log):
        total_in_eur_one_currency = self.get_element_text(xpath=xpath_total)
        if self.is_exist(xpath=xpath_list):
            all_orders_sum_in_eur_one_currency = self.wait_until_all_displayed(xpath=xpath_list)
            one_order_sum_in_eur_one_currency = [Decimal(sum_in_eur_one_currency.text) for sum_in_eur_one_currency in all_orders_sum_in_eur_one_currency]
            assert sum(one_order_sum_in_eur_one_currency) == Decimal(total_in_eur_one_currency), \
                f"Actual {currency_log} orders sum in EUR = {sum(one_order_sum_in_eur_one_currency)}, total value for {currency_log} in EUR = {total_in_eur_one_currency}"
            self.log.info(
                f"{currency_log} orders sum in EUR - {sum(one_order_sum_in_eur_one_currency)} = total {currency_log} sum in EUR - {total_in_eur_one_currency}")
        else:
            assert int(total_in_eur_one_currency) == 0
            self.log.warning(f"The list has no orders in EUR. Total {currency_log} sum in EUR = {total_in_eur_one_currency}")

    def verify_sum_in_eur_currency_totals(self):
        all_totals_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.TOTAL_IN_EUR_TABLE_VALUES_XPATH)
        one_total_sum_in_eur = [Decimal(total_in_eur.text) for total_in_eur in all_totals_sum_in_eur]
        total_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_IN_EUR_ALL_XPATH)
        assert sum(one_total_sum_in_eur) == Decimal(
            total_sum_in_eur), f"Actual all totals sum in EUR {sum(one_total_sum_in_eur)}, total sum in EUR {Decimal(total_sum_in_eur)}"
        self.log.info(f"All totals sum in EUR - {sum(one_total_sum_in_eur)} = total sum in EUR - {Decimal(total_sum_in_eur)}")

    # _________________________________Total tables - sum in currency_________________________________

    def verify_sum_price_list(self, xpath_total, xpath_list, currency_log):
        total_price_one_currency = self.get_element_text(xpath=xpath_total)
        if self.is_exist(xpath=xpath_list):
            all_orders_price_one_currency = self.wait_until_all_displayed(xpath=xpath_list)
            one_order_price_one_currency = [Decimal(price_one_currency.text[:-4]) for price_one_currency in all_orders_price_one_currency]
            assert sum(one_order_price_one_currency) == Decimal(total_price_one_currency), \
                f"Actual all orders price - {sum(one_order_price_one_currency)} {currency_log}, total price - {total_price_one_currency} {currency_log}"
            self.log.info(f"All orders price - {sum(one_order_price_one_currency)} {currency_log} = total price - {total_price_one_currency} {currency_log}")
        else:
            assert int(total_price_one_currency) == 0
            self.log.warning(f"The list has no orders in {currency_log}. Total price in {currency_log} = {total_price_one_currency}")

    def verify_sum_price_list_usdt(self):
        total_price_usdt = self.get_element_text(xpath=self.orders_all_constants.TOTAL_IN_CURRENCY_USDT_XPATH)
        if self.is_exist(xpath=self.orders_all_constants.ORDERS_PRICE_USDT_XPATH):
            all_orders_price_usdt = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_PRICE_USDT_XPATH)
            one_order_price_usdt = [Decimal(price_usdt.text[:-5]) for price_usdt in all_orders_price_usdt]
            assert sum(one_order_price_usdt) == Decimal(total_price_usdt), \
                f"Actual all orders price - {sum(one_order_price_usdt)} USDT, total price - {total_price_usdt} USDT"
            self.log.info(f"All orders price - {sum(one_order_price_usdt)} USDT = total price - {total_price_usdt} USDT")
        else:
            assert int(total_price_usdt) == 0
            self.log.warning(f"The list has no orders in USDT. Total price in USDT = {total_price_usdt}")

    # _________________________________Total tables - sum by teams_________________________________

    def verify_sum_teams_list(self, xpath_total, xpath_list, team_log):
        total_one_team = self.get_element_text(xpath=xpath_total)
        if self.is_exist(xpath=xpath_list):
            all_orders_sum_one_team = self.wait_until_all_displayed(xpath=xpath_list)
            one_order_sum_one_team = [Decimal(sum_one_team.text) for sum_one_team in all_orders_sum_one_team]
            assert sum(one_order_sum_one_team) == Decimal(total_one_team), \
                f"Actual {team_log} orders sum = {sum(one_order_sum_one_team)}, total {team_log} value = {total_one_team}"
            self.log.info(f"Sum of {team_log} orders - {sum(one_order_sum_one_team)} = total {team_log} value - {total_one_team}")
        else:
            assert int(total_one_team) == 0
            self.log.warning(f"The list has no {team_log} orders. Total {team_log} sum = {total_one_team}")

    def verify_sum_all_totals_for_teams(self):
        all_totals_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.TOTAL_ALL_TEAMS_VALUES_XPATH)
        one_total_sum_in_eur = [Decimal(total_in_eur.text) for total_in_eur in all_totals_sum_in_eur]
        total_team_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_ALL_TEAMS_SUM_XPATH)
        assert sum(one_total_sum_in_eur) == Decimal(
            total_team_sum_in_eur), f"Actual all totals sum in EUR {sum(one_total_sum_in_eur)}, total sum in EUR {Decimal(total_team_sum_in_eur)}"
        self.log.info(f"All totals sum in EUR - {sum(one_total_sum_in_eur)} = total sum in EUR - {Decimal(total_team_sum_in_eur)}")

    # _________________________________Total tables - sum by order type_________________________________
    def verify_sum_type(self, xpath_total, xpath_list, type_log):
        total_one_type = self.get_element_text(xpath=xpath_total)
        if self.is_exist(xpath=xpath_list):
            all_orders_sum_one_type = self.wait_until_all_displayed(xpath=xpath_list)
            one_order_sum_one_type = [Decimal(sum_one_type.text) for sum_one_type in all_orders_sum_one_type]
            assert sum(one_order_sum_one_type) == Decimal(total_one_type), \
                f"Actual {type_log} orders sum {sum(one_order_sum_one_type)}, total {type_log} value {Decimal(total_one_type)}"
            self.log.info(f"Sum of {type_log} orders - {sum(one_order_sum_one_type)} = total {type_log} value - {Decimal(total_one_type)}")
        else:
            assert int(total_one_type) == 0
            self.log.info(f"The list has no {type_log} orders. Total {type_log} sum = {total_one_type}")

    def verify_sum_all_totals_for_types(self):
        all_totals_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.TOTAL_ALL_TYPES_VALUES_XPATH)
        one_total_sum_in_eur = [Decimal(total_in_eur.text) for total_in_eur in all_totals_sum_in_eur]
        total_type_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_ALL_TYPES_SUM_XPATH)
        assert sum(one_total_sum_in_eur) == Decimal(
            total_type_sum_in_eur), f"Actual all totals sum in EUR {sum(one_total_sum_in_eur)}, total sum in EUR {Decimal(total_type_sum_in_eur)}"
        self.log.info(f"All totals sum in EUR - {sum(one_total_sum_in_eur)} = total sum in EUR - {Decimal(total_type_sum_in_eur)}")

    # _________________________________Total tables - total sum in all tables_________________________________
    def verify_all_sum_equals(self):
        currency_total_sum_in_eur = self.get_element_text(xpath=self.orders_all_constants.TOTAL_IN_EUR_ALL_XPATH)
        team_total_sum_in_eur = self.get_element_text(xpath=self.orders_all_constants.TOTAL_ALL_TEAMS_SUM_XPATH)
        type_total_sum_in_eur = self.get_element_text(xpath=self.orders_all_constants.TOTAL_ALL_TYPES_SUM_XPATH)
        assert float(currency_total_sum_in_eur) == float(team_total_sum_in_eur) == float(type_total_sum_in_eur), \
            f"Currency sum in EUR - {currency_total_sum_in_eur}, teams sum in EUR - {team_total_sum_in_eur}, types sum in EUR - {type_total_sum_in_eur}"
        self.log.info(f"Currency sum - {currency_total_sum_in_eur} = teams sum - {team_total_sum_in_eur} = types sum - {type_total_sum_in_eur}")

    # _________________________________FILTERS/FILTERS/FILTERS_________________________________

    # _________________________________Filters - Payment System Details_________________________________
    def verify_account_filter(self):
        """Verify Account filter is exist and has correct title"""
        assert self.get_element_text(self.orders_all_constants.FILTERS_ACCOUNT_TITLE_XPATH) == self.orders_all_constants.FILTERS_ACCOUNT_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_ACCOUNT_TITLE_XPATH)}"
        self.log.info(f"Account filter is exist, title is '{self.get_element_text(self.orders_all_constants.FILTERS_ACCOUNT_TITLE_XPATH)}'")

    # _________________________________Filters - Service Name_________________________________

    def verify_serv_name_filter(self):
        """Verify Service Name filter is exist and has correct title"""
        assert self.get_element_text(self.orders_all_constants.FILTERS_SERV_NAME_TITLE_XPATH) == self.orders_all_constants.FILTERS_SERV_NAME_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_SERV_NAME_TITLE_XPATH)}"
        self.log.info(f"Service Name filter is exist, title is '{self.get_element_text(self.orders_all_constants.FILTERS_SERV_NAME_TITLE_XPATH)}'")

    @wait_until_ok(5)
    def verify_serv_name_filtration(self):
        """Input random id from orders list to ID filter and verify filtration"""
        all_orders_list = self.wait_until_all_displayed(xpath=self.orders_all_constants.FILTERS_SERV_NAME_CELLS_XPATH)
        orders_serv_name = []
        for one_order in all_orders_list:
            if len(one_order.text) > 0:
                orders_serv_name.append(one_order.text)
        random_serv_name = random.choice(orders_serv_name)[:4]
        self.fill_field(xpath=self.orders_all_constants.FILTERS_SERV_NAME_XPATH, value=random_serv_name)
        self.log.info(f"Service Name value '{random_serv_name}' is selected")
        sleep(3)
        filtered_orders_list = self.wait_until_all_displayed(xpath=self.orders_all_constants.FILTERS_SERV_NAME_CELLS_XPATH)
        for one_filtered_order in filtered_orders_list:
            assert random_serv_name in one_filtered_order.text, \
                f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_SERV_NAME_CELLS_XPATH)}"
            self.log.info(f"The list has '{one_filtered_order.text}' order")
        self.log.info(f"The list has {len(filtered_orders_list)} order(s). All orders have Service Name value '{random_serv_name}'")

    # _________________________________Filters - Payment System_________________________________

    def verify_pay_sys_filter(self):
        """Verify Payment System filter is exist and has correct title"""
        assert self.get_element_text(self.orders_all_constants.FILTERS_PAY_SYS_TITLE_XPATH) == self.orders_all_constants.FILTERS_PAY_SYS_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_PAY_SYS_TITLE_XPATH)}"
        self.log.info(f"Payment System filter is exist, title is '{self.get_element_text(self.orders_all_constants.FILTERS_PAY_SYS_TITLE_XPATH)}'")

    def verify_pay_sys_filter_values(self):
        """Verify Payment System  filter has correct values - Card, Webmoney, Bitcoin, USDT TRC20, USDT ERC20, Skrill, Neteller, Paypal, Qiwi, Capitalist"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_PAY_SYS_XPATH)
        card_xpath = self.orders_all_constants.FILTERS_PAY_SYS_CARD_XPATH
        webmoney_xpath = self.orders_all_constants.FILTERS_PAY_SYS_WEBMONEY_XPATH
        bitcoin_xpath = self.orders_all_constants.FILTERS_PAY_SYS_BITCOIN_XPATH
        trc20_xpath = self.orders_all_constants.FILTERS_PAY_SYS_TRC20_XPATH
        erc20_xpath = self.orders_all_constants.FILTERS_PAY_SYS_ERC20_XPATH
        skrill_xpath = self.orders_all_constants.FILTERS_PAY_SYS_SKRILL_XPATH
        neteller_xpath = self.orders_all_constants.FILTERS_PAY_SYS_NETELLER_XPATH
        paypal_xpath = self.orders_all_constants.FILTERS_PAY_SYS_PAYPAL_XPATH
        qiwi_xpath = self.orders_all_constants.FILTERS_PAY_SYS_QIWI_XPATH
        capitalist_xpath = self.orders_all_constants.FILTERS_PAY_SYS_CAPITALIST_XPATH
        assert self.get_element_text(card_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_CARD_TEXT, f"Actual message: {self.get_element_text(card_xpath)}"
        assert self.get_element_text(
            webmoney_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_WEBMONEY_TEXT, f"Actual message: {self.get_element_text(webmoney_xpath)}"
        assert self.get_element_text(
            bitcoin_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_BITCOIN_TEXT, f"Actual message: {self.get_element_text(bitcoin_xpath)}"
        assert self.get_element_text(
            trc20_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_TRC20_TEXT, f"Actual message: {self.get_element_text(trc20_xpath)}"
        assert self.get_element_text(
            erc20_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_ERC20_TEXT, f"Actual message: {self.get_element_text(erc20_xpath)}"
        assert self.get_element_text(
            skrill_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_SKRILL_TEXT, f"Actual message: {self.get_element_text(skrill_xpath)}"
        assert self.get_element_text(
            neteller_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_NETELLER_TEXT, f"Actual message: {self.get_element_text(neteller_xpath)}"
        assert self.get_element_text(
            paypal_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_PAYPAL_TEXT, f"Actual message: {self.get_element_text(paypal_xpath)}"
        assert self.get_element_text(qiwi_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_QIWI_TEXT, f"Actual message: {self.get_element_text(qiwi_xpath)}"
        assert self.get_element_text(
            capitalist_xpath) == self.orders_all_constants.FILTERS_PAY_SYS_CAPITALIST_TEXT, f"Actual message: {self.get_element_text(capitalist_xpath)}"
        self.log.info(f"Payment System filter has {self.get_element_text(card_xpath)}, {self.get_element_text(webmoney_xpath)}, "
                      f"{self.get_element_text(bitcoin_xpath)}, {self.get_element_text(trc20_xpath)}, {self.get_element_text(erc20_xpath)}, "
                      f"{self.get_element_text(skrill_xpath)}, {self.get_element_text(neteller_xpath)}, {self.get_element_text(paypal_xpath)}, "
                      f"{self.get_element_text(qiwi_xpath)}, {self.get_element_text(capitalist_xpath)} values")

    # _________________________________Filters - Order type_________________________________

    def verify_order_type_filter(self):
        """Verify Order type filter is exist and has correct title"""
        assert self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_TITLE_XPATH) == self.orders_all_constants.FILTERS_ORDER_TYPE_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_TITLE_XPATH)}"
        self.log.info(f"Order type filter is exist, title is '{self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_TITLE_XPATH)}'")

    def verify_order_type_filter_values(self):
        """Verify Order type filter has correct values - Link, Content, Other"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_ORDER_TYPE_XPATH)
        assert self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_LINK_XPATH) == self.orders_all_constants.FILTERS_ORDER_TYPE_LINK_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_LINK_XPATH)}"
        assert self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_CONTENT_XPATH) == self.orders_all_constants.FILTERS_ORDER_TYPE_CONTENT_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_CONTENT_XPATH)}"
        assert self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_OTHER_XPATH) == self.orders_all_constants.FILTERS_ORDER_TYPE_OTHER_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_OTHER_XPATH)}"
        self.log.info(f"Order type filter has {self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_LINK_XPATH)}, "
                      f"{self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_CONTENT_XPATH)}, "
                      f"{self.get_element_text(self.orders_all_constants.FILTERS_ORDER_TYPE_OTHER_XPATH)} values")

    def verify_order_type_filtration(self, select_type, type_text, type_log):
        """Verify correctly filtration for Order type filter by values - Link, Content, Other """
        self.click(self.orders_all_constants.FILTERS_ORDER_TYPE_XPATH)
        self.action_chains_move_and_click(xpath=select_type)
        if self.is_exist(xpath=self.orders_all_constants.H2_NOT_FOUND_XPATH):
            assert self.get_element_text(self.orders_all_constants.H2_NOT_FOUND_XPATH) == self.orders_all_constants.H2_NOT_FOUND_TEXT
            self.log.warning(f"The list has no orders with type {type_log}. {self.get_element_text(self.orders_all_constants.H2_NOT_FOUND_XPATH)}")
        else:
            all_orders_list = self.wait_until_all_displayed(xpath=self.orders_all_constants.FILTERS_ORDER_TYPE_CELLS_XPATH)
            for one_order in all_orders_list:
                assert one_order.text[:4].lower() == type_text[:4].lower(), f"Actual Order type value - {one_order.text[:4].lower()}"
            self.log.info(f"The list has {len(all_orders_list)} orders. All orders in the list have type - {type_log}")

    # _________________________________Filters - Departments_________________________________

    def verify_departments_filter(self):
        """Verify Departments filter is exist and has correct title"""
        assert self.get_element_text(self.orders_all_constants.FILTERS_DEPS_TITLE_XPATH) == self.orders_all_constants.FILTERS_DEPS_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_DEPS_TITLE_XPATH)}"
        self.log.info(f"Order type filter is exist, title is '{self.get_element_text(self.orders_all_constants.FILTERS_DEPS_TITLE_XPATH)}'")

    def open_departments_filter(self):
        """Open Departments filter selector CIS general"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_DEPS_XPATH)

    def verify_departments_filter_values(self):
        """Verify Departments filter has correct values - INT iGaming Media Project, INT Products, INT Satellites, CIS iGaming Media Project, CIS Products,
        CIS general"""
        int_gmp_xpath = self.orders_all_constants.FILTERS_DEPS_INT_GMP_XPATH
        int_prod_xpath = self.orders_all_constants.FILTERS_DEPS_INT_PRODUCTS_XPATH
        int_sat_xpath = self.orders_all_constants.FILTERS_DEPS_INT_SATELLITES_XPATH
        cis_gmp_xpath = self.orders_all_constants.FILTERS_DEPS_CIS_GMP_XPATH
        cis_prod_xpath = self.orders_all_constants.FILTERS_DEPS_CIS_PRODUCTS_XPATH
        cis_general_xpath = self.orders_all_constants.FILTERS_DEPS_CIS_GENERAL_XPATH
        assert self.get_element_text(
            int_gmp_xpath) == self.orders_all_constants.FILTERS_DEPS_INT_GMP_TEXT, f"Actual message: {self.get_element_text(int_gmp_xpath)}"
        assert self.get_element_text(
            int_prod_xpath) == self.orders_all_constants.FILTERS_DEPS_INT_PRODUCTS_TEXT, f"Actual message: {self.get_element_text(int_prod_xpath)}"
        assert self.get_element_text(
            int_sat_xpath) == self.orders_all_constants.FILTERS_DEPS_INT_SATELLITES_TEXT, f"Actual message: {self.get_element_text(int_sat_xpath)}"
        assert self.get_element_text(
            cis_gmp_xpath) == self.orders_all_constants.FILTERS_DEPS_CIS_GMP_TEXT, f"Actual message: {self.get_element_text(cis_gmp_xpath)}"
        assert self.get_element_text(
            cis_prod_xpath) == self.orders_all_constants.FILTERS_DEPS_CIS_PRODUCTS_TEXT, f"Actual message: {self.get_element_text(cis_prod_xpath)}"
        assert self.get_element_text(
            cis_general_xpath) == self.orders_all_constants.FILTERS_DEPS_CIS_GENERAL_TEXT, f"Actual message: {self.get_element_text(cis_general_xpath)}"
        self.log.info(f"Departments filter has values: {self.get_element_text(int_gmp_xpath)}, {self.get_element_text(int_prod_xpath)}, "
                      f"{self.get_element_text(int_sat_xpath)}, {self.get_element_text(cis_gmp_xpath)}, {self.get_element_text(cis_prod_xpath)}, "
                      f"{self.get_element_text(cis_general_xpath)}")

    # _________________________________Filters - Teams_________________________________

    def verify_teams_filter(self):
        """Verify Teams filter is exist and has correct title"""
        assert self.get_element_text(self.orders_all_constants.FILTERS_TEAMS_TITLE_XPATH) == self.orders_all_constants.FILTERS_TEAMS_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_TEAMS_TITLE_XPATH)}"
        self.log.info(f"Order type filter is exist, title is '{self.get_element_text(self.orders_all_constants.FILTERS_TEAMS_TITLE_XPATH)}'")

    def verify_teams_int_gmp_filter_values(self):
        """Verify Teams filter for INT iGaming Media Project department has correct values - MegaDeph INT, The_First INT, All INT, Marketing, PL Team, X-Team,
        Core Team, Slotozilla Team"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_DEPS_INT_GMP_XPATH)
        self.action_chains_move_and_double_click(self.orders_all_constants.FILTERS_TEAMS_XPATH)
        megadeph_int_xpath = self.orders_all_constants.FILTERS_TEAMS_MEGADEPH_INT_XPATH
        first_int_xpath = self.orders_all_constants.FILTERS_TEAMS_FIRST_INT_XPATH
        all_int_xpath = self.orders_all_constants.FILTERS_TEAMS_ALL_INT_XPATH
        marketing_xpath = self.orders_all_constants.FILTERS_TEAMS_MARKETING_XPATH
        pl_xpath = self.orders_all_constants.FILTERS_TEAMS_PL_XPATH
        x_xpath = self.orders_all_constants.FILTERS_TEAMS_X_XPATH
        core_xpath = self.orders_all_constants.FILTERS_TEAMS_CORE_XPATH
        slotozilla_xpath = self.orders_all_constants.FILTERS_TEAMS_SLOTOZILLA_XPATH
        teams_selector_values = self.wait_until_all_displayed(self.orders_all_constants.FILTER_TEAMS_VALUES_LIST_XPATH)
        assert len(teams_selector_values) == 9
        assert self.get_element_text(
            megadeph_int_xpath) == self.orders_all_constants.FILTERS_TEAMS_MEGADEPH_INT_TEXT, f"Actual: {self.get_element_text(megadeph_int_xpath)}"
        assert self.get_element_text(
            first_int_xpath) == self.orders_all_constants.FILTERS_TEAMS_FIRST_INT_TEXT, f"Actual: {self.get_element_text(first_int_xpath)}"
        assert self.get_element_text(all_int_xpath) == self.orders_all_constants.FILTERS_TEAMS_ALL_INT_TEXT, f"Actual: {self.get_element_text(all_int_xpath)}"
        assert self.get_element_text(
            marketing_xpath) == self.orders_all_constants.FILTERS_TEAMS_MARKETING_TEXT, f"Actual: {self.get_element_text(marketing_xpath)}"
        assert self.get_element_text(pl_xpath) == self.orders_all_constants.FILTERS_TEAMS_PL_TEXT, f"Actual: {self.get_element_text(pl_xpath)}"
        assert self.get_element_text(x_xpath) == self.orders_all_constants.FILTERS_TEAMS_X_TEXT, f"Actual: {self.get_element_text(x_xpath)}"
        assert self.get_element_text(core_xpath) == self.orders_all_constants.FILTERS_TEAMS_CORE_TEXT, f"Actual: {self.get_element_text(core_xpath)}"
        assert self.get_element_text(
            slotozilla_xpath) == self.orders_all_constants.FILTERS_TEAMS_SLOTOZILLA_TEXT, f"Actual: {self.get_element_text(slotozilla_xpath)}"
        self.log.info(f"INT iGaming Media Project dep has {len(teams_selector_values) - 1} values:"
                      f" {self.get_element_text(megadeph_int_xpath)}, {self.get_element_text(first_int_xpath)}, {self.get_element_text(all_int_xpath)}, "
                      f" {self.get_element_text(marketing_xpath)}, {self.get_element_text(pl_xpath)}, {self.get_element_text(x_xpath)}, "
                      f" {self.get_element_text(core_xpath)}, {self.get_element_text(slotozilla_xpath)}")

    def verify_teams_int_prod_filter_values(self):
        """Verify Teams filter for INT Products department has correct values - Product Team, YS"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_DEPS_INT_PRODUCTS_XPATH)
        self.action_chains_move_and_double_click(self.orders_all_constants.FILTERS_TEAMS_XPATH)
        prod_xpath = self.orders_all_constants.FILTERS_TEAMS_PRODUCT_XPATH
        ys_xpath = self.orders_all_constants.FILTERS_TEAMS_YS_XPATH
        teams_selector_values = self.wait_until_all_displayed(self.orders_all_constants.FILTER_TEAMS_VALUES_LIST_XPATH)
        assert len(teams_selector_values) == 3
        assert self.get_element_text(prod_xpath) == self.orders_all_constants.FILTERS_TEAMS_PRODUCT_TEXT, f"Actual: {self.get_element_text(prod_xpath)}"
        assert self.get_element_text(ys_xpath) == self.orders_all_constants.FILTERS_TEAMS_YS_TEXT, f"Actual: {self.get_element_text(ys_xpath)}"
        self.log.info(f"INT Products dep has {len(teams_selector_values) - 1} values: {self.get_element_text(prod_xpath)}, {self.get_element_text(ys_xpath)}")

    def verify_teams_int_sat_filter_values(self):
        """Verify Teams filter for INT Satellites department has correct values - YS Satellites, Satellites Team"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_DEPS_INT_SATELLITES_XPATH)
        self.action_chains_move_and_double_click(self.orders_all_constants.FILTERS_TEAMS_XPATH)
        ys_sat_xpath = self.orders_all_constants.FILTERS_TEAMS_YS_SAT_XPATH
        satellites_xpath = self.orders_all_constants.FILTERS_TEAMS_SATELLITES_XPATH
        teams_selector_values = self.wait_until_all_displayed(self.orders_all_constants.FILTER_TEAMS_VALUES_LIST_XPATH)
        assert len(teams_selector_values) == 3
        assert self.get_element_text(ys_sat_xpath) == self.orders_all_constants.FILTERS_TEAMS_YS_SAT_TEXT, f"Actual: {self.get_element_text(ys_sat_xpath)}"
        assert self.get_element_text(
            satellites_xpath) == self.orders_all_constants.FILTERS_TEAMS_SATELLITES_TEXT, f"Actual: {self.get_element_text(satellites_xpath)}"
        self.log.info(
            f"INT Satellites dep has {len(teams_selector_values) - 1} values: {self.get_element_text(ys_sat_xpath)}, {self.get_element_text(satellites_xpath)}")

    def verify_teams_cis_gmp_filter_values(self):
        """Verify Teams filter for CIS iGaming Media Project department has correct values - The_First CIS, MegaDeph CIS, PBN, Other"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_DEPS_CIS_GMP_XPATH)
        self.action_chains_move_and_double_click(self.orders_all_constants.FILTERS_TEAMS_XPATH)
        first_cis_xpath = self.orders_all_constants.FILTERS_TEAMS_FIRST_CIS_XPATH
        megadeph_cis_xpath = self.orders_all_constants.FILTERS_TEAMS_MEGADEPH_CIS_XPATH
        pbn_xpath = self.orders_all_constants.FILTERS_TEAMS_PBN_XPATH
        other_xpath = self.orders_all_constants.FILTERS_TEAMS_OTHER_XPATH
        teams_selector_values = self.wait_until_all_displayed(self.orders_all_constants.FILTER_TEAMS_VALUES_LIST_XPATH)
        assert len(teams_selector_values) == 5
        assert self.get_element_text(
            first_cis_xpath) == self.orders_all_constants.FILTERS_TEAMS_FIRST_CIS_TEXT, f"Actual: {self.get_element_text(first_cis_xpath)}"
        assert self.get_element_text(
            megadeph_cis_xpath) == self.orders_all_constants.FILTERS_TEAMS_MEGADEPH_CIS_TEXT, f"Actual: {self.get_element_text(megadeph_cis_xpath)}"
        assert self.get_element_text(pbn_xpath) == self.orders_all_constants.FILTERS_TEAMS_PBN_TEXT, f"Actual: {self.get_element_text(pbn_xpath)}"
        assert self.get_element_text(other_xpath) == self.orders_all_constants.FILTERS_TEAMS_OTHER_TEXT, f"Actual: {self.get_element_text(other_xpath)}"
        self.log.info(f"CIS iGaming Media Project dep has {len(teams_selector_values) - 1} values: {self.get_element_text(first_cis_xpath)}, "
                      f" {self.get_element_text(megadeph_cis_xpath)}, {self.get_element_text(pbn_xpath)}, {self.get_element_text(other_xpath)}")

    def verify_teams_cis_prod_filter_values(self):
        """Verify Teams filter for CIS Products department has correct values - TOP SEO, Multi SEO"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_DEPS_CIS_PRODUCTS_XPATH)
        self.action_chains_move_and_double_click(self.orders_all_constants.FILTERS_TEAMS_XPATH)
        top_seo_xpath = self.orders_all_constants.FILTERS_TEAMS_TOP_SEO_XPATH
        multi_seo_xpath = self.orders_all_constants.FILTERS_TEAMS_MULTI_SEO_XPATH
        teams_selector_values = self.wait_until_all_displayed(self.orders_all_constants.FILTER_TEAMS_VALUES_LIST_XPATH)
        assert len(teams_selector_values) == 3
        assert self.get_element_text(top_seo_xpath) == self.orders_all_constants.FILTERS_TEAMS_TOP_SEO_TEXT, f"Actual: {self.get_element_text(top_seo_xpath)}"
        assert self.get_element_text(
            multi_seo_xpath) == self.orders_all_constants.FILTERS_TEAMS_MULTI_SEO_TEXT, f"Actual: {self.get_element_text(multi_seo_xpath)}"
        self.log.info(
            f"INT Satellites dep has {len(teams_selector_values) - 1} values: {self.get_element_text(top_seo_xpath)}, {self.get_element_text(multi_seo_xpath)}")

    def verify_teams_cis_general_filter_values(self):
        """Verify Teams filter for CIS General department has correct values - All CIS, Dev team"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_DEPS_CIS_GENERAL_XPATH)
        self.action_chains_move_and_double_click(self.orders_all_constants.FILTERS_TEAMS_XPATH)
        all_cis_xpath = self.orders_all_constants.FILTERS_TEAMS_ALL_CIS_XPATH
        dev_xpath = self.orders_all_constants.FILTERS_TEAMS_DEV_XPATH
        teams_selector_values = self.wait_until_all_displayed(self.orders_all_constants.FILTER_TEAMS_VALUES_LIST_XPATH)
        assert len(teams_selector_values) == 3
        assert self.get_element_text(all_cis_xpath) == self.orders_all_constants.FILTERS_TEAMS_ALL_CIS_TEXT, f"Actual: {self.get_element_text(all_cis_xpath)}"
        assert self.get_element_text(dev_xpath) == self.orders_all_constants.FILTERS_TEAMS_DEV_TEXT, f"Actual: {self.get_element_text(dev_xpath)}"
        self.log.info(
            f"INT Satellites dep has {len(teams_selector_values) - 1} values: {self.get_element_text(all_cis_xpath)}, {self.get_element_text(dev_xpath)}")

    # _________________________________Filters - Updated by role_________________________________

    def verify_updated_by_filter(self):
        """Verify Updated by filter is exist and has correct title"""
        assert self.get_element_text(self.orders_all_constants.FILTERS_UPD_BY_TITLE_XPATH) == self.orders_all_constants.FILTERS_UPD_BY_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_UPD_BY_TITLE_XPATH)}"
        self.log.info(f"Updated by filter is exist, title is {self.get_element_text(self.orders_all_constants.FILTERS_UPD_BY_TITLE_XPATH)}")

    def verify_updated_by_filter_values(self):
        """Verify Updated By filter has correct values - Заказчик, Руководитель команды, Модератор, Аналитик, Руководитель отдела, СОО/СЕО"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_UPD_BY_XPATH)
        customer_xpath = self.orders_all_constants.FILTERS_UPD_BY_CUSTOMER_XPATH
        team_lead_xpath = self.orders_all_constants.FILTERS_UPD_BY_TEAM_LEAD_XPATH
        moderator_xpath = self.orders_all_constants.FILTERS_UPD_BY_MODERATOR_XPATH
        analyst_xpath = self.orders_all_constants.FILTERS_UPD_BY_ANALYST_XPATH
        head_dep_xpath = self.orders_all_constants.FILTERS_UPD_BY_HEAD_DEP_XPATH
        ceo_coo_xpath = self.orders_all_constants.FILTERS_UPD_BY_CEO_COO_XPATH
        assert self.get_element_text(
            customer_xpath) == self.orders_all_constants.FILTERS_UPD_BY_CUSTOMER_TEXT, f"Actual: {self.get_element_text(customer_xpath)}"
        assert self.get_element_text(
            team_lead_xpath) == self.orders_all_constants.FILTERS_UPD_BY_TEAM_LEAD_TEXT, f"Actual: {self.get_element_text(team_lead_xpath)}"
        assert self.get_element_text(
            moderator_xpath) == self.orders_all_constants.FILTERS_UPD_BY_MODERATOR_TEXT, f"Actual: {self.get_element_text(moderator_xpath)}"
        assert self.get_element_text(analyst_xpath) == self.orders_all_constants.FILTERS_UPD_BY_ANALYST_TEXT, f"Actual: {self.get_element_text(analyst_xpath)}"
        assert self.get_element_text(
            head_dep_xpath) == self.orders_all_constants.FILTERS_UPD_BY_HEAD_DEP_TEXT, f"Actual: {self.get_element_text(head_dep_xpath)}"
        assert self.get_element_text(ceo_coo_xpath) == self.orders_all_constants.FILTERS_UPD_BY_CEO_COO_TEXT, f"Actual: {self.get_element_text(ceo_coo_xpath)}"
        self.log.info(f"Filter has {self.get_element_text(customer_xpath)}, {self.get_element_text(team_lead_xpath)}, {self.get_element_text(moderator_xpath)},"
                      f"{self.get_element_text(analyst_xpath)}, {self.get_element_text(head_dep_xpath)}, {self.get_element_text(ceo_coo_xpath)} values")

    def verify_updated_by_filtration(self, select_role, role_text, role_log):
        """Verify correctly filtration for Order type filter by values - Заказчик, Руководитель команды, Модератор, Аналитик, Руководитель отдела, СОО/СЕО"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_UPD_BY_XPATH)
        self.action_chains_move_and_click(xpath=select_role)
        if self.is_exist(xpath=self.orders_all_constants.H2_NOT_FOUND_XPATH):
            assert self.get_element_text(self.orders_all_constants.H2_NOT_FOUND_XPATH) == self.orders_all_constants.H2_NOT_FOUND_TEXT
            self.log.warning(f"The list has no orders with role {role_log}. {self.get_element_text(self.orders_all_constants.H2_NOT_FOUND_XPATH)}")
        else:
            all_orders_list = self.wait_until_all_displayed(xpath=self.orders_all_constants.FILTERS_UPD_BY_CELLS_XPATH)
            for one_order in all_orders_list:
                assert one_order.text[1:-1].lower() == role_text.lower(), f"Actual Order type value - {one_order.text[1:-1].lower()}"
            self.log.info(f"The list has {len(all_orders_list)} orders. All orders in the list have role - {role_log}")

    # _________________________________Filters - ID_________________________________

    def verify_id_filter(self):
        """Verify ID filter is exist and has correct title"""
        assert self.get_element_text(self.orders_all_constants.FILTERS_ID_TITLE_XPATH) == self.orders_all_constants.FILTERS_ID_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_ID_TITLE_XPATH)}"
        self.log.info(f"ID filter is exist, title is {self.get_element_text(self.orders_all_constants.FILTERS_ID_TITLE_XPATH)}")

    @wait_until_ok(5)
    def verify_filtration_id(self):
        """Input random id from orders list to ID filter and verify filtration"""
        all_orders_list = self.wait_until_all_displayed(xpath=self.orders_all_constants.FILTERS_ID_CELLS_XPATH)
        one_random_id = random.choice([one_order_id.text for one_order_id in all_orders_list])
        self.fill_field(xpath=self.orders_all_constants.FILTERS_ID_XPATH, value=one_random_id)
        self.log.info(f"ID {one_random_id} is selected")
        sleep(3)
        filtered_orders_list = self.wait_until_all_displayed(xpath=self.orders_all_constants.FILTERS_ID_CELLS_XPATH)
        assert len(filtered_orders_list) == 1, f"Actual amount of orders in the list = {len(filtered_orders_list)}"
        assert self.get_element_text(self.orders_all_constants.FILTERS_ID_CELLS_XPATH) == one_random_id
        self.log.info(f"The list has {len(filtered_orders_list)} order."
                      f" Order ID - {self.get_element_text(self.orders_all_constants.FILTERS_ID_CELLS_XPATH)}")

    # _________________________________Filters - Status_________________________________

    def verify_status_filter(self):
        """Verify Status filter is exist and has default status - active"""
        assert self.is_exist(self.orders_all_constants.FILTERS_STATUS_XPATH)
        assert self.get_element_text(self.orders_all_constants.FILTERS_STATUS_DEFAULT_XPATH) == self.orders_all_constants.FILTERS_STATUS_DEFAULT_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.FILTERS_STATUS_DEFAULT_XPATH)}"
        self.log.info(f"Status filter is exist, default status is {self.get_element_text(self.orders_all_constants.FILTERS_STATUS_DEFAULT_XPATH)}")

    def verify_status_filter_values(self):
        """Verify Status filter has correct values - all, active, completed, declined, deleted, payment, prepayment"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_STATUS_XPATH)
        all_xpath = self.orders_all_constants.FILTERS_STATUS_ALL_XPATH
        active_xpath = self.orders_all_constants.FILTERS_STATUS_DEFAULT_XPATH
        completed_xpath = self.orders_all_constants.FILTERS_STATUS_COMPLETED_XPATH
        declined_xpath = self.orders_all_constants.FILTERS_STATUS_DECLINED_XPATH
        deleted_xpath = self.orders_all_constants.FILTERS_STATUS_DELETED_XPATH
        payment_xpath = self.orders_all_constants.FILTERS_STATUS_PAYMENT_XPATH
        prepayment_xpath = self.orders_all_constants.FILTERS_STATUS_PREPAYMENT_XPATH
        assert self.get_element_text(all_xpath) == self.orders_all_constants.FILTERS_STATUS_ALL_TEXT, f"Actual: {self.get_element_text(all_xpath)}"
        assert self.get_element_text(active_xpath) == self.orders_all_constants.FILTERS_STATUS_DEFAULT_TEXT, f"Actual: {self.get_element_text(active_xpath)}"
        assert self.get_element_text(
            completed_xpath) == self.orders_all_constants.FILTERS_STATUS_COMPLETED_TEXT, f"Actual: {self.get_element_text(completed_xpath)}"
        assert self.get_element_text(
            declined_xpath) == self.orders_all_constants.FILTERS_STATUS_DECLINED_TEXT, f"Actual: {self.get_element_text(declined_xpath)}"
        assert self.get_element_text(deleted_xpath) == self.orders_all_constants.FILTERS_STATUS_DELETED_TEXT, f"Actual: {self.get_element_text(deleted_xpath)}"
        assert self.get_element_text(payment_xpath) == self.orders_all_constants.FILTERS_STATUS_PAYMENT_TEXT, f"Actual: {self.get_element_text(payment_xpath)}"
        assert self.get_element_text(
            prepayment_xpath) == self.orders_all_constants.FILTERS_STATUS_PREPAYMENT_TEXT, f"Actual: {self.get_element_text(prepayment_xpath)}"
        self.log.info(f"Filter has {self.get_element_text(all_xpath)}, {self.get_element_text(active_xpath)}, {self.get_element_text(completed_xpath)},"
                      f"{self.get_element_text(declined_xpath)}, {self.get_element_text(deleted_xpath)}, {self.get_element_text(payment_xpath)},"
                      f" {self.get_element_text(prepayment_xpath)} values")

    def status_filter_set_all(self, status, select_status):
        """Select values one by one in Status filter"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_STATUS_XPATH)
        self.action_chains_move_and_click(xpath=select_status)
        self.log.info(f"{status} value is selected")

    def verify_filtration_status_all(self, status_value):
        """Verify correctly filtration for Status filter by values - active, completed, declined, deleted, payment"""
        if self.is_exist(xpath=self.orders_all_constants.H2_NOT_FOUND_XPATH):
            assert self.get_element_text(self.orders_all_constants.H2_NOT_FOUND_XPATH) == self.orders_all_constants.H2_NOT_FOUND_TEXT
            self.log.warning(f"The list has no orders with status {status_value}. {self.get_element_text(self.orders_all_constants.H2_NOT_FOUND_XPATH)}")
        else:
            all_orders_list = self.wait_until_all_displayed(xpath=self.orders_all_constants.FILTERS_STATUS_CELLS_XPATH)
            for one_order in all_orders_list:
                assert one_order.text == status_value, f"Actual Order type value - {one_order.text}"
            self.log.info(f"The list has {len(all_orders_list)} orders. All orders in the list have status- {status_value}")

    def status_filter_set_prepayment(self):
        """Select Prepayment value in Status filter"""
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_STATUS_XPATH)
        self.action_chains_move_and_click(self.orders_all_constants.FILTERS_STATUS_PREPAYMENT_XPATH)
        self.log.info(f"Prepayment status is selected")

    def verify_filtration_status_prepayment(self):
        """Verify correctly filtration for Status filter by value prepayment"""
        if self.is_exist(xpath=self.orders_all_constants.H2_NOT_FOUND_XPATH):
            assert self.get_element_text(self.orders_all_constants.H2_NOT_FOUND_XPATH) == self.orders_all_constants.H2_NOT_FOUND_TEXT
            self.log.warning(f"The list has no orders with status Prepayment. {self.get_element_text(self.orders_all_constants.H2_NOT_FOUND_XPATH)}")
        else:
            all_orders_list = self.wait_until_all_displayed(xpath=self.orders_all_constants.FILTERS_STATUS_CELLS_XPATH)
            for one_order in all_orders_list:
                assert one_order.text == "Предоплата выполнена" or one_order.text == "Ожидает work link", f"Actual Order type value - {one_order.text}"
            self.log.info(f"The list has {len(all_orders_list)} orders. All orders have statuses - Предоплата выполнена или Ожидает work link")

import logging
from decimal import *

from pages.base_page import BasePage


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

    # _________________________________Elements_________________________________

    def verify_orders_all_page_h1(self):
        """Verify the Orders All Page h1 has correct text"""
        assert self.get_element_text(self.orders_all_constants.H1_XPATH) == self.orders_all_constants.H1_TEXT, \
            f"Actual message: {self.get_element_text(self.orders_all_constants.H1_XPATH)}"

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
            self.log.info(f"The list has no orders in EUR. Total {currency_log} sum in EUR = {total_in_eur_one_currency}")

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
            self.log.info(f"The list has no orders in {currency_log}. Total price in {currency_log} = {total_price_one_currency}")

    def verify_sum_price_list_usdt(self):
        total_price_usdt = self.get_element_text(xpath=self.orders_all_constants.TOTAL_IN_CURRENCY_USDT_XPATH)
        if self.is_exist(xpath=self.orders_all_constants.ORDERS_LIST_PRICE_USDT_XPATH):
            all_orders_price_usdt = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_PRICE_USDT_XPATH)
            one_order_price_usdt = [Decimal(price_usdt.text[:-5]) for price_usdt in all_orders_price_usdt]
            assert sum(one_order_price_usdt) == Decimal(total_price_usdt), \
                f"Actual all orders price - {sum(one_order_price_usdt)} USDT, total price - {total_price_usdt} USDT"
            self.log.info(f"All orders price - {sum(one_order_price_usdt)} USDT = total price - {total_price_usdt} USDT")
        else:
            assert int(total_price_usdt) == 0
            self.log.info(f"The list has no orders in USDT. Total price in USDT = {total_price_usdt}")

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
            self.log.info(f"The list has no {team_log} orders. Total {team_log} sum = {total_one_team}")

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
                f"Actual Product Team orders sum {sum(one_order_sum_one_type)}, total Product Team value {Decimal(total_one_type)}"
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

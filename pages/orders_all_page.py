import logging
from decimal import *

from pages.base_page import BasePage


class OrdersAllPage(BasePage):
    log = logging.getLogger("[OrdersAllPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.orders_all_page import OrdersAllConst
        self.orders_all_constants = OrdersAllConst
        # from pages.header import Header
        # self.header = Header(self.driver)

    # Total tables - sum in EUR

    def verify_sum_in_eur_eur(self):
        all_orders_sum_in_eur_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_EUR_EUR_XPATH)
        one_order_sum_in_eur_eur = [Decimal(sum_in_eur_eur.text) for sum_in_eur_eur in all_orders_sum_in_eur_eur]
        total_in_eur_eur = self.get_element_text(self.orders_all_constants.TOTAL_IN_EUR_EUR_XPATH)
        assert sum(one_order_sum_in_eur_eur) == Decimal(
            total_in_eur_eur), f"Actual all EUR orders sum in EUR {sum(one_order_sum_in_eur_eur)}, total EUR sum in EUR {Decimal(total_in_eur_eur)}"
        self.log.info(f"All EUR orders sum in EUR - {sum(one_order_sum_in_eur_eur)} = total EUR sum in EUR - {Decimal(total_in_eur_eur)}")

    def verify_sum_in_eur_uah(self):
        all_orders_sum_in_eur_uah = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_EUR_UAH_XPATH)
        one_order_sum_in_eur_uah = [Decimal(sum_in_eur_uah.text) for sum_in_eur_uah in all_orders_sum_in_eur_uah]
        total_in_eur_uah = self.get_element_text(self.orders_all_constants.TOTAL_IN_EUR_UAH_XPATH)
        assert sum(one_order_sum_in_eur_uah) == Decimal(
            total_in_eur_uah), f"Actual all UAH orders sum in EUR {sum(one_order_sum_in_eur_uah)}, total UAH sum in EUR {Decimal(total_in_eur_uah)}"
        self.log.info(f"All UAH orders sum in EUR - {sum(one_order_sum_in_eur_uah)} = total UAH sum in EUR - {Decimal(total_in_eur_uah)}")

    def verify_sum_in_eur_gbp(self):
        all_orders_sum_in_eur_gbp = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_EUR_GBP_XPATH)
        one_order_sum_in_eur_gbp = [Decimal(sum_in_eur_gbp.text) for sum_in_eur_gbp in all_orders_sum_in_eur_gbp]
        total_in_eur_gbp = self.get_element_text(self.orders_all_constants.TOTAL_IN_EUR_GBP_XPATH)
        assert sum(one_order_sum_in_eur_gbp) == Decimal(
            total_in_eur_gbp), f"Actual all GBP orders sum in EUR {sum(one_order_sum_in_eur_gbp)}, total GBP sum in EUR {Decimal(total_in_eur_gbp)}"
        self.log.info(f"All GBP orders sum in EUR - {sum(one_order_sum_in_eur_gbp)} = total GBP sum in EUR - {Decimal(total_in_eur_gbp)}")

    def verify_sum_in_eur_rub(self):
        all_orders_sum_in_eur_rub = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_EUR_RUB_XPATH)
        one_order_sum_in_eur_rub = [Decimal(sum_in_eur_rub.text) for sum_in_eur_rub in all_orders_sum_in_eur_rub]
        total_in_eur_rub = self.get_element_text(self.orders_all_constants.TOTAL_IN_EUR_RUB_XPATH)
        assert sum(one_order_sum_in_eur_rub) == Decimal(
            total_in_eur_rub), f"Actual all RUB orders sum in EUR {sum(one_order_sum_in_eur_rub)}, total RUB sum in EUR {Decimal(total_in_eur_rub)}"
        self.log.info(f"All RUB orders sum in EUR - {sum(one_order_sum_in_eur_rub)} = total RUB sum in EUR - {Decimal(total_in_eur_rub)}")

    def verify_sum_in_eur_usd(self):
        all_orders_sum_in_eur_usd = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_EUR_USD_XPATH)
        one_order_sum_in_eur_usd = [Decimal(sum_in_eur_usd.text) for sum_in_eur_usd in all_orders_sum_in_eur_usd]
        total_in_eur_usd = self.get_element_text(self.orders_all_constants.TOTAL_IN_EUR_USD_XPATH)
        assert sum(one_order_sum_in_eur_usd) == Decimal(
            total_in_eur_usd), f"Actual all USD orders sum in EUR {sum(one_order_sum_in_eur_usd)}, total USD sum in EUR {Decimal(total_in_eur_usd)}"
        self.log.info(f"All USD orders sum in EUR - {sum(one_order_sum_in_eur_usd)} = total USD sum in EUR - {Decimal(total_in_eur_usd)}")

    def verify_sum_in_eur_usdt(self):
        all_orders_sum_in_eur_usdt = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_EUR_USDT_XPATH)
        one_order_sum_in_eur_usdt = [Decimal(sum_in_eur_usdt.text) for sum_in_eur_usdt in all_orders_sum_in_eur_usdt]
        total_in_eur_usdt = self.get_element_text(self.orders_all_constants.TOTAL_IN_EUR_USDT_XPATH)
        assert sum(one_order_sum_in_eur_usdt) == Decimal(
            total_in_eur_usdt), f"Actual all USDT orders sum in EUR {sum(one_order_sum_in_eur_usdt)}, total USDT sum in EUR {Decimal(total_in_eur_usdt)}"
        self.log.info(f"All USDT orders sum in EUR - {sum(one_order_sum_in_eur_usdt)} = total USDT sum in EUR - {Decimal(total_in_eur_usdt)}")

    def verify_total_sum_in_eur_for_list(self):
        all_orders_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_GENERAL_SUM_IN_EUR_XPATH)
        one_order_sum_in_eur = [Decimal(sum_in_eur.text) for sum_in_eur in all_orders_sum_in_eur]
        total_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_ALL_CURRENCIES_SUM_XPATH)
        assert sum(one_order_sum_in_eur) == Decimal(
            total_sum_in_eur), f"Actual all orders sum in EUR {sum(one_order_sum_in_eur)}, total sum in EUR {Decimal(total_sum_in_eur)}"
        self.log.info(f"All orders sum in EUR - {sum(one_order_sum_in_eur)} = total sum in EUR - {Decimal(total_sum_in_eur)}")

    def verify_sum_all_totals_for_currency(self):
        all_totals_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.TOTAL_ALL_CURRENCIES_VALUES_XPATH)
        one_total_sum_in_eur = [Decimal(total_in_eur.text) for total_in_eur in all_totals_sum_in_eur]
        total_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_ALL_CURRENCIES_SUM_XPATH)
        assert sum(one_total_sum_in_eur) == Decimal(
            total_sum_in_eur), f"Actual all totals sum in EUR {sum(one_total_sum_in_eur)}, total sum in EUR {Decimal(total_sum_in_eur)}"
        self.log.info(f"All totals sum in EUR - {sum(one_total_sum_in_eur)} = total sum in EUR - {Decimal(total_sum_in_eur)}")

    # Total tables - sum in currency

    def verify_price_sum_eur(self):
        all_orders_price_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_PRICE_EUR_XPATH)
        one_order_price_eur = [Decimal(price_eur.text[:-4]) for price_eur in all_orders_price_eur]
        total_price_eur = self.get_element_text(self.orders_all_constants.TOTAL_IN_CURRENCY_EUR_XPATH)
        assert sum(one_order_price_eur) == Decimal(
            total_price_eur), f"Actual all orders price - {sum(one_order_price_eur)} EUR, total price - {Decimal(total_price_eur)} currency"
        self.log.info(f"All orders price - {sum(one_order_price_eur)} EUR = total price - {Decimal(total_price_eur)} EUR")

    def verify_price_sum_usd(self):
        all_orders_price_usd = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_PRICE_USD_XPATH)
        one_order_price_usd = [Decimal(price_usd.text[:-4]) for price_usd in all_orders_price_usd]
        total_price_usd = self.get_element_text(self.orders_all_constants.TOTAL_IN_CURRENCY_USD_XPATH)
        assert sum(one_order_price_usd) == Decimal(
            total_price_usd), f"Actual all orders price - {sum(one_order_price_usd)} USD, total price - {Decimal(total_price_usd)} USD"
        self.log.info(f"All orders price - {sum(one_order_price_usd)} USD = total price - {Decimal(total_price_usd)} USD")

    def verify_price_sum_usdt(self):
        all_orders_price_usdt = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_PRICE_USDT_XPATH)
        one_order_price_usdt = [Decimal(price_usdt.text[:-5]) for price_usdt in all_orders_price_usdt]
        total_price_usdt = self.get_element_text(self.orders_all_constants.TOTAL_IN_CURRENCY_USDT_XPATH)
        assert sum(one_order_price_usdt) == Decimal(
            total_price_usdt), f"Actual all orders price - {sum(one_order_price_usdt)} USDT, total price - {Decimal(total_price_usdt)} USDT"
        self.log.info(f"All orders price - {sum(one_order_price_usdt)} USDT = total price - {Decimal(total_price_usdt)} USDT")

    def verify_price_sum_uah(self):
        all_orders_price_uah = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_PRICE_UAH_XPATH)
        one_order_price_uah = [Decimal(price_uah.text[:-4]) for price_uah in all_orders_price_uah]
        total_price_uah = self.get_element_text(self.orders_all_constants.TOTAL_IN_CURRENCY_UAH_XPATH)
        assert sum(one_order_price_uah) == Decimal(
            total_price_uah), f"Actual all orders price - {sum(one_order_price_uah)} UAH, total price - {Decimal(total_price_uah)} UAH"
        self.log.info(f"All orders price - {sum(one_order_price_uah)} UAH = total price - {Decimal(total_price_uah)} UAH")

    def verify_price_sum_gbp(self):
        all_orders_price_gbp = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_PRICE_GBP_XPATH)
        one_order_price_gbp = [Decimal(price_gbp.text[:-4]) for price_gbp in all_orders_price_gbp]
        total_price_gbp = self.get_element_text(self.orders_all_constants.TOTAL_IN_CURRENCY_GBP_XPATH)
        assert sum(one_order_price_gbp) == Decimal(
            total_price_gbp), f"Actual all orders price - {sum(one_order_price_gbp)} GBP, total price - {Decimal(total_price_gbp)} GBP"
        self.log.info(f"All orders price - {sum(one_order_price_gbp)} GBP = total price - {Decimal(total_price_gbp)} GBP")

    def verify_price_sum_rub(self):
        all_orders_price_rub = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_PRICE_RUB_XPATH)
        one_order_price_rub = [Decimal(price_rub.text[:-4]) for price_rub in all_orders_price_rub]
        total_price_rub = self.get_element_text(self.orders_all_constants.TOTAL_IN_CURRENCY_RUB_XPATH)
        assert sum(one_order_price_rub) == Decimal(
            total_price_rub), f"Actual all orders price - {sum(one_order_price_rub)} RUB, total price - {Decimal(total_price_rub)} RUB"
        self.log.info(f"All orders price - {sum(one_order_price_rub)} RUB = total price - {Decimal(total_price_rub)} RUB")

    # Total tables - sum by teams
    def verify_total_team_sum_for_list(self):
        all_orders_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_GENERAL_SUM_IN_EUR_XPATH)
        one_order_sum_in_eur = [Decimal(sum_in_eur.text) for sum_in_eur in all_orders_sum_in_eur]
        total_team_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_ALL_TEAMS_SUM_XPATH)
        assert sum(one_order_sum_in_eur) == Decimal(
            total_team_sum_in_eur), f"Actual all orders sum in EUR {sum(one_order_sum_in_eur)}, total teams sum in EUR {Decimal(total_team_sum_in_eur)}"
        self.log.info(f"All orders sum in EUR - {sum(one_order_sum_in_eur)} = total teams sum in EUR - {Decimal(total_team_sum_in_eur)}")

    def verify_sum_all_totals_for_teams(self):
        all_totals_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.TOTAL_ALL_TEAMS_VALUES_XPATH)
        one_total_sum_in_eur = [Decimal(total_in_eur.text) for total_in_eur in all_totals_sum_in_eur]
        total_team_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_ALL_TEAMS_SUM_XPATH)
        assert sum(one_total_sum_in_eur) == Decimal(
            total_team_sum_in_eur), f"Actual all totals sum in EUR {sum(one_total_sum_in_eur)}, total sum in EUR {Decimal(total_team_sum_in_eur)}"
        self.log.info(f"All totals sum in EUR - {sum(one_total_sum_in_eur)} = total sum in EUR - {Decimal(total_team_sum_in_eur)}")

    # Total tables - sum by order type

    def verify_sum_type_content(self):
        all_orders_sum_type_content = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_TYPE_CONTENT_XPATH)
        one_order_sum_type_content = [Decimal(sum_type_content.text) for sum_type_content in all_orders_sum_type_content]
        total_type_content = self.get_element_text(self.orders_all_constants.TOTAL_TYPE_CONTENT_XPATH)
        assert sum(one_order_sum_type_content) == Decimal(total_type_content), \
            f"Actual content type orders sum {sum(one_order_sum_type_content)}, total content value {Decimal(total_type_content)}"
        self.log.info(f"Sum of content orders - {sum(one_order_sum_type_content)} = total content value - {Decimal(total_type_content)}")

    def verify_sum_type_link(self):
        all_orders_sum_type_link = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_TYPE_LINK_XPATH)
        one_order_sum_type_link = [Decimal(sum_type_link.text) for sum_type_link in all_orders_sum_type_link]
        total_type_link = self.get_element_text(self.orders_all_constants.TOTAL_TYPE_LINK_XPATH)
        assert sum(one_order_sum_type_link) == Decimal(total_type_link), \
            f"Actual link type orders sum {sum(one_order_sum_type_link)}, total link value {Decimal(total_type_link)}"
        self.log.info(f"Sum of link orders - {sum(one_order_sum_type_link)} = total link value - {Decimal(total_type_link)}")

    def verify_sum_type_other(self):
        all_orders_sum_type_other = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_TYPE_OTHER_XPATH)
        one_order_sum_type_other = [Decimal(sum_type_other.text) for sum_type_other in all_orders_sum_type_other]
        total_type_other = self.get_element_text(self.orders_all_constants.TOTAL_TYPE_OTHER_XPATH)
        assert sum(one_order_sum_type_other) == Decimal(total_type_other), \
            f"Actual other type orders sum {sum(one_order_sum_type_other)}, total other value {Decimal(total_type_other)}"
        self.log.info(f"Sum of other orders - {sum(one_order_sum_type_other)} = total other value - {Decimal(total_type_other)}")

    def verify_total_type_sum_for_list(self):
        all_orders_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_GENERAL_SUM_IN_EUR_XPATH)
        one_order_sum_in_eur = [Decimal(sum_in_eur.text) for sum_in_eur in all_orders_sum_in_eur]
        total_type_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_ALL_TYPES_SUM_XPATH)
        assert sum(one_order_sum_in_eur) == Decimal(
            total_type_sum_in_eur), f"Actual all orders sum in EUR {sum(one_order_sum_in_eur)}, total type sum in EUR {Decimal(total_type_sum_in_eur)}"
        self.log.info(f"All orders sum in EUR - {sum(one_order_sum_in_eur)} = total type sum in EUR - {Decimal(total_type_sum_in_eur)}")

    def verify_sum_all_totals_for_types(self):
        all_totals_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.TOTAL_ALL_TYPES_VALUES_XPATH)
        one_total_sum_in_eur = [Decimal(total_in_eur.text) for total_in_eur in all_totals_sum_in_eur]
        total_type_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_ALL_TYPES_SUM_XPATH)
        assert sum(one_total_sum_in_eur) == Decimal(
            total_type_sum_in_eur), f"Actual all totals sum in EUR {sum(one_total_sum_in_eur)}, total sum in EUR {Decimal(total_type_sum_in_eur)}"
        self.log.info(f"All totals sum in EUR - {sum(one_total_sum_in_eur)} = total sum in EUR - {Decimal(total_type_sum_in_eur)}")

    # Total tables - total sum in all tables
    def verify_all_sum_equals(self):
        currency_total_sum_in_eur = self.get_element_text(xpath=self.orders_all_constants.TOTAL_ALL_CURRENCIES_SUM_XPATH)
        team_total_sum_in_eur = self.get_element_text(xpath=self.orders_all_constants.TOTAL_ALL_TEAMS_SUM_XPATH)
        type_total_sum_in_eur = self.get_element_text(xpath=self.orders_all_constants.TOTAL_ALL_TYPES_SUM_XPATH)
        assert float(currency_total_sum_in_eur) == float(team_total_sum_in_eur) == float(type_total_sum_in_eur), \
            f"Currency sum in EUR - {currency_total_sum_in_eur}, teams sum in EUR - {team_total_sum_in_eur}, types sum in EUR - {type_total_sum_in_eur}"
        self.log.info(f"Currency sum - {currency_total_sum_in_eur} = teams sum - {team_total_sum_in_eur} = types sum - {type_total_sum_in_eur}")

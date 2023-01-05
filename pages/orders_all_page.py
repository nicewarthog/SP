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

    def verify_total_sum_in_eur(self):
        all_orders_sum_in_eur = self.wait_until_all_displayed(xpath=self.orders_all_constants.ORDERS_LIST_SUM_IN_EUR_XPATH)
        one_order_sum_in_eur = [Decimal(sum_in_eur.text) for sum_in_eur in all_orders_sum_in_eur]
        total_sum_in_eur = self.get_element_text(self.orders_all_constants.TOTAL_SUM_IN_EUR_XPATH)
        assert sum(one_order_sum_in_eur) == Decimal(
            total_sum_in_eur), f"Actual all orders sum in EUR {sum(one_order_sum_in_eur)}, total sum in EUR {Decimal(total_sum_in_eur)}"
        self.log.info(f"All orders sum in EUR {sum(one_order_sum_in_eur)} = total sum in EUR {Decimal(total_sum_in_eur)}")

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

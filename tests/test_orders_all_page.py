import logging

import pytest


class TestOrdersAllPage:
    log = logging.getLogger("OrdersAllPage")

    @pytest.fixture(scope="function")
    def move_to_orders_all_page(self, open_start_page, sign_in_analyst):
        # Click OrdersAllPage button on sidebar
        open_start_page.sidebar.click_orders_all_button()
        return self.move_to_orders_all_page

    def test_total_sum_in_eur(self, move_to_orders_all_page, open_start_page):
        """
        Fixture:
        - Go to OrdersAllPage
        Steps:
        - Verify all products sum in eur on the page
        - Verify that sum of all products in eur equals the total sum in eur
        """

        # Move to OrdersAllPage
        open_orders_all_page = open_start_page.sidebar.from_sidebar_to_orders_all_page()

        # Verify the sum in EUR of all orders equals the total sum in EUR
        open_orders_all_page.verify_total_sum_in_eur()

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

import logging

from constants.orders_all_page.all_pg_elements import OrdersAllElementsConst

orders_all_elements_const = OrdersAllElementsConst


class TestOrdersAllElements:
    log = logging.getLogger("OrdersAllPage")

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
        open_orders_all_page.move_from_sidebar()
        open_orders_all_page.verify_orders_all_page_h1()
        self.log.info("Orders All Page H1 is exist and has correct text")

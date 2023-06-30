import logging

from pages.base_page import BasePage


class OrdersAllPageElements(BasePage):
    log = logging.getLogger("[OrdersAllPageElements]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.orders_all_page.all_pg_elements import OrdersAllElementsConst
        self.all_pg_elements_const = OrdersAllElementsConst
        # from pages.sidebar.sidebar import Sidebar
        # self.sidebar = Sidebar(self.driver)
        # from pages.start_page.sp_base import StartPageBase
        # self.start_page = StartPageBase(self.driver)

    # _________________________________Open page and Elements_________________________________

    def move_from_sidebar(self):
        """Verify the Orders All Page h1 has correct text"""
        self.action_chains_move_and_click(xpath=self.all_pg_elements_const.H4_TYPE_XPATH)

    def verify_orders_all_page_h1(self):
        """Verify the Orders All Page h1 has correct text"""
        assert self.get_element_text(self.all_pg_elements_const.H1_XPATH) == self.all_pg_elements_const.H1_TEXT, \
            f"Actual message: {self.get_element_text(self.all_pg_elements_const.H1_XPATH)}"

    # _________________________________Paginator_________________________________
    def paginator_300_orders(self):
        """Open paginator, select value - 300 and click"""
        self.action_chains_move_and_click(self.all_pg_elements_const.PAGINATOR_XPATH)
        self.action_chains_move_and_click(self.all_pg_elements_const.PAGINATOR_SELECTOR_300_XPATH)

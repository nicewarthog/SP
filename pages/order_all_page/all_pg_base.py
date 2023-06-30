import logging

from pages.base_page import BasePage


class OrdersAllPageBase(BasePage):
    log = logging.getLogger("[OrdersAllPageBase]")

    def __init__(self, driver):
        super().__init__(driver)
        from pages.order_all_page.all_pg_elements import OrdersAllPageElements
        self.all_pg_elements = OrdersAllPageElements(self.driver)
        from pages.order_all_page.all_pg_tables import OrdersAllPageTables
        self.all_pg_tables = OrdersAllPageTables(self.driver)
        from pages.order_all_page.all_page_filters import OrdersAllPageFilters
        self.all_pg_filters = OrdersAllPageFilters(self.driver)
        from pages.sidebar.sidebar import Sidebar
        self.sidebar = Sidebar(self.driver)
        from pages.start_page.sp_base import StartPageBase
        self.start_page = StartPageBase(self.driver)

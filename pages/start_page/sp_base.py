import logging
from time import sleep

from pages.base_page import BasePage


class StartPageBase(BasePage):
    log = logging.getLogger("[StartPageBase]")

    def __init__(self, driver):
        super().__init__(driver)
        from pages.start_page.sp_elements import StartPageElements
        self.st_pg_elements = StartPageElements(self.driver)
        from pages.start_page.sp_sign_in import StartPageSignIn
        self.st_pg_sign_in = StartPageSignIn(self.driver)
        from pages.header.header import Header
        self.header = Header(self.driver)
        from pages.sidebar.sidebar import Sidebar
        self.sidebar = Sidebar(self.driver)
        from pages.order_all_page.all_pg_tables import OrdersAllPageTables
        self.orders_all_pg_tables = OrdersAllPageTables(self.driver)

    # From page to page

    def from_start_page_to_header(self):
        """Move from Start Page to Header"""
        from pages.header.header import Header
        return Header(self.driver)

    def from_start_page_to_sidebar(self):
        """Move from Start Page to Sidebar"""
        from pages.sidebar.sidebar import Sidebar
        sleep(1)
        return Sidebar(self.driver)

    # Refresh page

    def refresh_page(self):
        """Refresh page"""
        self.driver.refresh()

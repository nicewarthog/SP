import logging

from pages.base_page import BasePage


class Sidebar(BasePage):
    log = logging.getLogger("[Sidebar]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.sidebar import SidebarConst
        self.sidebar_constants = SidebarConst
        # from pages.header import Header
        # self.header = Header(self.driver)
        # from pages.start_page import StartPage
        # self.start_page = StartPage(self.driver)

    def verify_teams_button_elements(self):
        """Verify the Teams button has correct icon and title"""
        assert self.is_exist(xpath=self.sidebar_constants.TEAM_ICON_XPATH)
        assert self.get_element_text(self.sidebar_constants.TEAM_TITLE_XPATH) == self.sidebar_constants.TEAM_TITLE_TEXT, \
            f"Actual message: {self.get_element_text(self.sidebar_constants.TEAM_TITLE_XPATH)}"

    def verify_teams_button_is_not_exist(self):
        """Verify the Teams button does not display"""
        assert self.is_not_exist(xpath=self.sidebar_constants.TEAM_ICON_XPATH)

    def click_orders_all_button(self):
        # Click OrdersAllPage button
        self.click(xpath=self.sidebar_constants.ALL_ORDERS_TITLE_XPATH)

    # PAGES

    def from_sidebar_to_orders_all_page(self):
        """Move from Start Page to Sidebar"""
        from pages.orders_all_page import OrdersAllPage
        return OrdersAllPage(self.driver)

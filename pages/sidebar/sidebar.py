import logging

from pages.base_page import BasePage


class Sidebar(BasePage):
    log = logging.getLogger("[Sidebar]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.sidebar.sidebar import SidebarConst
        self.sidebar_constants = SidebarConst
        # from pages.header import Header
        # self.header = Header(self.driver)
        # from pages.start_page import StartPage
        # self.start_page = StartPage(self.driver)

    def verify_order_create_button(self):
        """Verify the Order create icon"""
        assert self.is_exist(xpath=self.sidebar_constants.CREATE_ORDER_XPATH)

    def verify_order_create_button_not_exist(self):
        """Verify the Order create icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.CREATE_ORDER_XPATH)

    def verify_my_orders_button(self):
        """Verify the My orders icon"""
        assert self.is_exist(xpath=self.sidebar_constants.MY_ORDERS_XPATH)

    def verify_my_orders_button_not_exist(self):
        """Verify the My orders icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.MY_ORDERS_XPATH)

    def verify_team_orders_button(self):
        """Verify the Team orders icon"""
        assert self.is_exist(xpath=self.sidebar_constants.TEAM_ORDERS_XPATH)

    def verify_team_orders_button_not_exist(self):
        """Verify the Team orders icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.TEAM_ORDERS_XPATH)

    def verify_dep_orders_button(self):
        """Verify the Departament orders icon"""
        assert self.is_exist(xpath=self.sidebar_constants.DEP_ORDERS_XPATH)

    def verify_dep_orders_button_not_exist(self):
        """Verify the Departament orders icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.DEP_ORDERS_XPATH)

    def verify_all_orders_button(self):
        """Verify the All orders icon"""
        assert self.is_exist(xpath=self.sidebar_constants.ALL_ORDERS_XPATH)

    def verify_all_orders_button_not_exist(self):
        """Verify the All orders icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.ALL_ORDERS_XPATH)

    def verify_export_button(self):
        """Verify the Export icon"""
        assert self.is_exist(xpath=self.sidebar_constants.EXPORT_XPATH)

    def verify_export_button_not_exist(self):
        """Verify the Export icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.EXPORT_XPATH)

    def verify_currency_button(self):
        """Verify the Currency exchange icon"""
        assert self.is_exist(xpath=self.sidebar_constants.CURRENCY_XPATH)

    def verify_currency_button_not_exist(self):
        """Verify the Currency exchange icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.CURRENCY_XPATH)

    def verify_donors_button(self):
        """Verify the Donors icon"""
        assert self.is_exist(xpath=self.sidebar_constants.DONORS_XPATH)

    def verify_donors_button_not_exist(self):
        """Verify the Donors icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.DONORS_XPATH)

    def verify_geo_button(self):
        """Verify the GEO icon"""
        assert self.is_exist(xpath=self.sidebar_constants.GEO_XPATH)

    def verify_geo_button_not_exist(self):
        """Verify the GEO icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.GEO_XPATH)

    def verify_users_button(self):
        """Verify the Users list icon"""
        assert self.is_exist(xpath=self.sidebar_constants.USERS_XPATH)

    def verify_users_button_not_exist(self):
        """Verify the Users list icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.USERS_XPATH)

    def verify_teams_button(self):
        """Verify the Teams list icon"""
        assert self.is_exist(xpath=self.sidebar_constants.TEAMS_XPATH)

    def verify_teams_button_not_exist(self):
        """Verify the Teams list icon is not exist"""
        assert self.is_not_exist(xpath=self.sidebar_constants.TEAMS_XPATH)

    def click_orders_all_button(self):
        # Click OrdersAllPage button
        self.click(xpath=self.sidebar_constants.ALL_ORDERS_XPATH)

    def move_to_sidebar_panel(self):
        self.action_chains_move_and_click(xpath=self.sidebar_constants.SIDEBAR_XPATH)

    # PAGES

    def from_sidebar_to_orders_all_page(self):
        """Move from Start Page to Sidebar"""
        from pages.order_all_page.all_pg_elements import OrdersAllPageElements
        return OrdersAllPageElements(self.driver)

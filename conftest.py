import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL, ORDERS_ALL_URL
from pages.order_all_page.all_pg_base import OrdersAllPageBase
from pages.start_page.sp_base import StartPageBase
from pages.utils import User


# _________________________________Open Start Page_________________________________

@pytest.fixture(scope="function")
def open_start_page():
    """Open start page"""
    # create driver
    driver = webdriver.Chrome(DRIVER_PATH)
    # open Start Page URL
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(1)
    # Steps
    yield StartPageBase(driver)
    # Close driver
    driver.close()


@pytest.fixture(scope="function")
def sign_in_customer(open_start_page):
    basic_user = User(login="seopay-qa-customer", password="seopay-qa-customer")
    open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)
    return sign_in_customer


@pytest.fixture(scope="function")
def sign_in_team_lead(open_start_page):
    basic_user = User(login="seopay-qa-team-lead", password="PUAaQSpL0OuCvQpf")
    open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)
    return sign_in_team_lead


@pytest.fixture(scope="function")
def sign_in_moderator(open_start_page):
    basic_user = User(login="seopay-qa-moderator", password="bXuDp4czuc60LkH9")
    open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)
    return sign_in_moderator


@pytest.fixture(scope="function")
def sign_in_analyst(open_start_page):
    basic_user = User(login="seopay-qa-analyst", password="seopay-qa-analyst")
    open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)
    return sign_in_analyst


@pytest.fixture(scope="function")
def sign_in_head_dep(open_start_page):
    basic_user = User(login="seopay-qa-head-dep", password="i1unXfsJoKXS7VrD")
    open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)
    return sign_in_head_dep


@pytest.fixture(scope="function")
def sign_in_coo_ceo(open_start_page):
    basic_user = User(login="seopay-qa-ceo", password="uGwql6dqvC9fAFwC")
    open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)
    return sign_in_coo_ceo


# @pytest.fixture(scope="function")
# def sign_in_admin(open_start_page):
#     basic_user = User(login="seopay-qa-superadmin", password="seopay-qa-superadmin")
#     open_start_page.st_pg_sign_in.sign_in_with_button(basic_user)
#     return sign_in_admin


# _________________________________Open Orders All Page_________________________________
@pytest.fixture(scope="function")
def open_orders_all_page():
    """Open start page"""
    # create driver
    driver = webdriver.Chrome(DRIVER_PATH)
    # open Orders All Page URL
    driver.get(ORDERS_ALL_URL)
    driver.maximize_window()
    driver.implicitly_wait(1)
    # Steps
    yield OrdersAllPageBase(driver)
    # Close driver
    driver.close()


@pytest.fixture(scope="function")
def sign_in_analyst_orders_all_page(open_orders_all_page):
    basic_user = User(login="seopay-qa-analyst", password="seopay-qa-analyst")
    open_orders_all_page.all_pg_tables.st_pg_sign_in.sign_in_with_button(basic_user)
    return sign_in_analyst_orders_all_page

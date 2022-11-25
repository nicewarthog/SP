import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


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
    yield StartPage(driver)
    # Close driver
    driver.close()


@pytest.fixture(scope="function")
def sign_in_with_basic_user(open_start_page):
    basic_user = User(login="seopay-qa-ceo", password="uGwql6dqvC9fAFwC")
    open_start_page.sign_in_with_button(basic_user)
    return sign_in_with_basic_user

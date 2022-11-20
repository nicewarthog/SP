import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage


@pytest.fixture(scope="function")
def open_start_page():
    """Open start page"""
    # create driver
    driver = webdriver.Chrome(DRIVER_PATH)
    # open Start Page URL
    driver.get(BASE_URL)
    # driver.maximize_window()
    driver.implicitly_wait(1)
    # Steps
    yield StartPage(driver)
    # Close driver
    driver.close()

# @pytest.fixture(scope="function")
# def basic_user(open_start_page):
#     user = User(login="Ігор", phone="974955232", password="qwerty")
#     open_start_page.sign_in(user)
#     return basic_user

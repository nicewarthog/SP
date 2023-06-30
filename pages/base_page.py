import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)
        # self.action_chains = ActionChains(driver=driver)

    def is_exist(self, xpath, by=By.XPATH):
        """Check that element exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def is_not_exist(self, xpath, by=By.XPATH):
        """Check that element not exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return False
        except selenium.common.exceptions.NoSuchElementException:
            return True

    def wait_until_presented(self, xpath):
        """Checking that an element is present on the DOM of a page. This does not necessarily mean that the element is visible"""
        return self.waiter.until(method=expected_conditions.presence_of_element_located((By.XPATH, xpath)),
                                 message=f"XPATH '{xpath}' is not presented or cannot be found")

    def wait_until_all_presented(self, xpath):
        """Checking that at least one element is present on the DOM of a page. This does not necessarily mean that the element is visible"""
        return self.waiter.until(method=expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)),
                                 message=f"XPATH '{xpath}' is not presented or cannot be found")

    def wait_until_displayed(self, xpath):
        """Checking that an element is present on the DOM of a page and visible.
         Visibility means that the element is not only displayed  but also has a height and width that is greater than 0"""
        return self.waiter.until(method=expected_conditions.visibility_of_element_located((By.XPATH, xpath)),
                                 message=f"XPATH '{xpath}' is not displayed or cannot be found")

    def wait_until_all_displayed(self, xpath):
        """Wait until all elements is displayed"""
        return self.waiter.until(method=expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath)),
                                 message=f"XPATH '{xpath}' is not displayed or cannot be found")

    def wait_until_clickable(self, xpath):
        """Wait until element is clickable"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, xpath)),
                                 message=f"XPATH '{xpath}' is not clickable or cannot be found")

    def action_chains_move_to_element(self, xpath):
        """Move to element, click and perform next actions"""
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(self.wait_until_displayed(xpath=xpath))
        return action_chains

    def action_chains_move_and_click(self, xpath):
        """Move to element, click and perform next actions"""
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(self.wait_until_displayed(xpath=xpath))
        action_chains.click(self.wait_until_displayed(xpath=xpath))
        action_chains.w3c_actions.perform()
        return action_chains

    def action_chains_move_and_double_click(self, xpath):
        """Move to element, double click and perform next actions"""
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(self.wait_until_displayed(xpath=xpath))
        action_chains.double_click(self.wait_until_displayed(xpath=xpath))
        action_chains.w3c_actions.perform()
        return action_chains

    def get_element_text(self, xpath):
        """Find element and get text"""
        element = self.wait_until_displayed(xpath=xpath)
        return element.text

    def fill_field(self, xpath, value):
        """Clear and fill field"""
        element = self.wait_until_clickable(xpath=xpath)
        element.clear()
        element.send_keys(value)

    def select_field(self, xpath, value):
        select = Select(self.wait_until_clickable(xpath=xpath))
        select.select_by_visible_text(value)

    def click(self, xpath):
        """Find and click button"""
        self.wait_until_clickable(xpath=xpath).click()

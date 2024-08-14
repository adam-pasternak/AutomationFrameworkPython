from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def click_element(element):
        element.click()

    @staticmethod
    def sendkey_element(element, key):
        element.send_keys(key)

    def wait_for_element_to_be_clickable(self, by, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable((by, locator)))

    def wait_and_click(self, element):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(element))
        wait.until(expected_conditions.visibility_of(element))
        element.click()

    def wait_for_visibility(self, element):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of(element))

import logging

from appium.webdriver.common.mobileby import MobileBy

from TAF_core.mobile.Android.screens.BaseScreen import BasePage


class SettingsScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(30)
        self.connections = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Connections"]')

    def connections_element_is_visible(self):
        self.wait_for_visibility(self.connections)
        assert self.connections.is_displayed(), "Connections element is not visible"
        logging.info("Connections element is visible")

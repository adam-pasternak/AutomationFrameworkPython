import pyautogui
import pytest
from playwright.sync_api import sync_playwright

from common.tools.PropertiesManager import get_property_value


@pytest.fixture()
def page():
    with sync_playwright() as playwright:
        browser_type = get_property_value("test_config.properties", "browser")
        if browser_type == 'chromium':
            browser = playwright.chromium.launch(headless=False)
        elif browser_type == 'firefox':
            browser = playwright.firefox.launch(headless=False)
        elif browser_type == 'webkit':
            browser = playwright.webkit.launch(headless=False)
        else:
            raise ValueError(f"Invalid browser type: '{browser_type}' set in properties file")

        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        # Maximize window
        pyautogui.keyDown('win')
        pyautogui.press('up')
        pyautogui.keyUp('win')

        yield page

        page.context.clear_cookies()
        # page.evaluate("localStorage.clear();")
        page.close()
        context.close()
        browser.close()

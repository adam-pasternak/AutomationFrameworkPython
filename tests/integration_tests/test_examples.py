import pytest

from common.tools.PropertiesManager import get_property_value
from TAF_core.api.requests.Requests import get_postman_echo
from TAF_core.frontend.functions.BrowserFunctions import open_page, screenshot_png
from TAF_core.frontend.pages.GooglePage import verify_google_logo_is_visible
from TAF_core.mobile.Android.screens.SettingsScreen import SettingsScreen


@pytest.mark.SamsungS21
def test_example_cross_platform(page, driver, token, random_digit):

    # Android sample test
    settings_screen = SettingsScreen(driver)
    settings_screen.connections_element_is_visible()

    # Frontend sample test
    open_page(page, get_property_value("test_config.properties", "env") + ".properties", "google_url")
    screenshot_png(page, "/tests/screenshots/test_example_cross_platform")
    verify_google_logo_is_visible(page)

    # API sample test
    response = get_postman_echo()
    assert response.status_code == 200

    # Assert sample fixture
    assert 0 <= random_digit <= 9

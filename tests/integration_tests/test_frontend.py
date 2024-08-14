from TAF_core.frontend.pages.LoggedUserPanel import is_cart_visible
from TAF_core.frontend.pages.LoginPage import set_username, set_password, click_submit
from common.tools.PropertiesManager import get_property_value
from TAF_core.frontend.functions.BrowserFunctions import open_page, screenshot_png


def test_frontend(page):

    # Open saucedemo.com test page
    open_page(page, get_property_value("test_config.properties", "env") + ".properties", "saucedemo_url")

    # Fill username field
    set_username(page, "standard_user")

    # Fill password field
    set_password(page, "secret_sauce")

    # Click submit button
    click_submit(page)

    # Make screenshot before verification
    screenshot_png(page, "/tests/screenshots/test_frontend")

    # Verify that user has logged in correctly - cart icon is visible
    assert is_cart_visible(page) is True

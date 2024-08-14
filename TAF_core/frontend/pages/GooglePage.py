from playwright.sync_api import Page

from common.tools.Logger import log_info

GOOGLE_LOGO = "//img[@alt='Google']"


def verify_google_logo_is_visible(page: Page):
    page.wait_for_selector(GOOGLE_LOGO, state="visible")
    assert page.is_visible(f"xpath={GOOGLE_LOGO}"), "Google logo is not visible"
    log_info("Google logo is visible")

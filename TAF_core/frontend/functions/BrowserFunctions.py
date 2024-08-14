import datetime

from playwright.sync_api import Page

from common.tools.Helpers import get_project_root_path
from common.tools.Logger import log_info
from common.tools.PropertiesManager import get_property_value


def open_page(page: Page, properties_file,  url):
    page.goto(get_property_value(properties_file, url))
    log_info("Page: " + get_property_value(properties_file, url) + " opened")


def screenshot_png(page: Page, path_to_save_from_project_root_level):
    path = get_project_root_path() + path_to_save_from_project_root_level + "_" \
           + datetime.datetime.now().strftime("%d%m%y%H%M%S") + ".png"
    page.screenshot(path=path)
    log_info("Screenshot saved to " + path)

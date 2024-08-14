from playwright.sync_api import Page

from common.tools.Logger import log_info

CART = "//div[@id='shopping_cart_container']/a"


def is_cart_visible(page: Page):
    cart_visibility = page.is_visible(CART)
    log_info("Cart visibility: " + str(cart_visibility))
    return cart_visibility

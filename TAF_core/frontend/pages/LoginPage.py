import logging

from playwright.sync_api import Page


ERROR_MESSAGE = "//h3[@data-test='error']"
PASSWORD = "#password"
SUBMIT = "#login-button"
USERNAME = "#user-name"


def set_username(page: Page, username):
    page.fill(USERNAME, username)
    logging.info("Username filled")


def set_password(page: Page, password):
    page.fill(PASSWORD, password)
    logging.info("Password filled")


def click_submit(page: Page):
    page.click(SUBMIT)
    logging.info("Submit button clicked")


def get_error_message_text(page: Page):
    page.text_content(ERROR_MESSAGE)
    logging.info("Error message content: " + ERROR_MESSAGE)

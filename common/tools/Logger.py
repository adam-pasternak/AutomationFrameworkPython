import logging

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()


def log_debug(message):
    logger.debug(message)


def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_critical(message):
    logger.critical(message)


import json
import logging

import requests
from requests import Response, HTTPError

from common.tools.Buffer import get_value
from common.tools.Logger import log_info
from common.tools.PropertiesManager import get_property_value

properties_file = get_property_value("test_config.properties", "env") + ".properties"
url = get_property_value(properties_file, "postman_echo_url")


def get_postman_echo() -> Response:
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url + "/get", headers=headers)
        logging.info("RESPONSE FROM " + url + "/get: " + str(response.json()))
        response.raise_for_status()
    except HTTPError:
        log_info(("\n" + json.dumps(response.json(), indent=4)))
    return response

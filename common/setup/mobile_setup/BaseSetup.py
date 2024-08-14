import json
import pytest
from appium import webdriver

from common.tools.Helpers import get_project_root_path
from common.tools.Logger import log_info
from common.tools.PropertiesManager import get_property_value

with open(get_project_root_path() + '/common/setup/mobile_setup/devices_config.json', 'r') as file:
    config = json.load(file)


@pytest.fixture
def capabilities(request):
    marker_expression = request.config.getoption('-k')

    # Default to a device from test config if no marker expression is provided
    profile = get_property_value(get_property_value("test_config.properties", "dataset"), "DEVICE")\
        if not marker_expression else marker_expression

    return config.get(profile, {})


@pytest.fixture
def driver(capabilities):
    log_info("CAPABILITIES: " + str(capabilities))
    url = "http://localhost:4723"
    driver = webdriver.Remote(url, capabilities)
    driver.implicitly_wait(45)
    yield driver
    driver.quit()

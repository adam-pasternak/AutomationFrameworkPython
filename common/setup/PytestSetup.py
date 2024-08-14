import os
import pytest

from common.tools.Logger import log_info
from TAF_core.api.requests.authorization.GetToken import get_token


@pytest.fixture(scope="class", autouse=True)
def setup():
    log_info("EXECUTING TEST: " + os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])
    yield
    print("\n")


@pytest.fixture(scope="session")
def token():
    get_token()
    log_info("Token obtained")

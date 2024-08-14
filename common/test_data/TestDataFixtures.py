import random

import pytest


@pytest.fixture()
def random_digit():
    random_digit = random.randint(0, 9)
    return random_digit

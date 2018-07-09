import locale

import pytest


@pytest.fixture(autouse=True)
def setup_locale():
    locale.setlocale(locale.LC_ALL, "us_EN")


def test_numbers():
    assert locale.format("%f", 10.5) == "10.500000"

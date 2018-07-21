import locale

import pytest


@pytest.fixture(autouse=True)
def setup_locale():
    locale.setlocale(locale.LC_ALL, "us_EN")
    yield
    locale.setlocale(locale.LC_ALL, None)


def test_numbers_us():
    assert locale.format("%f", 10.5) == "10.500000"


@pytest.fixture(autouse=True)
def setup_locale(request):
    mark = request.node.get_closest_marker("change_local")
    loc = mark.args[0] if mark is not None else "us_EN"
    locale.setlocale(locale.LC_ALL, loc)
    yield
    locale.setlocale(locale.LC_ALL, None)


@pytest.mark.change_local("pt_BR")
def test_numbers_br():
    assert locale.format("%f", 10.5) == "10,500000"

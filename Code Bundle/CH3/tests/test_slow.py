import pytest


@pytest.mark.slow
def test_long_computation():
    ...


@pytest.mark.timeout(10, method="thread")
def test_topology_sort():
    ...


def test_foo():
    pass

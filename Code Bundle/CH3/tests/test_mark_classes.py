import pytest


@pytest.mark.timeout(10)
class TestCore:

    def test_simple_simulation(self):
        ...

    def test_compute_tracers(self):
        ...


class Test2(TestCore):

    def test_pipes(self):
        ...

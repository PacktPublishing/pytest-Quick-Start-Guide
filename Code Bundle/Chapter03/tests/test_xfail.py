import sys

import pytest


@pytest.mark.xfail
def test_simulation_34():
    ...


@pytest.mark.xfail(
    sys.platform.startswith("win"),
    reason="flaky on Windows #42",
    strict=False,
)
def test_login_dialog():
    ...


def check_credentials(name):
    raise NotImplementedError


@pytest.mark.xfail(
    raises=NotImplementedError, reason="will be implemented in #987"
)
def test_credential_check():
    check_credentials("User")  # not implemented yet


class Particle:
    pass


def collide(p1, p2):
    pass


@pytest.mark.xfail(
    run=False, reason="undefined particles cause a crash #625"
)
def test_undefined_particle_collision_crash():
    collide(Particle(), Particle())


def initialize_physics():
    pass


def test_particle_splitting():
    initialize_physics()
    import numpy

    if numpy.__version__ < "1.13":
        pytest.xfail("split computation fails with numpy < 1.13")
    ...

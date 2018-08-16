import os
import sys

import pytest


@pytest.mark.skipif(
    sys.platform.startswith("win"),
    reason="fork not available on Windows",
)
def test_spawn_server_using_fork():
    ...


@pytest.mark.skipif(
    not hasattr(os, "fork"), reason="os.fork not available"
)
def test_spawn_server_using_fork2():
    ...


def initialize_graphics():
    pass


def supports_shaders():
    return False


def test_shaders():
    initialize_graphics()
    if not supports_shaders():
        pytest.skip("shades not supported")
    # rest of the test code
    ...


def test_tracers_as_arrays_manual():
    try:
        import numpy
    except ImportError:
        pytest.skip("requires numpy")
    ...


def test_tracers_as_arrays_114():
    numpy = pytest.importorskip("numpy", minversion="1.14")
    ...

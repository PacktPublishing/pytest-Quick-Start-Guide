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

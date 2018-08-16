import json
import os
import subprocess
import tempfile
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def setup_dev_environment():
    previous = os.environ.get("APP_ENV", "")
    os.environ["APP_ENV"] = "TESTING"
    yield
    os.environ["APP_ENV"] = previous


def test_setup_app():
    pass


@pytest.fixture
def venv_dir():
    import venv

    with tempfile.TemporaryDirectory() as d:
        venv.create(d)
        pwd = os.getcwd()
        os.chdir(d)
        yield d
        os.chdir(pwd)


@pytest.mark.usefixtures("venv_dir")
class Test:

    def test_something(self):
        print([str(x) for x in Path(".").iterdir()])
        assert Path("pyvenv.cfg").is_file()

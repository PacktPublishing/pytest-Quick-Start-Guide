import tempfile

import pytest
from myapp import setup


@pytest.fixture
def setup_app():
    ...
    setup()
    tempfile.gettempdir()


import pytest


@pytest.fixture
def setup_app():
    import tempfile
    from myapp import setup

    ...

    setup()
    tempfile.gettempdir()

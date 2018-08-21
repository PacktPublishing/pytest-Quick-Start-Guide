import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import pytest


class DataBaseFixture:

    def __init__(self):
        self.db_file = self.create_temporary_db()
        self.session = self.connect_db(self.db_file)

    def teardown(self):
        self.session.close()
        os.remove(self.db_file)

    ...

    def check_row(self, table_name, **query):
        row = self.session.find(table_name, **query)
        assert row is not None
        ...

    ...

    def create_temporary_db(self):
        ...
        # wrong way of obtaining a temp filename follows
        fd, name = tempfile.mkstemp()
        os.close(fd)
        f = Path(name)
        f.write_text("")
        return str(f)

    def connect_db(self, db_file):
        ...
        return mock.MagicMock()

    def create_table(self, table_name, **fields):
        ...
        return mock.MagicMock()


@pytest.fixture
def db_testing():
    result = DataBaseFixture()
    yield result
    result.teardown()


class DataBaseTesting(DataBaseFixture):

    def __init__(self, test_case):
        super().__init__()
        test_case.addCleanup(self.teardown)


class Test(unittest.TestCase):

    def test_1(self):
        db_testing = DataBaseTesting(self)
        db_testing.create_table(
            "weapons", name=str, type=str, dmg=int
        )
        db_testing.check_row("weapons", name="zweihander")
        ...

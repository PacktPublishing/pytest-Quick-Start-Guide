import os
import tempfile
import unittest
from unittest import mock


class Test(unittest.TestCase):

    def setUp(self):
        self.db_file = self.create_temporary_db()
        self.session = self.connect_db(self.db_file)

    def tearDown(self):
        self.session.close()
        os.remove(self.db_file)

    def create_temporary_db(self):
        ...
        return tempfile.NamedTemporaryFile(delete=False).name

    def connect_db(self, db_file):
        ...
        return mock.MagicMock()

    def create_table(self, table_name, **fields):
        ...

    def check_row(self, table_name, **query):
        ...

    def test1(self):
        self.create_table("weapons", name=str, type=str, dmg=int)
        ...

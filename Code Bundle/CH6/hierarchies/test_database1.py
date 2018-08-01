import os
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.db_file = self.create_temporary_db()
        self.session = self.connect_db(self.db_file)

    def tearDown(self):
        self.session.close()
        os.remove(self.db_file)

    def create_temporary_db(self):
        ...

    def connect_db(self, db_file):
        ...

    def create_table(self, name, **fields):
        ...

    def check_row(self, name, **query):
        ...

    def test1(self):
        self.create_table("weapons", name=str, type=str, dmg=int)
        ...

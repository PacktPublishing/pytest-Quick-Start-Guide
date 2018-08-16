import os
import unittest


class DataBaseTesting:

    def __init__(self, test_case):
        self.db_file = self.create_temporary_db()
        self.session = self.connect_db(self.db_file)
        self.test_case = test_case
        test_case.addCleanup(self.teardown)

    def teardown(self):
        self.session.close()
        os.remove(self.db_file)

    ...

    def check_row(self, table_name, **query):
        row = self.session.find(table_name, **query)
        self.test_case.assertIsNotNone(row)
        ...

    ...

    def create_temporary_db(self):
        ...

    def connect_db(self, db_file):
        ...

    def create_table(self, name, **fields):
        ...


class Test(unittest.TestCase):

    def test_1(self):
        db_testing = DataBaseTesting(self)
        db_testing.create_table(
            "weapons", name=str, type=str, dmg=int
        )
        db_testing.check_row("weapons", name="zweihander")
        ...

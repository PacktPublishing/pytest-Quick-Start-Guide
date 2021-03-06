import os
import tempfile
from unittest import mock
import unittest


class DataBaseTesting(unittest.TestCase):

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


class GUITesting(unittest.TestCase):

    def setUp(self):
        self.app = self.create_app()

    def tearDown(self):
        self.app.close_all_windows()

    def create_app(self):
        ...
        return mock.MagicMock()

    def mouse_click(self, window, button):
        ...

    def enter_text(self, window, text):
        ...

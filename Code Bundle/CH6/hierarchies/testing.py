import os
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

    def connect_db(self, db_file):
        ...

    def create_table(self, name, **fields):
        ...

    def check_row(self, name, **query):
        ...


class GUITesting(unittest.TestCase):

    def setUp(self):
        self._app = self.create_app()

    def tearDown(self):
        self._app.close_all_windows()

    def mouse_click(self, window, button):
        ...

    def enter_text(self, window, text):
        ...

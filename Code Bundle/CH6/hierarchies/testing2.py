import unittest

import pytest


class DataBaseTesting(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _setup(self, db_testing):
        self._db_testing = db_testing

    def create_temporary_db(self):
        return self._db_testing.create_temporary_db()

    def connect_db(self, db_file):
        return self._db_testing.connect_db(db_file)

    ...


class GUITesting(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _setup(self, gui_testing):
        self._gui_testing = gui_testing

    def mouse_click(self, window, button):
        return self._gui_testing.mouse_click(window, button)

    ...

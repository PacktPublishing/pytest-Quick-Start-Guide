
import csv
import shutil
import tempfile
import unittest
from collections import namedtuple
from pathlib import Path

DATA = """
Main Grid,48,44
2nd Grid,24,21
3rd Grid,24,48
"""

GridData = namedtuple("GridData", "name total_cells active_cells")


def convert_size(s):
    return int(s)


def parse_grid_data(fields):
    return GridData(
        name=str(fields[0]),
        total_cells=convert_size(fields[1]),
        active_cells=convert_size(fields[2]),
    )


def iter_grids_from_csv(path):
    with path.open() as f:
        for fields in csv.reader(f.readlines()):
            yield parse_grid_data(fields)


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_dir = Path(tempfile.mkdtemp())
        cls.filepath = cls.temp_dir / "data.csv"
        cls.filepath.write_text(DATA.strip())

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.temp_dir)

    def setUp(self):
        self.grids = list(iter_grids_from_csv(self.filepath))

    def test_read_properties(self):
        self.assertEqual(self.grids[0], GridData("Main Grid", 48, 44))
        self.assertEqual(self.grids[1], GridData("2nd Grid", 24, 21))
        self.assertEqual(self.grids[2], GridData("3rd Grid", 24, 48))

    def test_invalid_path(self):
        with self.assertRaises(IOError):
            list(iter_grids_from_csv(Path("invalid file")))

    @unittest.expectedFailure
    def test_write_properties(self):
        self.fail("not implemented yet")


import csv
import shutil
import tempfile
import unittest
from collections import namedtuple
from pathlib import Path
import pytest

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


class Test:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def _setup_class(cls):
        temp_dir = Path(tempfile.mkdtemp())
        cls.filepath = temp_dir / "data.csv"
        cls.filepath.write_text(DATA.strip())
        yield
        shutil.rmtree(temp_dir)

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.grids = list(iter_grids_from_csv(self.filepath))

    def test_read_properties(self):
        assert self.grids[0] == GridData("Main Grid", 48, 44)
        assert self.grids[1] == GridData("2nd Grid", 24, 21)
        assert self.grids[2] == GridData("3rd Grid", 24, 48)

    def test_invalid_path(self):
        with pytest.raises(IOError):
            list(iter_grids_from_csv(Path("invalid file")))

    @pytest.mark.xfail
    def test_write_properties(self):
        assert 0, "not implemented yet"

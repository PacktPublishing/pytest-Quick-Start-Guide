import csv
from collections import namedtuple

DATA = """
Main Grid,48,44
2nd Grid,24,21
3rd Grid,24,null
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


def iter_grids_from_csv(lines):
    for fields in csv.reader(lines):
        yield parse_grid_data(fields)


def test_read_properties():
    lines = DATA.strip().splitlines()
    grids = list(iter_grids_from_csv(lines))
    assert grids[0] == GridData("Main Grid", 48, 44)
    assert grids[1] == GridData("2nd Grid", 24, 21)
    assert grids[2] == GridData("3rd Grid", 24, 0)

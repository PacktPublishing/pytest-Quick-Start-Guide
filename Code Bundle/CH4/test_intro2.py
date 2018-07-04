import csv
from series import highest_rated, oldest
import pytest


@pytest.fixture
def comedy_series():
    with open("series.csv", "r", newline="") as file:
        yield list(csv.reader(file))


def test_highest_rated(comedy_series):
    assert highest_rated(comedy_series) == "Seinfeld"


def test_oldest(comedy_series):
    assert oldest(comedy_series) == "Seinfeld"


def write_csv():
    import csv

    with open("series.csv", "w", newline="") as f:
        w = csv.writer(f)
        for c in comedy_series():
            w.writerow(c)

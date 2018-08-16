import csv
from series import highest_rated, oldest
import pytest


@pytest.fixture
def comedy_series():
    with open("series.csv", "r", newline="") as file:
        return list(csv.reader(file))


def test_highest_rated(comedy_series):
    assert highest_rated(comedy_series) == "Seinfeld"


def test_oldest(comedy_series):
    assert oldest(comedy_series) == "Seinfeld"

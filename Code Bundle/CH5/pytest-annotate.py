from operator import itemgetter


def highest_rated(series):
    return sorted(series, key=itemgetter(2))[-1][0]


def test_highest_rated():
    series = [
        ("The Office", 2005, 8.8),
        ("Scrubs", 2001, 8.4),
        ("IT Crowd", 2006, 8.5),
        ("Parks and Recreation", 2009, 8.6),
        ("Seinfeld", 1989, 8.9),
    ]
    assert highest_rated(series) == "Seinfeld"

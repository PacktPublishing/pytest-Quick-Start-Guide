from operator import itemgetter


def highest_rated(series):
    return sorted(series, key=itemgetter(2))[-1][0]


def oldest(series):
    return sorted(series, key=itemgetter(1))[0][0]

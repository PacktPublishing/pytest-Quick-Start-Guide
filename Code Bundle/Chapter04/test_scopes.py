import pytest


def connect_to_db(host, ns):
    return None


class Series:

    def __init__(self, *args):
        pass


class Actors:

    def __init__(self, *args):
        pass


@pytest.fixture(scope="session")
def db():
    db = connect_to_db("localhost", "test")
    db.create_table(Series)
    db.create_table(Actors)
    yield db
    db.prune()
    db.disconnect()


@pytest.fixture(scope="function")
def transaction(db):
    transaction = db.start_transaction()
    yield transaction
    transaction.rollback()


def test_insert(transaction):
    transaction.add(Series("The Office", 2005, 8.8))
    assert transaction.find(name="The Office") is not None

def test_fetch_series(postgresql):
    cur = postgresql.cursor()
    cur.execute("SELECT * FROM comedy_series;")
    assert len(cur.fetchall()) == 5
    cur.close()

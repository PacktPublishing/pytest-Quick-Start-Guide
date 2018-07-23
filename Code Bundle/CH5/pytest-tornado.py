import pytest


@pytest.fixture
def app():
    pass


@pytest.mark.gen_test
def test_tornado(http_client):
    url = "https://docs.pytest.org/en/latest/"
    response = yield http_client.fetch(url)
    assert response.code == 200

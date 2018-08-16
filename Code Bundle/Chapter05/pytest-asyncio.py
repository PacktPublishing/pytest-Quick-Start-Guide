import pytest


async def fetch_requests(url):
    return [1, 2]


@pytest.mark.asyncio
async def test_fetch_requests():
    requests = await fetch_requests("example.com/api")
    assert len(requests) == 2

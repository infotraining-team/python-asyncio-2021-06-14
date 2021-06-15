import asyncio
import pytest
import unittest.mock as mock

async def coro_add(a, b):
    await asyncio.sleep(10)
    return a+b

@pytest.mark.asyncio
async def test_coro_add():
    with mock.patch('asyncio.sleep', mock.AsyncMock(return_value=None)):
        res = await coro_add(3, 4)
        assert res == 7
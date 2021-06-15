from asimplefile import asimplefile
import pytest
import contextlib
import unittest.mock as mock

@pytest.mark.asyncio
async def test_getting_CM():
    with mock.patch('builtins.open', mock.mock_open(read_data="asdads")):
        async with asimplefile("hello.py") as f:
            assert isinstance(f, contextlib.AbstractAsyncContextManager)

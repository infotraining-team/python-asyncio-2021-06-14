from asimplefile import asimplefile
import pytest
import contextlib

@pytest.mark.asyncio
async def test_getting_CM():
    async with asimplefile("hello.py") as f:
        assert isinstance(f, contextlib.AbstractAsyncContextManager)

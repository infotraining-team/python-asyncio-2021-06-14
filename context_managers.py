def unsafe_file():
    f = open("hello.py")
    a = f.read()
    return a

def safe_file():
    with open("hello.py") as f:
        b = f.read()
        f.seek(0)
        a = f.read()
        return a

#print(safe_file())

from contextlib import contextmanager
from contextlib import asynccontextmanager
from types import TracebackType

@contextmanager
def test_cm(param):
    print("beggining")
    try:
        if param == "crash":
            raise ValueError
        yield "this is returned"
    finally:
        print("closing")

with test_cm("safe") as c:
    print("inside scope")
    print(c)
    print("finishing")

import asyncio

@asynccontextmanager
async def client(host, port):
    reader, writer = await asyncio.open_connection(host, port)

    try:
        yield reader, writer

    finally:
        writer.close()
        await asyncio.shield(writer.wait_closed())

async def main():
    async with client("google.pl", 80) as (reader, writer):
        writer.write(b"GET HTTP/1.1\r\n")
        await writer.drain()
        content = await reader.read(100000)
        print(content)

asyncio.run(main())





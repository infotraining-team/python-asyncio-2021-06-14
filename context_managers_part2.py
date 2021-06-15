import asyncio

class Test:
    def __init__(self, param):
        self.param = param

    def __enter__(self):
        print(self.param)
        return self

    def read(self):
        return "asdasdadasds"

    def __exit__(self, ext, exc, tb):
        print("closing")

class Client:
    def __init__(self, host, port):
        self.param = host, port

    async def __aenter__(self):
        self.reader, self.writer = await asyncio.open_connection(*self.param)
        return self.reader, self.writer

    async def __aexit__(self, ext, exc, tb):
        self.writer.close()
        await self.writer.wait_closed()

async def main():
    with Test("asda") as f:
        f.read()

    async with Client("google.pl", 80) as (reader, writer):
        writer.write(b"GET\r\n")
        await writer.drain()
        print(await reader.read(1000000))

asyncio.run(main())
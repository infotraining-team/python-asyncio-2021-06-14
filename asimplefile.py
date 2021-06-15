import asyncio

# async CM
class asimplefile:
    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        self.handler = await asyncio.to_thread(open, self.filename)
        return self

    async def read(self):
        return await asyncio.to_thread(self.handler.read)

    async def __aexit__(self, exc, ext, tb):
        await asyncio.to_thread(self.handler.close)


# target
async def main():
    async with asimplefile("hello.py") as f:
        content = await f.read()
        print(content)

    # async with asimplefile("hello.py") as f:
    #     async for line in f:
    #         print(line)

    # with open("hello.py") as f:
    #     content = f.read()
    #     print(content)

asyncio.run(main())
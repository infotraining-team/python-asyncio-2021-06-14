import asyncio

class Counter:
    def __init__(self, count):
        self.c = count

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.c > 0:
            await asyncio.sleep(0.2)
            self.c -= 1
            return self.c
        else:
            raise StopAsyncIteration

async def main():
    # async for i in Counter(5):
    #     print(i)

    return [i async for i in Counter(3)]

res = asyncio.run(main())
print(res)
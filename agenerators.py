import asyncio
import time

async def agen(n):
    while n >= 0:
        yield n
        await asyncio.sleep(1)
        n -= 1

async def test(n):
    l = []
    async for i in agen(n):
        l.append(i)
    return l

async def main():
    start = time.time()
    tasks = asyncio.gather(test(3), test(3), test(2))
    res = await tasks
    stop = time.time()
    print(res)
    print(f"time: {stop-start}")

asyncio.run(main())

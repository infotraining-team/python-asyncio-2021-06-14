import asyncio
from asimplefile import asimplefile
import os

def get_filenames(startdir):
    for dirpath, _, filenames in os.walk(startdir):
        for fname in filenames:
            if fname.endswith(".py"):
                yield os.path.join(dirpath, fname)

async def producer(in_q):
    for file in get_filenames("."):
        await in_q.put(file)
    await in_q.put(None)

async def process_file(filename):
    counter = 0
    async with asimplefile(filename) as f:
        async for _ in f:
            counter += 1
    return counter

async def consumer(in_q, out_q):
    while True:
        filename = await in_q.get()
        if filename is not None:
            lines = await process_file(filename)
            await out_q.put(lines)
        else:
            await in_q.put(None)
            return

async def summator(out_q):
    sum = 0
    while True:
        res = await out_q.get()
        if res is not None:
            sum += res
            print(f"\rlines = {sum}", end="")
        else:
            print("\r\ndone")
            return

async def main():
    in_q = asyncio.Queue()
    out_q = asyncio.Queue()
    p = asyncio.create_task(producer(in_q))
    cons = asyncio.gather(*[consumer(in_q, out_q) for i in range(10)])
    s = asyncio.create_task(summator(out_q))
    await p
    await cons
    await out_q.put(None)
    await s

asyncio.run(main())


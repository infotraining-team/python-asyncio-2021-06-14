import asyncio

async def producer(q):
    for i in range(50):
        await asyncio.sleep(0.5)
        await q.put(i)

async def consumer(name, q):
    while True:
        t = await q.get()
        print(f"{name} got {t}")

async def main():
    q = asyncio.Queue()
    p = asyncio.create_task(producer(q))
    await asyncio.gather(consumer(1, q), consumer(2, q))
    await p

asyncio.run(main())
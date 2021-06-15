import asyncio

async def producer(q):
    for i in range(10):
        await q.put(i)
        print("-- put --")

async def consumer(name, q):
    while True:
        t = await q.get()
        if t is not None:
            print(f"{name} got {t}")
            await asyncio.sleep(1) # processing
            q.task_done()
        else:
            await q.put(None)
            return

async def main():
    q = asyncio.Queue(3)
    p = asyncio.create_task(producer(q))
    workers = asyncio.gather(consumer(1, q), consumer(2, q))
    await p  # all tasks created
    await q.put(None)
    await workers

asyncio.run(main())
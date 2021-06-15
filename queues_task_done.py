import asyncio

async def producer(q):
    for i in range(10):
        await q.put(i)
        print("-- put --")

async def consumer(name, q):
    try:
        while True:
            t = await q.get()
            print(f"{name} got {t}")
            await asyncio.sleep(1) # processing
            q.task_done()
    except asyncio.CancelledError:
        print(f"{name} finishing")

async def main():
    q = asyncio.Queue(3)
    p = asyncio.create_task(producer(q))
    workers = asyncio.gather(consumer(1, q), consumer(2, q))
    await p  # all tasks created
    await q.join()  # all tasks processed
    workers.cancel()
    try:
        await workers
    except asyncio.CancelledError:
        pass


asyncio.run(main())
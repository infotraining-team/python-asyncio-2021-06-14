import asyncio

async def coro(delay, crash):
    print(f"starting, will sleep for {delay}")
    await asyncio.sleep(delay)
    print("finished waiting")
    if crash:
        raise ValueError
    else:
        return 42

async def main():
    try:
        res = await coro(2, True)
    except ValueError:
        print("crash!!")
        res = None
    return res

async def main_gather():
    tasks = [coro(5, False), coro(2, True)]
    try:
        res = await asyncio.gather(*tasks)
    except ValueError:
        print("crash!!")
        return
    print(res)

async def main_gather_return():
    tasks = [coro(5, False), coro(2, True)]
    res = await asyncio.gather(*tasks, return_exceptions=True)
    print(res)

async def main_wait():
    tasks = [coro(5, False), coro(2, True), coro(1, False)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    for c in done:
        try:
            res = await c
            print(f"got {res}")
        except ValueError:
            print("crash!!!")

async def main_wait_first_ex():
    tasks = [coro(5, False), coro(2, True), coro(1, False)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    for c in done:
        try:
            res = await c
            print(f"got {res}")
        except ValueError:
            print("crash!!!")
    print("wait for pending")
    for c in pending:
        res = await c
        print(f"got {res}")

print(asyncio.run(main_wait_first_ex()))

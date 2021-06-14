import asyncio
import time

def sync_fun(n):
    print(f"sync starting {n}")
    time.sleep(1)
    print(f"continuing {n}")
    time.sleep(1)
    print(f"finishing {n}")
    return n

#res = [sync_fun(1), sync_fun(2)]
#print(res)

async def async_fun(n):
    print(f"async starting {n}")
    await asyncio.sleep(3)
    print(f"continuing {n}")
    t = asyncio.sleep(3)
    await t
    print(f"finishing {n}")
    return n

async def main():
    # res1 = await async_fun(1)
    # res2 = await async_fun(2)
    tasks = asyncio.gather(async_fun(1), async_fun(2), async_fun(3))
    print("tasks started, waiting")
    res = await tasks
    print(f"got {res}")

asyncio.run(main())



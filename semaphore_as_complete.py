import asyncio
import socket
from keyword import kwlist

async def probe(name, sem):
    loop = asyncio.get_running_loop()
    try:
        async with sem:
            res = await loop.getaddrinfo(name, None)
        return(f"{name} already taken")
    except socket.gaierror:
        return(f"{name} not taken")

async def sleep(n):
    await asyncio.sleep(n)
    return n

async def main():
    sem = asyncio.Semaphore(4)
    names = (f"{kw}.pl" for kw in kwlist)
    coros = [probe(name, sem) for name in names]
    for coro in asyncio.as_completed(coros):
        res = await coro
        print(res)

asyncio.run(main())

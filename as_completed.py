import asyncio
import socket
from keyword import kwlist

async def probe(name):
    loop = asyncio.get_running_loop()
    try:
        res = await loop.getaddrinfo(name, None)
        return(f"{name} already taken")
    except socket.gaierror:
        return(f"{name} not taken")

async def sleep(n):
    await asyncio.sleep(n)
    return n

async def main():
    names = (f"{kw}.pl" for kw in kwlist if len(kw) <= 6)
    coros = [probe(name) for name in names]
    for coro in asyncio.as_completed(coros):
        res = await coro
        print(res)

asyncio.run(main())

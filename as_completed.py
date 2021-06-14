import asyncio
import socket
from keyword import kwlist

async def main():
    loop = asyncio.get_running_loop()
    try:
        res = await loop.getaddrinfo("yield.pl", None)
        print(res)
    except socket.gaierror:
        pass

print(list(kw for kw in kwlist if len(kw) <= 6))

asyncio.run(main())

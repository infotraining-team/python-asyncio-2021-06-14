import asyncio
import time

n = 0

async def monitor():
    global n
    while True:
        await asyncio.sleep(1)
        print(f"{n} req/sec")
        n = 0

async def client(address, num):
    global n
    reader, writer = await asyncio.open_connection(*address)
    while True:
        writer.write(b'1000')
        await writer.drain()
        resp = await reader.read(100000)
        #await asyncio.sleep(0.5)
        #print(resp)
        n += 1

async def main():
    await asyncio.gather(*[client(("localhost", 25000), 20) for i in range(8)], monitor())

asyncio.run(main())
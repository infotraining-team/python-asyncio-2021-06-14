import asyncio
import time

CLIENTS = 100

async def client(address):
    reader, writer = await asyncio.open_connection(*address)
    writer.write(b"20000")
    await writer.drain()
    resp = await reader.read(100000)
    print(b'got: ' + resp)
    writer.close()


async def run_clients(address):
    tasks = []
    for i in range(CLIENTS):
        tasks.append(client(address))

    done, pending = await asyncio.wait(tasks, timeout = 1)
    print(f"done = {len(done)}")
    print(f"pending = {len(pending)}")

asyncio.run(run_clients(("localhost", 25000)))
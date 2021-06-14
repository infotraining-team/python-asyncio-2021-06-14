import asyncio
from primes import primes_up_to
from concurrent.futures import ProcessPoolExecutor

pool = ProcessPoolExecutor(8)

async def echo_server(address):
    server = await asyncio.start_server(echo_handler, *address)
    await server.serve_forever()

async def echo_handler(reader, writer):
    while True:
        data = await reader.read(10000)
        if not data:
            break
        try:
            num = int(data)
            #print(f'got {num}')
        except ValueError:
            #print(f'parse error {data}')
            break
        ### CPU intensive - blocking
        # res = primes_up_to(num)
        # res = await asyncio.to_thread(primes_up_to, num)
        loop = asyncio.get_running_loop()
        res = loop.run_in_executor(pool, primes_up_to, num)
        writer.write(f"reply: {res}".encode("utf-8"))
        await writer.drain()
    print("conn closed")
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(echo_server(("", 25000)))
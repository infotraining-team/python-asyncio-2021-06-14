import asyncio

num = 0

async def offset():
    await asyncio.sleep(0.1)
    return 1

async def bad_increment():
    global num
    temp = num
    add = await offset()
    num = temp + add

async def good_increment():
    global num
    add = await offset()
    num += add

async def safe_increment(lock):
    global num
    async with lock:
        num = num + await offset()

async def main():
    tasks = []
    lock = asyncio.Lock()
    for i in range(100):
        tasks.append(good_increment())
    await asyncio.gather(*tasks)
    return num

res = asyncio.run(main())
print(res)
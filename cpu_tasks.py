import asyncio
import time
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

pool = ProcessPoolExecutor(8)

async def task():
    await asyncio.sleep(2)

def slow_task():
    time.sleep(2)

async def async_task():
    #await asyncio.to_thread(slow_task)
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(pool, slow_task)

async def main():
    start = time.time()
    task = async_task
    await asyncio.gather(task(), task(), task())
    end = time.time()
    print("tasks = ", end - start)

if __name__ == "__main__":
    asyncio.run(main())
import asyncio

async def runme():
    await asyncio.sleep(1)
    print("Hello world")

asyncio.run(runme())

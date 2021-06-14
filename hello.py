import asyncio

async def hello(param):
    print("welcome", param)
    await asyncio.sleep(1)
    return 42

#print(type(hello))
#print(type(hello("guest")))

res = asyncio.run(hello("guest"))
print(res)
import asyncio

# async CM
class asimplefile:
    pass

# target
async def main():
    async with asimplefile("hello.py") as f:
        content = await f.read()
        print(content)

    # with open("hello.py") as f:
    #     content = f.read()
    #     print(content)

asyncio.run(main())
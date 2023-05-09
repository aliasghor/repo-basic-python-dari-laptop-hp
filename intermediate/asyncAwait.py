import asyncio

# async def main():
#     print("Tikus")
#     task = asyncio.create_task(gerry('Gerry'))
#     # await task
#     await asyncio.sleep(0.5)
#     print("Selesai")

# async def gerry(text):
#     print(text)
#     await asyncio.sleep(10)

# asyncio.run(main())

"""Async Example"""
async def fetchData():
    print("Start Fetching")
    await asyncio.sleep(2)
    print("Done Fetching")
    return {"data":1}

async def printNumber():
    for i in range(10+1):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetchData())
    task2 = asyncio.create_task(printNumber())

    value = await task1
    print(value)
    await task2

asyncio.run(main())
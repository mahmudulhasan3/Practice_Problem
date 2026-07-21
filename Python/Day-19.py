import time

# def rice():
#     print("Rice")
#     time.sleep(3)
#     print("Cook")

# def veg():
#     print("Cut")

# rice()
# veg()

import asyncio

# async def rice():
#     print("Rice")
#     await asyncio.sleep(3)
#     print("Cook")

# async def veg():
#     print("Cut")

# async def main():
#     await asyncio.gather(
#         rice(),
#         veg()
#     )
# asyncio.run(main())


# import asyncio


# async def say_hi():
#     print("Hi!")


# asyncio.run(say_hi())


import asyncio


async def make_tea():
    print("Tea uthalam")
    await asyncio.sleep(3)
    print("Tea ready")


async def cut_bread():
    print("Cut bread")


async def main():
    await asyncio.gather(make_tea(), cut_bread())


asyncio.run(main())

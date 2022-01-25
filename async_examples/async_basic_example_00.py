# https://docs.python.org/3/library/asyncio-task.html#awaitables
import asyncio

async def nested():
    return 42

async def main():

    nested()


asyncio.run(main())
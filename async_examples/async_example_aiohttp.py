import aiohttp
import asyncio

async def async_example():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_example())

if __name__ == "__main__":
    main()

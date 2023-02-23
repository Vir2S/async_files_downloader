import aiohttp
import asyncio

from time import time


def write_image(data):
    filename = "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, "wb") as f:
        f.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data=data)


async def main():
    url = "https://loremflickr.com/1280/720/"

    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url=url, session=session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    t = time()
    asyncio.run(main())
    print(time() - t)

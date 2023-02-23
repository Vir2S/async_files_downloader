import aiohttp
import asyncio
import requests

from time import time


url = "https://loremflickr.com/1280/720/"


def get_file(url):
    return requests.get(url, allow_redirects=True)


def write_file(response):
    filename = response.url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)


def main():
    t = time()

    url = "https://loremflickr.com/1280/720/"

    for i in range(10):
        write_file(get_file(url=url))

    print(time() - t)


if __name__ == "__main__":
    main()

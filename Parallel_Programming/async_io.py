# Asyncio is a Python library for writing concurrent code using coroutines, which are lightweight threads that can be paused and resumed to allow other coroutines to run. This allows for asynchronous programming, where a single thread can handle multiple I/O-bound tasks without blocking. For example, a web scraper may use asyncio to fetch data from multiple websites concurrently, without waiting for each request to complete before starting the next one.

import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://example.com', 'https://google.com', 'https://github.com']
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())

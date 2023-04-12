import asyncio
import random
import time
 

async def sensor_stream():
    while True:
        reading = random.uniform(0, 1)
        value = yield reading
        await asyncio.sleep(0.5)

async def main():
    async for reading in sensor_stream():
        print(reading)
        await asyncio.sleep(1)

asyncio.run(main())
import json
import asyncio
import aiohttp

data = {"name": "test"}

data = json.dumps(data)
# for _ in range(10000):



async def test():
    session = aiohttp.ClientSession()
    await session.get('http://0.0.0.0:8001/')
    session.close()

loop = asyncio.get_event_loop()

tasks = []
for _ in range(1000):
    tasks.append(test())

loop = asyncio.get_event_loop()
print("running")
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
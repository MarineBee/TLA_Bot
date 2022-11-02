import asyncio
import time

twitter_api_data_path = "D:/TereBin/TtTB/data/twitter_api_data.txt"

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def twitter_main(streamer_json_path, app_data_path):
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

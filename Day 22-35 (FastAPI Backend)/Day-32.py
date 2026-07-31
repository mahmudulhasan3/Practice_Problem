# from fastapi import FastAPI
# import time
# import asyncio

# app = FastAPI()


# async def weather(city: str):
#     print(f"🌤️ Fetching weather for {city}...")
#     await asyncio.sleep(3)
#     return {"city": city, "temperature": "32°C", "condition": "Sunny"}


# async def weather_fetch(city: str):
#     await asyncio.sleep(5)
#     return {"city": city, "temperature": "32°C", "condition": "Sunny"}


# @app.get("/weather/{city}")
# async def check(city: str):
#     data, data2 = await asyncio.gather(weather(city), weather_fetch(city))
#     return {"no": data, "good": data2}


# Mini Project: Farm Dashboard API

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

import time
import asyncio
from fastapi import FastAPI

app = FastAPI()


async def fetch_weather(city: str):
    print("Starting")
    await asyncio.sleep(2)
    print("Ending")
    return {"temperature": "32°C", "condition": "Sunny"}


async def fetch_soil_data(city: str):
    print("Starting")
    await asyncio.sleep(4)
    print("Ending")
    return {"soil_type": "Clay", "moisture": "45%"}


async def fetch_market_price(crop: str):
    print("Starting")
    await asyncio.sleep(3)
    print("Ending")
    return {"crop": crop, "price_per_kg": "৪৫ টাকা"}


@app.get("/farm-dashboard-slow/{city}")
async def farm_dashboard_slow(city: str):
    start = time.time()
    weather = await fetch_weather(city)
    soil = await fetch_soil_data(city)
    crop = await fetch_market_price(city)
    stop = time.time()
    total_time = stop - start
    return {"weather": weather, "soil": soil, "crop": crop, "time": total_time}


@app.get("/farm_dashboard_fast/{city}")
async def farm_dashboard_fast(city: str):
    start = time.time()
    weather, soil, crop = await asyncio.gather(
        fetch_weather(city), fetch_soil_data(city), fetch_market_price(city)
    )
    stop = time.time()
    total_time = stop - start
    return {"weather": weather, "soil": soil, "crop": crop, "time": total_time}


@app.get("/buggy-route")
async def buggy_route():
    time.sleep(5)  
    return {"status": "buggy done"}


@app.get("/ping")
def ping():
    return {"status": "pong"}

import os
from src.endpoints.debug import debug
import random
import datetime


@debug.router.get("/debug/random_number")
async def random_number():
    return {"result": random.random(), "time": datetime.datetime.now()}

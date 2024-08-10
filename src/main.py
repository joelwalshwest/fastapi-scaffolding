from debugpy.server.api import os
from fastapi import FastAPI
from src.endpoints.debug import health_check

if os.getenv("TARGET") == "DEV":
    import debugpy

    debugpy.listen(("127.0.0.1", 5678))

app = FastAPI()

app.include_router(health_check.router)

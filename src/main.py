from fastapi import FastAPI
from src.endpoints.debug import health_check
from src.utils import environment
from src.utils.environment import Environment

if environment.Environment.current() == Environment.LOCAL:
    import debugpy

    debugpy.listen(("127.0.0.1", 5678))

app = FastAPI()

app.include_router(health_check.router)

@app.get("/")
async def root():
    return "i am root, from an automated build # 2"

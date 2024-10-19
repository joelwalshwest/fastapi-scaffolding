from fastapi import FastAPI
from src.endpoints.debug import health_check
from src.utils import environment
from src.utils.environment import Environment
from fastapi.middleware.cors import CORSMiddleware

if environment.Environment.current() == Environment.LOCAL:
    import debugpy

    debugpy.listen(("127.0.0.1", 5678))

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:80",
    "https://react-scaffolding.joelwalshwest.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_check.router)


@app.get("/")
async def root():
    return "I'm just here showing off my automated builds!"

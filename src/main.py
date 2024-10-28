from fastapi import FastAPI
from src.endpoints.heroes import heroes
from src.endpoints.debug import debug
from src.utils import environment
from src.utils.environment import Environment
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from src.database import session

if environment.Environment.current() == environment.Environment.LOCAL:
    import debugpy

    debugpy.listen(("127.0.0.1", 5678))


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=constants.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(debug.router)
app.include_router(heroes.router)

@asynccontextmanager
async def lifespan(_: FastAPI):
    SQLModel.metadata.create_all(session.get_engine())
    yield

@app.get("/")
async def root():
    return "fastapi-scaffolding v0"

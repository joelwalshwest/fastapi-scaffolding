from fastapi import FastAPI
from src.endpoints.debug import debug
from src.utils import environment
from src.utils import constants
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/")
async def root():
    return {}

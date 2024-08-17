from fastapi import Depends, FastAPI
from src.endpoints.debug import health_check
from src.utils import environment
from src.utils.environment import Environment


if environment.Environment.current() == Environment.LOCAL:
    import debugpy

    debugpy.listen(("127.0.0.1", 5678))


app = FastAPI()

app.include_router(health_check.router)

from sqlmodel import Field, SQLModel, create_engine, Session, select
from src.database import connection

engine = connection.get_connection()


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/")
async def root():
    return "I'm just here showing off my automated builds!"


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.post("/heroes/")
def create_hero(*, session: Session = Depends(get_session), hero: Hero):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


@app.get("/heroes")
def read_heroes(*, session: Session = Depends(get_session)):
    heroes = session.exec(select(Hero)).all()
    return heroes

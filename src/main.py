from fastapi import Depends, FastAPI
from src.endpoints.debug import health_check
from src.utils import environment
from src.utils.environment import Environment

import os

import sqlalchemy


def connect_unix_socket() -> sqlalchemy.engine.base.Engine:
    """Initializes a Unix socket connection pool for a Cloud SQL instance of MySQL."""
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.
    db_user = "db-user"
    db_pass = "12345678"
    db_name = "tmp-database"
    unix_socket_path = "/cloudsql/fastapi-scaffolding:us-east1:fastapi-scaffolding-db"

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            database=db_name,
            query={"unix_socket": unix_socket_path},
        ),
        # ...
    )
    return pool


if environment.Environment.current() == Environment.LOCAL:
    import debugpy

    debugpy.listen(("127.0.0.1", 5678))

app = FastAPI()

app.include_router(health_check.router)

from sqlmodel import Field, SQLModel, create_engine, Session, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


engine = connect_unix_socket()


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

from src.database import engine
from src.utils import environment
from sqlmodel import Session

_ENVIRONMENT = environment.Environment.current()
ENGINE = engine.get_engine(_ENVIRONMENT)


def get_session():
    with Session(ENGINE) as session:
        yield session

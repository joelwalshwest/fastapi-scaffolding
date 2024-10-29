from src.database import engine
from src.utils import environment
from sqlmodel import Session

_ENVIRONMENT = environment.Environment.current()
_ENGINE = engine.get_engine(_ENVIRONMENT)


def get_engine():
    return _ENGINE


def get_session():
    with Session(_ENGINE) as session:
        yield session

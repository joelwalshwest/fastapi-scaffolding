import fastapi
from sqlmodel import Session, select
from fastapi import Depends
from src.model import hero
from src.database import session

router = fastapi.APIRouter()


@router.post("/heroes/")
def create_hero(*, session: Session = Depends(session.get_session), hero: hero.Hero):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


@router.get("/heroes")
def read_heroes(*, session: Session = Depends(session.get_session)):
    heroes = session.exec(select(hero.Hero)).all()
    return heroes

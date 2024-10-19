import fastapi
from src.utils import environment as ev

router = fastapi.APIRouter()


@router.get("/debug/health_check")
async def health_check():
    return {"test": "this actually worked"}


@router.get("/debug/environment")
async def environment():
    env = ev.Environment.current()
    secrets = ev.Environment.secrets()
    return {"ENIRONMENT": env, "SECRETS": secrets}

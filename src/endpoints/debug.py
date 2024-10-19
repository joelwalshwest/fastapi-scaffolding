import fastapi
from src.utils import environment as env

router = fastapi.APIRouter()


@router.get("/debug/environment")
async def environment():
    environment = env.Environment.current()
    return {"Environment": environment}


@router.get("/debug/health_check")
async def health_check():
    return "All systems go"

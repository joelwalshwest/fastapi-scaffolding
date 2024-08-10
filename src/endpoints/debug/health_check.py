import fastapi

router = fastapi.APIRouter()


@router.get("/debug/health_check")
async def health_check():
    return "all systems go"

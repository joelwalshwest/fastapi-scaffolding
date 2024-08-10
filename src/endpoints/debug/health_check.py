import fastapi
import os

router = fastapi.APIRouter()


@router.get("/debug/health_check")
async def health_check():

    return "all systems go"


@router.get("/debug/environment")
async def environment():

    env_secrets = ""
    with open("/root/secrets/ENV_SECRETS", "r+") as file_handle:
        env_secrets = file_handle.read()

    return {"ENV": os.getenv("ENVIRONMENT"), "ENV_SECRETS": env_secrets}

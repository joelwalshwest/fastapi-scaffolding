from src.endpoints.debug import debug


@debug.router.get("/debug/health_check")
async def health_check():
    return "all systems go"

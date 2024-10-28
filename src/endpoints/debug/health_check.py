from src.endpoints.debug import debug


@debug.router.get("/debug/health_check")
async def health_check():
    return {"result": "All systems go!"}

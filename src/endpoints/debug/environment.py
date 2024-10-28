from src.utils import environment as ev
from src.endpoints.debug import debug


@debug.router.get("/debug/environment")
async def environment():
    environment = ev.Environment.current()
    return {"Environment": environment}

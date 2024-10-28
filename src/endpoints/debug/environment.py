from src.utils import environment as ev
from src.endpoints.debug import debug


@debug.router.get("/debug/environment")
async def environment():
    env = ev.Environment.current()
    return {"ENV": env.value, "MYSQL_USERNAME": env.MYS_SQL_USERNAME()}

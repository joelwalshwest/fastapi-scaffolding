import enum
import os


class Environment(enum.Enum):
    LOCAL = "local"
    QA = "qa"
    PROD = "prod"

    @classmethod
    def current(cls) -> "Environment":
        match os.getenv("ENVIRONMENT"):
            case "local":
                return Environment.LOCAL
            case "qa":
                return Environment.QA
            case "prod":
                return Environment.PROD
            case _:
                exit(1)

    def MYS_SQL_USERNAME(self) -> str:
        return str(os.getenv("MYSQL_USERNAME"))

    def MYS_SQL_PASSWORD(self) -> str:
        return str(os.getenv("MYSQL_PASSWORD"))

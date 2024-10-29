import enum
import os


class Environment(enum.Enum):
    LOCAL = "local"
    QA = "qa"
    PROD = "prod"

    @classmethod
    def current(cls) -> "Environment":
        print(os.getenv("ENVIRONMENT"))
        match os.getenv("ENVIRONMENT"):
            case "local":
                return Environment.LOCAL
            case "qa":
                return Environment.QA
            case "prod":
                return Environment.PROD
            case _:
                # Default to local 
                return Environment.LOCAL


    def MY_SQL_USERNAME(self) -> str:
        return str(os.getenv("MYSQL_USERNAME"))

    def MY_SQL_PASSWORD(self) -> str:
        return str(os.getenv("MYSQL_PASSWORD"))

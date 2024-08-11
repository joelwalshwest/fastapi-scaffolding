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

    @classmethod
    def secrets(cls) -> str:
        db_username = os.getenv("MYSQL_USERNAME")
        db_password = os.getenv("MYSQL_PASSWORD")
        return db_username + " " + db_password

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
    def get_mysql_username(cls) -> str:
        my_sql_username = os.getenv("MYSQL_USERNAME")
        if my_sql_username is None:
            raise RuntimeError("Expected to have environment populated")

        return my_sql_username

    @classmethod
    def get_mysql_password(cls) -> str:
        my_sql_password = os.getenv("MYSQL_PASSWORD")
        if my_sql_password is None:
            raise RuntimeError("Expected to have environment populated")

        return my_sql_password

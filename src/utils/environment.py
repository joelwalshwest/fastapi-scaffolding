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
        result = ""
        with open("/root/secrets/ENV_SECRETS", "r+") as file_handle:
            result = file_handle.read()

        return result

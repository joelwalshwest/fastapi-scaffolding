import enum
import os


def _EXPORT_ENVIRONMENT_VARIABLES():
    google_application_credentials_file_name = os.getenv(
        "GOOGLE_APPLICATION_CREDENTIALS_FILE_NAME"
    )

    is_running_locally = google_application_credentials_file_name is not None

    if is_running_locally:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
            "/code/.config/gcloud/" + google_application_credentials_file_name
        )


_EXPORT_ENVIRONMENT_VARIABLES()


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
                raise RuntimeError(
                    "Expected to have ENVIRONMENT variable set to one of: 'local', 'qa' or 'prod'"
                )

    def database_name(self) -> str:
        match self:
            case Environment.LOCAL:
                return "local-database.db"
            case Environment.QA:
                return "qa-database"
            case Environment.PROD:
                return "prod-database"

    def MY_SQL_USERNAME(self) -> str:
        return str(os.getenv("MYSQL_USERNAME"))

    def MY_SQL_PASSWORD(self) -> str:
        return str(os.getenv("MYSQL_PASSWORD"))

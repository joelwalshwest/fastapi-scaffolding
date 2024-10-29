from google.cloud.sql.connector import Connector
import pymysql
from src.utils import environment
from sqlalchemy import Engine, create_engine


_CLOUD_SQL_DB_NAME = "fastapi-scaffolding:us-east1:fastapi-scaffolding-db"
_DB_USERNAME = environment.Environment.current().MY_SQL_USERNAME()
_DB_PASSWORD = environment.Environment.current().MY_SQL_PASSWORD()
_DB_NAME = environment.Environment.current().database_name()

if environment.Environment.current() != environment.Environment.LOCAL:
    _CONNECTOR = Connector()


def get_engine(env: environment.Environment) -> Engine:
    match env:
        case environment.Environment.QA | environment.Environment.PROD:
            return _get_cloud_connection()
        case environment.Environment.LOCAL:
            return _get_local_connection()


def _get_local_connection() -> Engine:
    return create_engine("sqlite:///" + _DB_NAME)


def _get_cloud_connection() -> Engine:
    return create_engine("mysql+pymysql://", creator=_cloud_connection_creator)


def _cloud_connection_creator() -> pymysql.connections.Connection:
    instance_connection_str = _get_cloud_connection_str(
        environment.Environment.current()
    )

    return _CONNECTOR.connect(
        instance_connection_str,
        "pymysql",
        user=_DB_USERNAME,
        password=_DB_PASSWORD,
        db=_DB_NAME,
    )


def _get_cloud_connection_str(env: environment.Environment) -> str:
    match env:
        case environment.Environment.QA | environment.Environment.PROD:
            return _CLOUD_SQL_DB_NAME
        case _:
            raise ValueError("Cloud connection str does not apply to LOCAL environment")

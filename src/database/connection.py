from google.cloud.sql.connector import Connector
import pymysql
import sqlalchemy
from src.endpoints.debug.health_check import environment
from src.utils.environment import Environment
from sqlalchemy import Engine, create_engine


if Environment.current() is not Environment.LOCAL:
    _CONNECTOR = Connector()


# To save money, prod and qa are the
_PROD_DB_CONNECTION_NAME = "fastapi-scaffolding:us-east1:fastapi-scaffolding-db"
_QA_DB_CONNECTION_NAME = "fastapi-scaffolding:us-east1:fastapi-scaffolding-db"
_LOCAL_DB_FIILE_NAME = "database.db"
_DB_USERNAME = Environment.get_mysql_username()
_DB_PASSWORD = Environment.get_mysql_password()


def get_connection() -> Engine:
    match Environment.current():
        case Environment.QA, Environment.PROD:
            return _get_cloud_connection()
        case Environment.LOCAL:
            return _get_local_connection()
        case _:
            raise ValueError("")


def _get_local_connection() -> Engine:
    return create_engine("sqlite:///" + _LOCAL_DB_FIILE_NAME)


def _get_cloud_connection() -> Engine:
    return create_engine("mysql+pymysql://", creator=_cloud_connection_creator)


def _cloud_connection_creator() -> pymysql.connections.Connection:
    instance_connection_str = _get_cloud_connection_str()
    return _CONNECTOR.connect(
        instance_connection_str,
        "pymysql",
        user=_DB_USERNAME,
        password=_DB_PASSWORD,
        db="tmp-database",
    )


def _get_cloud_connection_str() -> str:
    match Environment.current():
        case Environment.QA, Environment.PROD:
            return _PROD_DB_CONNECTION_NAME
        case _:
            raise ValueError("")

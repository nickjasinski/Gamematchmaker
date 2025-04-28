from db_config import DB_CONFIG
from postgres_db import PostgresDB
from postgres_handler import PostgresHandler


class DatabaseFactory:
    @staticmethod
    def getHandler():
        from db_config import DB_CONFIG
        db = PostgresDB(DB_CONFIG)
        db.connect()
        return PostgresHandler(db)

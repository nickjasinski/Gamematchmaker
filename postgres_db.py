import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional
from abstract_db import AbstractDB


class PostgresDB(AbstractDB):
    def __init__(self, config):
        self.config = config
        self.connection: Optional[psycopg2.extensions.connection] = None

    def connect(self):
        self.connection = psycopg2.connect(**self.config)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def getSession(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)

    def getConnection(self):
        return self.connection

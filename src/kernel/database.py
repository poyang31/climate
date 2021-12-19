from pymongo import MongoClient
from pymongo.database import Collection

from .config import Config


class Database:
    def __init__(self, config: Config):
        self.config = config
        dsn = self.config.get("database.dsn")
        self._client = MongoClient(dsn)

    def get_client(self) -> MongoClient:
        return self._client

    def get_collection(self, name: str) -> Collection:
        db_name = self.config.get("database.name")
        db = self.get_client().get_database(db_name)
        return db.get_collection(name)

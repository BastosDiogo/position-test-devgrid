import os
from dotenv import load_dotenv

import pymongo

load_dotenv()

class Pymongo:
    def __init__(self) -> None:
        MONGO_HOST = os.getenv("MONGO_HOST")
        MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
        MONGO_USERNAME = os.getenv("MONGO_USERNAME")
        self.client = pymongo.MongoClient(
            f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}{MONGO_HOST}",
            tls=True,
            tlsCAFile="isrgrootx1.pem",
            tlsAllowInvalidHostnames=True,
            retryWrites=False,
        )
        self._database = self.client[os.getenv("DATABASE_ENVIROMENT")]

    @property
    def database(self):
        return self._database

    @property
    def lista_colections(self):
        try:
            self.database.list_collection_names()
            return True
        except:
            return False
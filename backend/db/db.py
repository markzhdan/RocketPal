
from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
URI = os.environ.get("URI")
DB_NAME = os.environ.get("DB_NAME")

class Database:
    def __init__(self):
        self.client = MongoClient(URI)

    def close(self):
        self.client.close()

    def get_database(self):
        return self.client[DB_NAME]

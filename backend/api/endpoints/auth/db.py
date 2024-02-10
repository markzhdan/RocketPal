
from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://parkjae433:zBazf6Rzca8N4ccr@rocketpalcluster.txs3ukk.mongodb.net/?retryWrites=true&w=majority"
# db_name = "RocketPalDB"

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://parkjae433:zBazf6Rzca8N4ccr@rocketpalcluster.txs3ukk.mongodb.net/?retryWrites=true&w=majority")

    def close(self):
        self.client.close()

    def get_database(self):
        return self.client["RocketPalDB"]

# # Singleton database instance
# client = Database().get_database()

# for user in client['Users'].find():
#     print(user)
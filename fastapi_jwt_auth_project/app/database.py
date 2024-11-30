from pymongo import MongoClient

client = MongoClient("your_mongodb_connection_string")
db = client.get_database("your_database_name")
user_collection = db.get_collection("users")

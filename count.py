from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["aintboard"]  # Replace "your_db_name" with the name of your database
collection = db["test_bgg"]

count = collection.count_documents({})
print(count)
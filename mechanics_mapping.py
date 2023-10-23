from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["aintboard"]  # Replace "your_db_name" with the name of your database

# Access the collections
mechanics_collection = db["mechanics"]
boardgame_collection = db["bg"]

# Initialize an empty list to hold the mappings
mappings = []

# Iterate through the documents in the boardgame collection
for doc in boardgame_collection.find():
    # Get the Mechanics field value from the document
    mechanics_value = doc.get("Mechanics")
    if mechanics_value and isinstance(mechanics_value, str):
        # Split the Mechanics field value on comma and space
        mechanic_strings = mechanics_value.split(", ")
        # Initialize an empty list to hold the IDs for this document
        mechanic_ids = []
        # Iterate through the mechanic strings
        for mechanic_string in mechanic_strings:
            # Look up the corresponding document in the mechanics collection
            mechanics_doc = mechanics_collection.find_one({"value": mechanic_string})
            if mechanics_doc:
                # Add the _id to the list of IDs for this document
                mechanic_ids.append(str(mechanics_doc["_id"]))
        # Create a mapping for this document
        mapping = {
            "bg_id": doc["_id"],
            "mechanics_ids": mechanic_ids
        }
        # Add the mapping to the list of mappings
        mappings.append(mapping)

# Optionally, store the mappings in a new collection in MongoDB
mapping_collection = db["mechanics_mapping"]
mapping_collection.insert_many(mappings)
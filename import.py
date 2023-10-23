import pandas as pd
from pymongo import MongoClient

# Load the CSV file into a pandas DataFrame
url = "bgg_dataset.csv"
df = pd.read_csv(url, delimiter=';')

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["aintboard"]  # replace "your_db_name" with the name of your database
collection = db["bg"]  # replace "your_collection_name" with the name of your collection

# Convert the DataFrame to a list of dictionaries and insert them into the MongoDB collection
records = df.to_dict(orient="records")
collection.insert_many(records)

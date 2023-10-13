import pandas as pd
from pymongo import MongoClient

# Load the CSV file into a pandas DataFrame
url = "bgg_dataset.csv"
df = pd.read_csv(url, delimiter=';')

# Group Domains to distinct values
# Select the column of interest
column = df['Domains']  # Replace 'your_column_name' with the name of the column

# Initialize an empty set to collect the distinct values
distinct_values = set()

# Split the values in the column on commas, and iterate through the resulting lists
for value_list in column.str.split(', '):
    if not isinstance(value_list, list):  # Handle missing or NaN values
        continue
    # Add each value from the list to the set of distinct values
    distinct_values.update(value_list)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["aintboard"]  # replace "your_db_name" with the name of your database
collection = db["domains"]  # replace "your_new_collection_name" with the name of your new collection

# Convert the set of distinct values to a list of dictionaries
records = [{"value": value} for value in distinct_values]

# Insert the list of dictionaries into the new MongoDB collection
collection.insert_many(records)